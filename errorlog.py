import logging
import subprocess
import resource

# Configure logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

# Function to execute a script and log resource usage
def run_script(script_path):
    try:
        # Run the script
        result = subprocess.run(['python3', script_path], capture_output=True, text=True)
        result.check_returncode()
    except subprocess.CalledProcessError as e:
        # If there is an error, log the error and the output
        logging.error(f"Command that failed: {e.cmd}")
        logging.error(f"Exit code: {e.returncode}")
        logging.error(f"Standard Output: {e.stdout}")
        logging.error(f"Standard Error: {e.stderr}")

    # Get resource usage
    usage = resource.getrusage(resource.RUSAGE_CHILDREN)

    # Log CPU time (user + system)
    cpu_time = usage.ru_utime + usage.ru_stime
    logging.info(f"CPU time: {cpu_time} seconds")

    # Log memory usage (convert from kilobytes to megabytes)
    memory_usage = usage.ru_maxrss / 1024
    logging.info(f"Memory usage: {memory_usage} MB")

# Your Python script to execute
python_script = 'your_script.py'

# Call the function
run_script(python_script)

