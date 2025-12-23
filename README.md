```md
# SYSTEM LOG ANALYZER

A lightweight command-line tool for processing system logs and summarizing latency behavior and event patterns using statistical analysis.

---

## Overview

Modern systems generate large volumes of log data describing request handling, warnings, failures, and performance metrics. While logs are essential for monitoring and debugging, reading raw log files line by line does not scale as system size grows.

This project processes structured log files and produces concise summaries that describe **what is happening in the system**, enabling engineers to quickly assess system behavior before deeper investigation.

The tool focuses on **observation and reporting**, not diagnosis.

---

## System Flow

```

┌──────────────┐
│ generated.log│
└──────┬───────┘
│
v
┌────────────────────┐
│ Line-by-line read  │
└──────┬─────────────┘
│
v
┌────────────────────┐
│ Tokenize log entry │
└──────┬─────────────┘
│
v
┌─────────────────────────────┐
│ Extract event level & latency│
└──────┬──────────────────────┘
│
v
┌─────────────────────────────┐
│ Aggregate counts & latencies│
└──────┬──────────────────────┘
│
v
┌─────────────────────────────┐
│ Statistical analysis        │
│ (mean, median, threshold)  │
└──────┬──────────────────────┘
│
v
┌─────────────────────────────┐
│ Structured summary output   │
└─────────────────────────────┘

```

---

## What the Analyzer Does

- Reads log entries from a text file
- Identifies INFO, WARN, and ERROR events
- Extracts latency values from each entry
- Aggregates request counts and error counts
- Computes latency statistics:
  - Mean
  - Median
  - Standard deviation
- Detects unusually slow requests
- Reports top-N slowest latencies
- Prints a structured summary to standard output

The analyzer intentionally does **not** attempt to explain causes or infer root problems.

---

## Log Format

Each log entry must follow the format:

```

YYYY-MM-DD HH:MM:SS <LEVEL> latency=<value>

```

Example:
```

2024-12-21 10:00:31 ERROR latency=980

```

Where:
- `<LEVEL>` ∈ {INFO, WARN, ERROR}
- `latency` is measured in milliseconds

---

## Anomaly Detection Logic

Latency anomalies are detected using a statistical threshold:

```

threshold = mean_latency + 3 × standard_deviation

```

Any latency value exceeding this threshold is flagged as anomalous.

This method is deterministic, explainable, and commonly used in monitoring systems.

---

## Project Structure

```

log-analyzer/
├── analyzer.py    # parsing, aggregation, reporting
├── stats.py       # statistical computations
├── generated.log  # input log file
└── README.md

```

---

## Example Output

```

## Log Summary

Total requests processed : 1000
INFO events : 742
WARN events : 181
ERROR events: 77

## Latency Metrics

Average latency (ms): 164.32
Median latency (ms): 128
Anomaly threshold (ms): 684.21
Number of anomalies: 19
Top 5 slowest requests (ms): [1298, 1276, 1259, 1234, 1218]
ERROR rate: 7.7%

````

---

## Design Notes

- Parsing logic and statistical logic are separated
- All computation uses the Python standard library
- The analyzer operates offline on log files
- Log generation (if used) is decoupled from analysis

---

## Limitations

- Assumes a single log format
- Offline analysis only
- No root cause inference
- No visualization layer

---

## Requirements

- Python 3.x
- No external dependencies

---

## Usage

```bash
python analyzer.py generated.log
````

---

## Scope Statement

This tool answers **what is happening** in the system.
Explaining **why it is happening** is intentionally out of scope.

```
```
