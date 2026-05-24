WITH overloaded_cells AS (

    SELECT
        object_name,
        endtime_utc,
        prb_utilization_pct,

        CASE
            WHEN prb_utilization_pct > 90
            THEN 1
            ELSE 0
        END AS overloaded

    FROM kpi_data
),

grouped_overloads AS (

    SELECT
        object_name,
        endtime_utc,

        ROW_NUMBER() OVER (
            PARTITION BY object_name
            ORDER BY endtime_utc
        )

        -

        ROW_NUMBER() OVER (
            PARTITION BY object_name, overloaded
            ORDER BY endtime_utc
        ) AS grp

    FROM overloaded_cells

    WHERE overloaded = 1
)

SELECT
    object_name,

    MIN(endtime_utc)
        AS overload_start_time,

    COUNT(*) AS duration_minutes

FROM grouped_overloads

GROUP BY
    object_name,
    grp

HAVING COUNT(*) >= 3

ORDER BY duration_minutes DESC;