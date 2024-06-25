
from .tasks import _TASKS
from .datasets import _DATASETS, _META

class SinglePredTasks:
    def __init__(self):
        self.tasks = _TASKS
        self.datasets = _DATASETS
        self.meta = _META
        