import logging
import subprocess
import resource
from datetime import datetime
from typing import Optional

# Configure logging
def configure_logging(log_level: int = logging.DEBUG) -> None:
    logging.basicConfig(filename='debug.log', level=log_level)

# Function to execute a script
def execute_script(script_path: str) -> Optional[subprocess.CompletedProcess]:
    try:
        result = subprocess.run(['python3', script_path], capture_output=True, text=True)
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
    usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu_time = usage.ru_utime + usage.ru_stime
    memory_usage = usage.ru_maxrss / 1024
    logging.info(f"CPU time: {cpu_time} seconds")
    logging.info(f"Memory usage: {memory_usage} MB")

# Function to run the script and log resource usage
def run_script(script_path: str, log_level: int = logging.DEBUG) -> None:
    configure_logging(log_level)
    logging.info(f"Starting script: {script_path} at {datetime.now()}")

    result = execute_script(script_path)

    if result:
        logging.info(f"Script executed successfully: {result.stdout}")
    else:
        logging.error("Script execution failed.")

    log_resource_usage()
    logging.info(f"Finished script: {script_path} at {datetime.now()}")

# Your Python script to execute
python_script = 'your_script.py'

# Call the function
run_script(python_script)

# Unit Tests
import unittest
from unittest.mock import patch, MagicMock

class TestScriptExecution(unittest.TestCase):

    @patch('subprocess.run')
    def test_execute_script_success(self, mock_run):
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = 'Success'
        mock_run.return_value = mock_result

        result = execute_script('dummy_script.py')
        self.assertIsNotNone(result)
        self.assertEqual(result.stdout, 'Success')

    @patch('subprocess.run')
    def test_execute_script_failure(self, mock_run):
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stdout = 'Failure'
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd='dummy_script.py', output='Failure', stderr='Error')

        result = execute_script('dummy_script.py')
        self.assertIsNone(result)

    @patch('resource.getrusage')
    def test_log_resource_usage(self, mock_getrusage):
        mock_usage = MagicMock()
        mock_usage.ru_utime = 1.0
        mock_usage.ru_stime = 0.5
        mock_usage.ru_maxrss = 1024
        mock_getrusage.return_value = mock_usage

        with patch('logging.info') as mock_logging_info:
            log_resource_usage()
            mock_logging_info.assert_any_call('CPU time: 1.5 seconds')
            mock_logging_info.assert_any_call('Memory usage: 1.0 MB')

if __name__ == '__main__':
    unittest.main()
