import statistics

def detect_anomalies(latencies):
    average_latency = statistics.mean(latencies)
    std_latency = statistics.stdev(latencies)
    threshold_latency = average_latency + 3 * std_latency

    anomalies_latency = []
    for x in latencies:
        if x > threshold_latency:
            anomalies_latency.append(x)

    return anomalies_latency, average_latency, threshold_latency

# top n slowest latencies
def n_slowest_latencies(latencies, n):
    temp = latencies.copy()
    temp.sort(reverse=True)
    top_n = temp[:n]
    return top_n
