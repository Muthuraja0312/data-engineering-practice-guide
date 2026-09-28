WITH start_city AS (
    SELECT r1.id, r1.origin
    FROM routes r1
    LEFT JOIN routes r2
        ON r1.id = r2.id
       AND r1.origin = r2.destination
    WHERE r2.destination IS NULL
),
end_city AS (
    SELECT r1.id, r1.destination
    FROM routes r1
    LEFT JOIN routes r2
        ON r1.id = r2.id
       AND r1.destination = r2.origin
    WHERE r2.origin IS NULL
)
SELECT s.id,
       s.origin,
       e.destination
FROM start_city s
JOIN end_city e
    ON s.id = e.id;
