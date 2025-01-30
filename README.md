# Cpu-usage
# System Health Monitoring Script

## Overview
This Python script monitors system health by checking CPU usage, memory usage, disk space, and the number of running processes. It logs warnings when resource usage exceeds predefined thresholds.

## Features
- Monitors CPU, memory, and disk usage.
- Logs warnings when thresholds are exceeded.
- Displays the number of running processes.
- Saves logs in `system_health.log`.

## Prerequisites
Ensure you have Python installed (version 3.x recommended) and install the required package:

```bash
pip install psutil
```

## Installation
1. Download or clone the script.
2. Install dependencies using `pip install psutil`.
3. Run the script with:
   ```bash
   python system_health.py
   ```

## Configuration
Modify the threshold values in the script as needed:
```python
CPU_THRESHOLD = 80  # CPU usage percentage
MEMORY_THRESHOLD = 80  # Memory usage percentage
DISK_THRESHOLD = 90  # Disk usage percentage
```

## Logging
Logs are saved in `system_health.log`. Warnings are recorded when thresholds are exceeded.

## Enhancements
Future improvements could include:
- Continuous monitoring with scheduled intervals.
- Email or notification alerts for critical issues.
- More detailed process monitoring.

## License
This script is free to use and modify.

## Author
GEMBALI KEERTHIVARDHAN


