import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import logging
import subprocess
import sys
import psutil
from datetime import datetime

class ScriptRunner:
    def __init__(self, log_file='debug.log'):
        self.log_file = log_file
        self.configure_logging()

    def configure_logging(self, log_level=logging.DEBUG):
        logging.basicConfig(filename=self.log_file, level=log_level,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def execute_script(self, script_path):
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
    def log_error(e):
        logging.error(f"Command that failed: {e.cmd}")
        logging.error(f"Exit code: {e.returncode}")
        logging.error(f"Standard Output: {e.stdout}")
        logging.error(f"Standard Error: {e.stderr}")

    @staticmethod
    def log_resource_usage():
        process = psutil.Process()
        cpu_time = process.cpu_times().user + process.cpu_times().system
        memory_usage = process.memory_info().rss / 1024 / 1024  # in MB
        logging.info(f"CPU time: {cpu_time:.2f} seconds")
        logging.info(f"Memory usage: {memory_usage:.2f} MB")

    def run_script(self, script_path):
        logging.info(f"Starting script: {script_path} at {datetime.now()}")
        result = self.execute_script(script_path)
        if result:
            logging.info(f"Script executed successfully: {result.stdout}")
        else:
            logging.error("Script execution failed.")
        self.log_resource_usage()
        logging.info(f"Finished script: {script_path} at {datetime.now()}")
        return result

class AdvancedDebugTool:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Debug Tool")
        self.master.geometry("800x600")
        
        self.script_runner = ScriptRunner()
        self.script_path = tk.StringVar()
        
        self.create_menu()
        self.create_notebook()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load Script", command=self.load_script)
        file_menu.add_command(label="Exit", command=self.master.quit)

        run_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Run", menu=run_menu)
        run_menu.add_command(label="Start Script", command=self.run_script)
        run_menu.add_command(label="Start Observer", command=self.start_observer)

        settings_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Settings", menu=settings_menu)
        settings_menu.add_command(label="Preferences", command=self.show_preferences)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_notebook(self):
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        self.main_frame = ttk.Frame(self.notebook)
        self.observer_frame = ttk.Frame(self.notebook)
        self.settings_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.main_frame, text="Main")
        self.notebook.add(self.observer_frame, text="Observer")
        self.notebook.add(self.settings_frame, text="Settings")

        self.create_main_frame()
        self.create_observer_frame()
        self.create_settings_frame()

    def create_main_frame(self):
        ttk.Label(self.main_frame, text="Script Path:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        ttk.Entry(self.main_frame, textvariable=self.script_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.main_frame, text="Browse", command=self.load_script).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(self.main_frame, text="Run Script", command=self.run_script).grid(row=1, column=1, padx=5, pady=5)

        self.output_text = tk.Text(self.main_frame, wrap='word', height=20)
        self.output_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)

    def create_observer_frame(self):
        self.observer_text = tk.Text(self.observer_frame, wrap='word', state='disabled')
        self.observer_text.pack(expand=True, fill='both', padx=5, pady=5)

    def create_settings_frame(self):
        ttk.Label(self.settings_frame, text="Log File:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        ttk.Entry(self.settings_frame, textvariable=tk.StringVar(value=self.script_runner.log_file), width=50).grid(row=0, column=1, padx=5, pady=5)
        # Add more settings as needed

    def load_script(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            self.script_path.set(file_path)

    def run_script(self):
        if not self.script_path.get():
            messagebox.showerror("Error", "Please select a script first.")
            return
        result = self.script_runner.run_script(self.script_path.get())
        if result:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, result.stdout)
        self.start_observer()  # Automatically start the observer after running the script

    def start_observer(self):
        self.notebook.select(self.observer_frame)
        self.update_observer()

    def update_observer(self):
        self.observer_text.configure(state='normal')
        with open(self.script_runner.log_file, 'r') as f:
            self.observer_text.delete(1.0, tk.END)
            self.observer_text.insert(tk.END, f.read())
        self.observer_text.configure(state='disabled')
        self.master.after(1000, self.update_observer)

    def show_preferences(self):
        # Implement preferences dialog
        pass

    def show_about(self):
        messagebox.showinfo("About", "Advanced Debug Tool\nVersion 1.0\n\nCreated by Your Name")

def main():
    root = tk.Tk()
    AdvancedDebugTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
