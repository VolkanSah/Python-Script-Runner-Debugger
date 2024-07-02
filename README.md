# Python Script Runner & Debugger

This Python script is designed to run other Python scripts, logging both errors and resource usage. It was developed during a collaborative debugging session with OpenAI's ChatGPT and my new ChatGPT4 Plugin [ChatGPT-ShellMaster](https://github.com/VolkanSah/ChatGPT-ShellMaster). The initial goal was to troubleshoot a Python-based GUI application. The tool proved so useful that we decided to package it and share it with the wider community.

## Features
- Executes Python scripts and captures error output.
- Logs the command that failed, exit code, standard output, and standard error if a script fails.
- Logs CPU time (user + system) and memory usage.

## Usage
1. **Install Requirements**: No additional packages are needed as `subprocess`, `resource`, and `logging` are part of the Python Standard Library.
2. **Replace Script Path**: Replace `'your_script.py'` in the line `python_script = 'your_script.py'` with the path to the Python script you want to run.
3. **Run the Script**:
    ```shell
    python3 pylog.py
    ```

## Background
This script emerged from a collaborative debugging session with ChatGPT, an AI developed by OpenAI. The initial goal was to resolve syntax errors in a Python-based GUI for managing various tasks. As we worked through the issue, we realized that a tool for running Python scripts while logging errors and resource usage could be incredibly beneficial to many developers.

Thus, ChatGPT and I decided to develop this script runner and debugger and share it with the broader community. We sincerely hope this tool will help other developers save time and avoid headaches while debugging their Python scripts.

## Note
Credit for Version 1 of this tool goes to ChatGPT-4 from OpenAI for its invaluable assistance in finding solutions.
Credits for Version 2 of this tool goes to **VolkanSah**
