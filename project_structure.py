import os
from pathlib import Path

list_of_files =[
    f"src/data/data_ingestion.py",
    f"src/data/data_preprocessing.py",
    f"src/model/model_building.py",
    f"src/model/model_evaluation.py",
    f"src/model/register_model.py",
    f"src/__init__.py",
    f"flask_api/main.py",
    f"yt_chorome_plugin/manifest.json",
    f"yt_chorome_plugin/popup.html",
    f"yt_chorome_plugin/popup.js"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    print(filedir, filename)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if not os.path.exists(filepath) or os.path.getsizer == 0:
        with open(filepath, "w") as f:
            pass
        print("File has been created")
    else:
        print("File already exists")