import statistics

# top n slowest latencies
def n_slowest_latencies(latencies, n):
    temp = latencies.copy()
    temp.sort(reverse=True)
    top_n = temp[:n]
    return top_n

# Flags unusually high latencies using a mean + 3σ threshold
def detect_anomalies(latencies):
    average_latency = statistics.mean(latencies)
    std_latency = statistics.stdev(latencies)
    threshold_latency = average_latency + 3 * std_latency
    median_latency=statistics.median(latencies)

    anomalies_latency = []
    for x in latencies:
        if x > threshold_latency:
            anomalies_latency.append(x)
    return anomalies_latency, average_latency, threshold_latency, median_latency


