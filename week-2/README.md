# Week 2 — CPU process scheduling

Implements **FCFS**, **SJF**, **PS** (priority scheduling), and **RR** (round-robin, time quantum = 4). Outputs per-process waiting time and turnaround time, plus average waiting time and average turnaround time.

## Files

| File                         | Description |
|------------------------------|-------------|
| `process_scheduling_main.py` | Full implementation of all four algorithms with a fixed 4-process example; prints comparison (which algorithm gives lowest average waiting time and lowest average turnaround time). **Recommended to run.** |
| `process_scheduling_alt.py`  | Same four algorithms with a different 4-process example (longer burst times). |
| `processScheduling.py`       | Interactive: prompts for number of processes and each process's arrival time, burst time, and priority. Implements FCFS fully; SJF/PS are partially implemented or commented out. |

## Run

```bash
python process_scheduling_main.py
# or
python process_scheduling_alt.py
# or (interactive FCFS)
python processScheduling.py
```

## Tech stack

- **Python 3**
- **Standard library:** `collections.deque` (for round-robin queue)
