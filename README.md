# KI pysec2023

These excersices are part of the course pysec2023 at KI. 
Code is written in Python 3.9.0 and Python 3.11.2
Used text editor is VS Code.
Used shell is bash.
OS is Windows 11.

### Setup environment:

1. Download and install version 3.11.* and 3.9.0 from python.org
2. Create virtual environments for each version:
    - `python -m venv .venv11`
    - `python -m venv .venv9`
NOTE: I used path alias to switch between versions.
set alias: alias python9='<path_to_python>'/python.exe'
Then check version with: python9 --version
3. Activate the environments:   
    - `source .venv11/bin/activate`
    - `source .venv9/bin/activate`
4. Install packages:
    - `pip install -r requirements.txt`
5. Run the code:
    - `python main.py`