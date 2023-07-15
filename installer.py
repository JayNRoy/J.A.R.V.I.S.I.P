import os
import sys
import urllib

""" An installer file that ensures all required modules for the program are installed.
    It also installs all missing modules so that the program can run."""

requiredModules = [
    "json",
    "random",
    "pickle",
    "os",
    "numpy",
    "sys",
    "pyttsx3",
    "speechrecognition",
    "urllib"
]

# First ensure pip is installed on the machine.
try:
    import pip
    print("pip found.")
except ModuleNotFoundError:
    # if pip is not installed, download get-pip.py
    url = "https://bootstrap.pypa.io/get-pip.py"
    urllib.request.urlretrieve(url, "get-pip.py")
    
   # run get-pip.py using os.system()
    os.system(f"{sys.executable} get-pip.py")
    
    
# Start installing any modules that are missing.
for module in requiredModules:
    select = module
    try:
        import select
    except ImportError:
        print(f"{select} module not found. Installing {select}.")
        os.system(f"pip3.10 install {select}")