import sys
import os
from cx_Freeze import setup, Executable

# What will be included in the .exe
files = [
    "credentials.csv"
]
# Includes
configurations = Executable(
        script="main.py",
    )

# Congurations
setup(
    name="Social Media Automation",
    version="1.0",
    description="Automating Social Media content creation and posting",
    author="Raphael Rodrigues",
    options={"build_exe":{
        "include_files": files,
                "packages": [
            "selenium", 
            "webdriver_manager", 
            "pyautogui", 
            "time", 
            "random", 
            "csv",
            "os", ],
        "include_msvcr": True 
        }},
    executables=[configurations]
)