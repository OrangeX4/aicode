import importlib
import argparse
import yaml
import time
import shutil
from scripts.branch import current_branch, checkout

parser = argparse.ArgumentParser()
parser.add_argument('--task', default=None)
parser.add_argument('--debug', default=None)
args = parser.parse_args()

current_task_name = current_branch.name if current_branch.name != 'dev' else 'main'

if args.task is None and args.debug is None:
    checkout(current_task_name)
    importlib.import_module(f'tasks.{current_task_name}.main')
else:
    # read yaml file from ./tasks/current_task_name/task.yaml
    with open(f'./tasks/{current_task_name}/task.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        # task-version-2023-12-04-22-22-default
        new_task_name = (
            (
                f'{"task" if args.task is not None else "debug"}-v{config["VERSION"]}-{time.strftime("%Y-%m-%d-%H-%M", time.localtime())}-{args.task}'
            )
            .replace('-', '_')
            .replace('.', '_')
        )
        # copy ./tasks/current_task_name to ./tasks/new_task_name
        shutil.copytree(f'./tasks/{current_task_name}', f'./tasks/{new_task_name}')
        # checkout new task
        checkout(new_task_name)
