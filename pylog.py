import logging
import subprocess
import sys
import psutil
from datetime import datetime
from typing import Optional

# Configure logging
def configure_logging(log_level: int = logging.DEBUG, log_file: str = 'debug.log') -> None:
    logging.basicConfig(filename=log_file, level=log_level, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

# Function to execute a script and capture its output
def execute_script(script_path: str) -> Optional[subprocess.CompletedProcess]:
    try:
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        result.check_returncode()
        return result
    except subprocess.CalledProcessError as e:
        log_error(e)
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return None

# Function to log errors
def log_error(e: subprocess.CalledProcessError) -> None:
    logging.error(f"Command that failed: {e.cmd}")
    logging.error(f"Exit code: {e.returncode}")
    logging.error(f"Standard Output: {e.stdout}")
    logging.error(f"Standard Error: {e.stderr}")

# Function to log resource usage
def log_resource_usage() -> None:
    process = psutil.Process()
    cpu_time = process.cpu_times().user + process.cpu_times().system
    memory_usage = process.memory_info().rss / 1024 / 1024  # in MB
    logging.info(f"CPU time: {cpu_time:.2f} seconds")
    logging.info(f"Memory usage: {memory_usage:.2f} MB")

# Function to monitor script execution and log resource usage
def run_script(script_path: str, log_level: int = logging.DEBUG, log_file: str = 'debug.log') -> None:
    configure_logging(log_level, log_file)
    logging.info(f"Starting script: {script_path} at {datetime.now()}")

    result = execute_script(script_path)

    if result:
        logging.info(f"Script executed successfully: {result.stdout}")
    else:
        logging.error("Script execution failed.")

    log_resource_usage()
    logging.info(f"Finished script: {script_path} at {datetime.now()}")

# Example of how this might be used in a game loop or main function
def main():
    # Run the game loop, periodically log resource usage
    run_script('your_script.py')

# Call the main function if this script is executed directly
if __name__ == '__main__':
    main()
