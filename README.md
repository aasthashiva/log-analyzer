# SYSTEM-LOG-ANALYZER

A Python program that reads system log files and summarizes latency behavior and event types.

## Overview

System logs contain detailed records of what a system did over time.  
Reading them line by line is inefficient, especially when the file is large.

This project extracts a small set of useful summaries from raw log data in order to understand overall system behavior.

## What the program does

- Reads log entries from a text file  
- Identifies INFO, WARN, and ERROR events  
- Extracts latency values from each entry  
- Aggregates latency data across all requests  
- Computes average latency and a statistical threshold  
- Flags unusually slow requests  
- Reports the slowest observed latencies  

The program summarizes behavior. It does not attempt to explain causes.

## Log format

Each log entry must follow this format:
```text
YYYY-MM-DD HH:MM:SS <LEVEL> latency=<value>
Example:
2024-12-21 10:00:31 ERROR latency=980

How it works

The log file is read line by line

Each line is split into components

Event type and latency are extracted

Latency values are collected for analysis

Anomalies are detected using a mean + 3σ threshold

All computation is done locally using the Python standard library.

Project structure
log-analyzer/
├── analyzer.py   # log parsing and aggregation logic
├── stats.py      # statistical analysis helpers
├── sample.log    # example input log file
└── README.md

Requirements

Python 3.x

No external libraries

Usage

Run the analyzer from the project directory:

python analyzer.py


The program reads the log file and prints a summary to standard output.
