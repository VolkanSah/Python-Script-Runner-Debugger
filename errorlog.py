import logging
import subprocess

# Configure logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

# Your Python script to execute
python_script = 'your_script.py'

try:
    # Run your script
    subprocess.check_output(['python3', python_script])
except subprocess.CalledProcessError as e:
    # If there is an error, log the error and the output
    logging.error(f"Execution failed: {e}")
    logging.error(f"Output: {e.output.decode('utf-8')}")
