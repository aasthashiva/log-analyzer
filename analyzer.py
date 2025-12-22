def parse_in_parts(parts):
    is_error="ERROR" in parts
    is_warn="WARN" in parts
    is_info="INFO" in parts
    latency=None
    for part in parts:
        if part.startswith("latency="):
            latency=int(part.split("=")[1])
            break
    return latency, is_error, is_warn, is_info

with open ("sample.log","r") as file:
    error_count=0
    warn_count=0
    info_count=0

    all_latency=[]
    error_latency=[]
    for line in file:
        parts=line.strip().split()
        latency, is_error, is_warn, is_info=parse_in_parts(parts)
        if is_error:
            error_count=error_count+1
        if latency is not None:
            all_latency.append(latency)
            if is_error:
                error_latency.append(latency)
            if is_warn:
                warn_count+=1
            if is_info:
                info_count+=1
    print("Latency Record:",all_latency)
    print("Error Record:",error_latency)
    print("ERROR occurred:", error_count, " times")
    print("WARN occurred:",warn_count, " times")
    print("INFO occurred:",info_count, " times")

from stats import detect_anomalies, n_slowest_latencies
anomalies_latency, average_latency, threshold_latency=detect_anomalies(all_latency)
top_n=n_slowest_latencies(all_latency, 5)

print("Average Latency:", average_latency)
print("Anomaly Threshold:", threshold_latency)
print("Anomalous Latencies:", anomalies_latency)
print("Top 5 Slowest Latencies:", top_n)





