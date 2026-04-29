import requests  # Sends HTTP requests to webpages.
import pandas as pd  # Stores extracted records in a table and writes CSV output.
from lxml import html  # Parses raw HTML into a searchable HTML tree.
from pathlib import Path  # Handles file paths cleanly.


BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"

BOOKS_URL = "https://books.toscrape.com/"


def fetch_html(url: str) -> str:
    """
    Send an HTTP GET request and return the webpage HTML.

    This is the "crawling" or "fetching" stage:
    Python asks the website for the page content.
    """

    response = requests.get(url, timeout=10)

    # Raise an error if the request failed.
    response.raise_for_status()

    return response.text


def parse_books(html_text: str) -> list[dict]:
    """
    Parse book records from the HTML.

    This is the "parsing" or "extraction" stage:
    Python searches the HTML tree for book data.
    """

    html_tree = html.fromstring(html_text)

    # Each book on the page is stored inside an <article> tag.
    book_cards = html_tree.xpath("//ol/li/article")

    books = []

    for book in book_cards:
        title = book.xpath(".//h3/a/@title")[0]
        relative_url = book.xpath(".//h3/a/@href")[0]
        price = book.xpath(".//p[@class='price_color']/text()")[0]
        availability = book.xpath(".//p[contains(@class, 'instock')]/text()")
        rating_class = book.xpath(".//p[contains(@class, 'star-rating')]/@class")[0]

        # Example class value: "star-rating Three"
        rating = rating_class.replace("star-rating", "").strip()

        books.append(
            {
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability[-1].strip() if availability else "Unknown",
                "product_url": f"{BOOKS_URL}{relative_url}",
            }
        )

    return books


def save_outputs(books: list[dict]) -> None:
    """
    Save extracted book data and a small summary report.
    """

    OUTPUT_DIR.mkdir(exist_ok=True)

    df = pd.DataFrame(books)

    csv_path = OUTPUT_DIR / "books.csv"
    summary_path = OUTPUT_DIR / "summary.txt"

    df.to_csv(csv_path, index=False)

    # Clean price column for basic analysis.
    df["price_numeric"] = (
        df["price"]
        .str.replace("£", "", regex=False)
        .str.replace("Â", "", regex=False)
        .astype(float)
)

    with summary_path.open("w") as file:
        file.write("Bookstore Web Data Pipeline Summary\n")
        file.write("===================================\n\n")
        file.write(f"Books extracted: {len(df)}\n")
        file.write(f"Average price: £{df['price_numeric'].mean():.2f}\n")
        file.write(f"Highest price: £{df['price_numeric'].max():.2f}\n")
        file.write(f"Lowest price: £{df['price_numeric'].min():.2f}\n")
        file.write("\nRating counts:\n")

        for rating, count in df["rating"].value_counts().items():
            file.write(f"- {rating}: {count}\n")

    print(f"Extracted {len(df)} books")
    print(f"CSV saved to: {csv_path}")
    print(f"Summary saved to: {summary_path}")


def main() -> None:
    """
    Main ETL-style workflow:
    Extract HTML -> Transform into structured rows -> Load to CSV/report.
    """

    html_text = fetch_html(BOOKS_URL)
    books = parse_books(html_text)
    save_outputs(books)


if __name__ == "__main__":
    main()
