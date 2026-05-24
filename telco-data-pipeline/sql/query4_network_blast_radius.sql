SELECT
    a.host,

    a.problem_name,

    COUNT(t.destination_node)
        AS connected_devices_count

FROM alerts a

LEFT JOIN topology t
ON a.host = t.hostname

WHERE a.alert_type = 'Problem'

AND NOT EXISTS (

    SELECT 1

    FROM alerts r

    WHERE r.host = a.host
    AND r.problem_name = a.problem_name
    AND r.alert_type = 'Resolved'
)

GROUP BY
    a.host,
    a.problem_name

ORDER BY connected_devices_count DESC;