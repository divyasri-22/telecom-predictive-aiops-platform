WITH problem_alerts AS (

    SELECT
        host,
        problem_name,
        timestamp AS problem_time

    FROM alerts

    WHERE alert_type = 'Problem'
),

resolved_alerts AS (

    SELECT
        host,
        problem_name,
        timestamp AS resolved_time

    FROM alerts

    WHERE alert_type = 'Resolved'
)

SELECT
    p.host,

    AVG(
        EXTRACT(
            EPOCH FROM (
                r.resolved_time - p.problem_time
            )
        ) / 60
    ) AS avg_resolution_minutes

FROM problem_alerts p

JOIN resolved_alerts r
ON p.host = r.host
AND p.problem_name = r.problem_name

GROUP BY p.host;