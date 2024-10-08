# LiveTimer
A Python module to log multiple points in a repeating operation to get live statistics.

## Upfront Performance Notice
This module was not designed with per-cycle performance in mind. It was designed to time IO-bound operations with 
millisecond precision, and has not been benchmarked or optimized for highly performant applications. You are welcome
to submit pull requests that would improve performance.

## Usage
This example can be found in `demo.py`.
```python
>> with RichTimer().start as timer:
>>     for _ in range(100):
>>         with timer.cycle as cycle:
>>             time.sleep(randint(1, 8) * 0.001)
>>             cycle.log("Logpoint: 10-80ms")
>>             time.sleep(randint(1, 2) * 0.001)
>>             cycle.log("Logpoint: 10-20ms")
>>             time.sleep(0.1)
>>             cycle.log("Logpoint: 100ms")
```

Output:
```
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃ Metric              ┃ Total ┃ Avg      ┃ Min      ┃ Max      ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│ Count               │ 100   │          │          │          │
│ Time per Iteration  │       │ 0.107448 │ 0.102287 │ 0.113916 │
│ - Logpoint: 10-80ms │       │ 0.004728 │ 0.001104 │ 0.010578 │
│ - Logpoint: 10-20ms │       │ 0.001943 │ 0.001042 │ 0.003702 │
│ - Logpoint: 100ms   │       │ 0.100768 │ 0.100067 │ 0.109139 │
└─────────────────────┴───────┴──────────┴──────────┴──────────┘
```