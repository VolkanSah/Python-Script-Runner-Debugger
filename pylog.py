import logging
import subprocess
import sys
import psutil
import tkinter as tk
from datetime import datetime
from typing import Optional

class ScriptRunner:
    def __init__(self, log_file: str = 'debug.log'):
        self.log_file = log_file
        self.configure_logging()

    def configure_logging(self, log_level: int = logging.DEBUG) -> None:
        logging.basicConfig(
            filename=self.log_file,
            level=log_level,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def execute_script(self, script_path: str) -> Optional[subprocess.CompletedProcess]:
        try:
            result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
            result.check_returncode()
            return result
        except subprocess.CalledProcessError as e:
            self.log_error(e)
            return None
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            return None

    @staticmethod
    def log_error(e: subprocess.CalledProcessError) -> None:
        logging.error(f"Command that failed: {e.cmd}")
        logging.error(f"Exit code: {e.returncode}")
        logging.error(f"Standard Output: {e.stdout}")
        logging.error(f"Standard Error: {e.stderr}")

    @staticmethod
    def log_resource_usage() -> None:
        process = psutil.Process()
        cpu_time = process.cpu_times().user + process.cpu_times().system
        memory_usage = process.memory_info().rss / 1024 / 1024  # in MB
        logging.info(f"CPU time: {cpu_time:.2f} seconds")
        logging.info(f"Memory usage: {memory_usage:.2f} MB")

    def run_script(self, script_path: str) -> None:
        logging.info(f"Starting script: {script_path} at {datetime.now()}")
        result = self.execute_script(script_path)
        if result:
            logging.info(f"Script executed successfully: {result.stdout}")
        else:
            logging.error("Script execution failed.")
        self.log_resource_usage()
        logging.info(f"Finished script: {script_path} at {datetime.now()}")

class DebugTool:
    def __init__(self, master):
        self.master = master
        self.master.title("Debug Tool")
        self.master.geometry("300x200")
        self.script_runner = ScriptRunner()

        self.start_button = tk.Button(self.master, text="Start Script", command=self.run_script)
        self.start_button.pack(pady=20)

        self.observer_button = tk.Button(self.master, text="Open Observer", command=self.open_observer_window)
        self.observer_button.pack(pady=20)

    def run_script(self):
        self.script_runner.run_script('gui2.py')

    def open_observer_window(self):
        observer_window = tk.Toplevel(self.master)
        observer_window.title("Observer Window")
        observer_window.geometry("600x400")
        log_display = tk.Text(observer_window, wrap='word', state='disabled')
        log_display.pack(expand=True, fill='both')

        def update_log_display():
            log_display.configure(state='normal')
            with open('debug.log', 'r') as f:
                log_display.delete(1.0, tk.END)
                log_display.insert(tk.END, f.read())
            log_display.configure(state='disabled')
            observer_window.after(1000, update_log_display)

        update_log_display()

def main():
    root = tk.Tk()
    DebugTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
