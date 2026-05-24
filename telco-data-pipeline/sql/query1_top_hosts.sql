SELECT
    host,

    COUNT(*) AS total_problem_alerts,

    SUM(
        CASE
            WHEN severity = 'High'
            THEN 1
            ELSE 0
        END
    ) AS high_alerts,

    SUM(
        CASE
            WHEN severity = 'Average'
            THEN 1
            ELSE 0
        END
    ) AS average_alerts,

    SUM(
        CASE
            WHEN severity = 'Warning'
            THEN 1
            ELSE 0
        END
    ) AS warning_alerts,

    SUM(
        CASE
            WHEN severity = 'Disaster'
            THEN 1
            ELSE 0
        END
    ) AS disaster_alerts

FROM alerts

WHERE alert_type = 'Problem'

GROUP BY host

ORDER BY total_problem_alerts DESC

LIMIT 5;