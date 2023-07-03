# Python Script Runner & Debugger
This Python script is designed to run other Python scripts, logging both errors and resource usage. It was developed as a convenient tool while debugging a Python-based GUI for managing UFW (Uncomplicated Firewall) rules.

## Features
- Runs Python scripts and captures any error output
- Logs the command that failed, exit code, standard output, and standard error if a script fails
- Logs CPU time (user + system) and memory usage
## Usage
- Install the required Python packages: subprocess and resource are part of the Python Standard Library, and logging is used for logging errors and resource usage.
- Replace 'your_script.py' in the line python_script = 'your_script.py' with the path to the Python script you want to run.

Run this script: 
```shell
python3 pylog.py
```
## Background
This script emerged from a collaborative debugging session with an AI developed by OpenAI, known as ChatGPT. The initial goal was to help resolve syntax errors that were occurring in a Python-based GUI for managing UFW (Uncomplicated Firewall) rules. As we delved into the issue, we recognized that a tool for running Python scripts and simultaneously logging both errors and resource usage could be tremendously beneficial to many developers.

Thus, ChatGPT and I decided to develop this script runner and debugger, and share it with the broader community. We sincerely hope that this tool will assist other developers in saving time and avoiding headaches while debugging their Python scripts.

## Note 
It is cool, ChatGPT want find solutions for you, so the credits goes to ChatGPT4from OpenAI!
