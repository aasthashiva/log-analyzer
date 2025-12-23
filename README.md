# log-analyzer

A lightweight Python utility for parsing structured system logs, aggregating latency metrics, and identifying anomalously slow requests using deterministic statistical methods.

This project focuses on **clarity, correctness, and explainability**, mirroring how foundational observability tools are built in real systems.

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

This project intentionally avoids machine learning and external dependencies.

The objective is to demonstrate how **raw operational data** can be transformed into **actionable metrics** using straightforward parsing and statistics—techniques that remain foundational even in large-scale systems.

---

## Processing Flow

```text
┌───────────────┐
│  Log File     │
│ (generated.log)│
└───────┬───────┘
        │
        ▼
┌────────────────────┐
│ Read file line by  │
│ line               │
└───────┬────────────┘
        │
        ▼
┌────────────────────┐
│ Tokenize log entry │
│ into parts         │
└───────┬────────────┘
        │
        ▼
┌──────────────────────────┐
│ Extract fields           │
│ - latency                │
│ - INFO / WARN / ERROR    │
└───────┬──────────────────┘
        │
        ▼
┌──────────────────────────┐
│ Aggregate metrics        │
│ - latency list           │
│ - event counters         │
└───────┬──────────────────┘
        │
        ▼
┌──────────────────────────┐
│ Statistical analysis     │
│ - mean & median latency  │
│ - anomaly threshold      │
│ - slowest N requests     │
└───────┬──────────────────┘
        │
        ▼
┌──────────────────────────┐
│ Console summary output   │
└──────────────────────────┘
