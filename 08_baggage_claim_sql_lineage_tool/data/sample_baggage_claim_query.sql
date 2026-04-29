-- Sample airline baggage claim query
-- This query joins baggage claims, bag scan events, and customer data.
-- The goal is to produce an operational report showing open claims,
-- the impacted customer, the latest scan airport, and compensation amount.

SELECT
    c.claim_id,
    c.claim_status,
    c.claim_created_date,
    b.bag_tag_number,
    b.origin_airport,
    b.destination_airport,
    s.last_scan_airport,
    s.last_scan_time,
    cust.customer_name,
    cust.loyalty_tier,
    c.compensation_amount,
    CASE
        WHEN c.compensation_amount > 100 THEN 'High Priority'
        ELSE 'Standard Priority'
    END AS claim_priority
FROM baggage_claims c
JOIN baggage b
    ON c.bag_tag_number = b.bag_tag_number
JOIN bag_scan_events s
    ON b.bag_tag_number = s.bag_tag_number
JOIN customers cust
    ON c.customer_id = cust.customer_id
WHERE c.claim_status IN ('Open', 'Investigating');
