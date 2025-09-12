import os
from pathlib import Path

project_name = "us_visa" # like a component where all file and directories will be

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluaiton.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.py",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml"
]


for filepath in list_of_files:
    # create windows path to aviod error
    filepath = Path(filepath)

    # separate directories form files
    filedir, filename = os.path.split(filepath)
    
    # create directory if not empty string
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # create files paths
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open(filepath, "w") as f:
            pass

    else:
        print(f"File is already present at: {filepath}")