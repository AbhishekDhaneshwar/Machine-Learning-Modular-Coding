import os, sys
from pathlib import Path
import logging 

while True:
    project_name=input("Enter the name of your project")
    if project_name != "":
        break

#src/__init__.py
#src/components/__init__.py
    
list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exceptions/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exceptions.py",
    "setup.py" 
]


for file_pth in list_of_files:
    filepath= Path(file_pth)
    filedir, filename= os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass

    else:
        logging.info("File is already present at : {filepath}")


    



















