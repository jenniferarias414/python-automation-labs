import pandas as pd  # Organizes lineage rows into a table/DataFrame.
import sqlglot  # Parses SQL text into objects Python can inspect.
from sqlglot import exp  # SQL expression classes like Column, Table, Select.
import streamlit as st  # Creates the local browser-based GUI.
from pathlib import Path  # Makes file paths cleaner and cross-platform.


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

SAMPLE_SQL_FILE = DATA_DIR / "sample_baggage_claim_query.sql"
OUTPUT_CSV_FILE = OUTPUT_DIR / "lineage_output.csv"


def load_sample_sql() -> str:
    """
    Load the sample airline SQL query from the data folder.
    """

    return SAMPLE_SQL_FILE.read_text()


def get_table_aliases(parsed_query: exp.Expression) -> dict:
    """
    Build a dictionary that maps SQL aliases to real table names.

    Example:
        FROM baggage_claims c
        JOIN customers cust

    Alias map:
        c    -> baggage_claims
        cust -> customers
    """

    alias_map = {}

    for table in parsed_query.find_all(exp.Table):
        table_name = table.name
        alias = table.alias_or_name
        alias_map[alias] = table_name

    return alias_map


def resolve_source_table(column: exp.Column, alias_map: dict, all_tables: list[str]) -> str:
    """
    Resolve the source table for a SQL column.

    Example:
        c.claim_id -> baggage_claims.claim_id
    """

    table_or_alias = column.table

    if table_or_alias:
        return alias_map.get(table_or_alias, table_or_alias)

    if len(all_tables) == 1:
        return all_tables[0]

    return "Unknown"


def classify_transformation(select_expression: exp.Expression) -> str:
    """
    Label output columns as DIRECT or TRANSFORMED.
    """

    if isinstance(select_expression, exp.Column):
        return "DIRECT"

    return "TRANSFORMED"


def extract_lineage(sql_text: str) -> pd.DataFrame:
    """
    Parse SQL and extract simplified column-level lineage.

    Output:
        output_column -> source_table -> source_column -> transformation_type
    """

    parsed_query = sqlglot.parse_one(sql_text)
    alias_map = get_table_aliases(parsed_query)
    all_tables = sorted(set(alias_map.values()))
    lineage_rows = []

    for select in parsed_query.find_all(exp.Select):
        for select_expression in select.expressions:
            output_column = select_expression.alias_or_name
            source_columns = list(select_expression.find_all(exp.Column))

            for source_column in source_columns:
                source_table = resolve_source_table(
                    source_column,
                    alias_map,
                    all_tables,
                )

                lineage_rows.append(
                    {
                        "output_column": output_column,
                        "source_table": source_table,
                        "source_column": source_column.name,
                        "transformation_type": classify_transformation(select_expression),
                        "sql_expression": select_expression.sql(pretty=True),
                    }
                )

    return pd.DataFrame(lineage_rows)


def save_lineage_to_csv(lineage_df: pd.DataFrame) -> None:
    """
    Save lineage results to a CSV file for review or documentation.
    """

    OUTPUT_DIR.mkdir(exist_ok=True)
    lineage_df.to_csv(OUTPUT_CSV_FILE, index=False)


st.set_page_config(
    page_title="Baggage Claim SQL Lineage Tool",
    layout="wide",
)

st.title("Baggage Claim SQL Lineage Tool")
st.write(
    "Paste a SQL query to see which source tables and columns feed each output column."
)

with st.expander("What is data lineage?", expanded=True):
    st.write(
        """
        Data lineage explains where data comes from and how it moves through a query or pipeline.

        In this project, lineage means:
        **output column → source table → source column → transformation logic**
        """
    )

sample_sql = load_sample_sql()

sql_input = st.text_area(
    "SQL Query",
    value=sample_sql,
    height=350,
)

if st.button("Parse SQL Lineage"):
    try:
        lineage_df = extract_lineage(sql_input)

        if lineage_df.empty:
            st.warning("No lineage found. Try a SELECT query with source columns.")
        else:
            save_lineage_to_csv(lineage_df)

            st.success("Lineage parsed successfully.")
            st.subheader("Lineage Results")
            st.dataframe(lineage_df, width="stretch")

            st.download_button(
                label="Download Lineage CSV",
                data=lineage_df.to_csv(index=False),
                file_name="lineage_output.csv",
                mime="text/csv",
            )

            st.info(f"Lineage output also saved locally to: {OUTPUT_CSV_FILE}")

    except Exception as error:
        st.error(f"Error parsing SQL: {error}")
        st.write(
            "Tip: Make sure the SQL is a valid SELECT statement. "
            "This learning tool works best with straightforward SELECT/JOIN queries."
        )
