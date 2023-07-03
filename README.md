# Python Script Runner & Debugger
This Python script is designed to run other Python scripts, logging both errors and resource usage. It was developed during a collaborative debugging session with OpenAI's ChatGPT and my new ChatGPT4 Plugin [ChatGPT-ShellMaster](https://github.com/VolkanSah/ChatGPT-ShellMaster). The goal was to troubleshoot a Python-based GUI application. The tool proved to be so useful, that we decided to package it up and share it with the wider community. We hope this tool can be of use to other developers out there, saving them some time and headaches when debugging their Python scripts.

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
This script emerged from a collaborative debugging session with an AI developed by OpenAI, known as ChatGPT. The initial goal was to help resolve syntax errors that were occurring in a Python-based GUI for managing stuff/ rules. As we delved into the issue, we recognized that a tool for running Python scripts and simultaneously logging both errors and resource usage could be tremendously beneficial to many developers. So we didn`t stop to think and create this simple script for you all 😄 

Thus, ChatGPT and I decided to develop this script runner and debugger, and share it with the broader community. We sincerely hope that this tool will assist other developers in saving time and avoiding headaches while debugging their Python scripts.

## Note 
It is cool, ChatGPT want find solutions for you, so the credits goes to ChatGPT4 from OpenAI not to me 💝
