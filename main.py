import importlib
from scripts.branch import current_branch, checkout

# importlib.import_module(f'tasks.{current_branch.name}.main')

checkout('main')
