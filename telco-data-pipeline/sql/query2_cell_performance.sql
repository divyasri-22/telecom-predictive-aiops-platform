SELECT
    object_name,

    AVG(dl_throughput_mbps)
        AS avg_dl_throughput,

    AVG(ul_throughput_mbps)
        AS avg_ul_throughput,

    MAX(prb_utilization_pct)
        AS peak_prb_utilization,

    MAX(connected_users)
        AS peak_connected_users

FROM kpi_data

GROUP BY object_name

ORDER BY peak_prb_utilization DESC;