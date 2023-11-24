# KI pysec2023

These excersices are part of the course pysec2023 at KI. 
Code is written in Python 3.9.0 and Python 3.10.11
Used text editor is VS Code.
Used shell is bash.
OS is Windows 11.

All the tasks descriptions can be found in Task_tracker.txt

### Setup environment:

1. Download and install version 3.10.* and 3.9.0 from python.org
2. Create virtual environments for each version:
    - `python -m venv .venv10`
    - `python -m venv .venv9`
NOTE: I used path alias to switch between versions.
set alias: alias python9='<path_to_python>'/python.exe'
Then check version with: python9 --version
3. Activate the environments:   
    - `source .venv10/bin/activate`
    - `source .venv9/bin/activate`
4. Install packages:
    - `pip install -r requirements.txt`
5. Run the needed code by typing in console:
    - `python directory_tree,py`
    and follow the instructions for each application.