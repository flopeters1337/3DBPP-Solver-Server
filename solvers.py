
from abc import ABC, abstractmethod


class AbstractSolver(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def solve(self, crates_list):
        return None


class DummySolver(AbstractSolver):
    def __init__(self):
        pass    # TODO

    def solve(self, crates_list):
        pass    # TODO


class SimpleSolver(AbstractSolver):
    def __init__(self):
        pass    # TODO

    def solve(self, crates_list):
        pass    # TODO
