import importlib
from scripts.checkout import current_branch

importlib.import_module('tasks.main.' + current_branch)