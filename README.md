# system-log-analyzer

A lightweight Python utility for parsing structured system logs, aggregating latency metrics, and identifying anomalously slow requests using deterministic statistical methods.
This project focuses on **clarity, correctness, and explainability**, mirroring how foundational observability tools are built in real systems.

---

## Problem Statement

Raw system logs contain useful performance signals, but extracting consistent metrics from large log files is tedious and error-prone.

This tool demonstrates how to stream logs, aggregate latency and error data, and surface unusually slow requests without external dependencies or opaque heuristics.

---

## Overview

System logs are often the first signal of performance degradation.  
This tool processes raw log files to extract latency data, classify event types, and surface unusually slow requests through simple statistical thresholds.

It does **not** attempt root-cause analysis, prediction, or automated remediation.

---

## Key Features

- Parses structured log entries line by line  
- Extracts and aggregates latency values  
- Counts INFO, WARN, and ERROR events  
- Computes average and median latency  
- Detects anomalous latencies using a statistical threshold  
- Reports the top N slowest requests  
- Calculates error rate across processed requests  

All computation is performed locally using Python’s standard library.

---

## Design Philosophy

This project avoids machine learning and external dependencies by design.

It focuses on demonstrating how raw operational data can be transformed into actionable metrics using simple parsing and deterministic statistics.

---

## Processing Flow

```text

┌────────────────────────────┐
│ Log Generation             │
│ (generate_log.py)          │
│                            │
│ - Uses random module       │
│ - Generates ~100k entries  │
│ - Writes to generated.log  │
└───────────────┬────────────┘
                │
                ▼
┌────────────────────────────┐
│ Log File                   │
│ (generated.log)            │
└───────────────┬────────────┘
                │
                ▼
┌────────────────────────────┐
│ Read file line by line     │
│ (streaming, not in-memory) │
└───────────────┬────────────┘
                │
                ▼
┌────────────────────────────┐
│ Tokenize log entry         │
│ into parts                 │
└───────────────┬────────────┘
                │
                ▼
┌────────────────────────────┐
│ Extract fields             │
│ - latency                  │
│ - INFO / WARN / ERROR      │
└───────────────┬────────────┘
                │
                ▼
┌────────────────────────────┐
│ Aggregate metrics          │
│ - latency list             │
│ - error-specific latency  │
│ - event counters           │
└───────────────┬────────────┘
                │
                ▼
┌────────────────────────────┐
│ Statistical analysis       │
│ - mean latency             │
│ - median latency           │
│ - anomaly threshold        │
│ - slowest N requests       │
└───────────────┬────────────┘
                │
                ▼
┌────────────────────────────┐
│ Console summary output     │
└────────────────────────────┘

```

# Project Structure
log-analyzer/
├── analyze_logs.py   # Streaming log parsing and metric aggregation
├── stats.py          # Statistical utilities and anomaly detection
├── generate_log.py   # Synthetic log generation for testing
├── generated.log     # Sample log file
└── README.md

---

# Requirements

Python 3.x
No third-party libraries

---

# Output Summary

The analyzer reports:

- Total requests processed
- Count of INFO, WARN, and ERROR events
- Average and median latency (ms)
- Anomaly threshold (mean + kσ)
- Number of anomalous requests
- Top N slowest latencies
- Overall error rate
- All values are derived directly from the input log file.

---

## Notes

- Malformed log entries or entries missing a latency field are skipped rather than terminating processing.
- Anomaly detection is purely statistical and deterministic
- Results are intended for inspection, not automated decision-making
- The project favors transparency over sophistication
