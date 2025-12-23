from stats import detect_anomalies, n_slowest_latencies

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

with open ("generated.log","r") as file:
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
        if is_warn:
                warn_count+=1
        if is_info:
                info_count+=1
        if latency is not None:
            all_latency.append(latency)
            if is_error:
                error_latency.append(latency)
            
    print("\nLog Summary")
    print("-----------")
    print("Total requests processed : ",len(all_latency))
    print("INFO events: ", info_count)
    print("WARN events: ", warn_count)
    print("ERROR events: ", error_count)
    

anomalies_latency, average_latency, threshold_latency, median_latency=detect_anomalies(all_latency)
top_n=n_slowest_latencies(all_latency, 5)

print("\nLatency Metrics")
print("---------------")
print("Average latency (ms): ", round(average_latency, 2))
print("Median Latency:", median_latency)
print("Anomaly threshold (ms): ", round(threshold_latency, 2))
print("Number of anomalies: ", len(anomalies_latency))
print("Top 5 slowest requests (ms): ", top_n)
print("ERROR rate: ", (error_count/len(all_latency))*100)



