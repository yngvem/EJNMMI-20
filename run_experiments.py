import subprocess
from pathlib import Path

EX_RECIPE_FOLDER = Path('experiment_folders/unet_new_data')
EX_FOLDER = Path('experiments')


for ex in EX_RECIPE_FOLDER.iterdir():
    print(ex)
    subprocess.run(["python", "create_experiments.py", f"{ex}", "unet", "--experimentdir", f"{EX_FOLDER}"])

for ex in EX_FOLDER.iterdir():
    print(f'Running experiment: {ex}')
    subprocess.run(["python", "run_experiment.py", f"{ex}", "10000", "--eval", "dice"])
