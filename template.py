import os
import logging
from pathlib import Path 

logging.basicConfig(
    level=logging.INFO,
    format = "[%(asctime)s: %(levelname)s]: %(message)s"
)
while True:
    project_name = input("Enter project name: ").strip()
    if project_name != "":
        break

logging.info(f"Creating the project with name: {project_name}")

list_of_files = [
    ".github/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/templates/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    "configs/config.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    file_dir, filename = os.path.split(Path(filepath))
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"directory {file_dir} created for file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"created new file {filename} at {filepath}")
    else:
        logging.info(f"{filename} exists with current size: {os.path.getsize(filepath)}")