import psutil
import logging

# Configure logging
logging.basicConfig(
    filename='system_health.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define threshold values
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 90  # in percentage


def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        message = f'High CPU usage detected: {cpu_usage}%'
        print(message)
        logging.warning(message)

def check_memory():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        message = f'High Memory usage detected: {memory_usage}%'
        print(message)
        logging.warning(message)

def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        message = f'Low Disk space detected: {disk_usage}% used'
        print(message)
        logging.warning(message)

def check_running_processes():
    process_count = len(psutil.pids())
    message = f'Number of running processes: {process_count}'
    print(message)
    logging.info(message)

def monitor_system():
    check_cpu()
    check_memory()
    check_disk()
    check_running_processes()

if __name__ == "__main__":
    monitor_system()
