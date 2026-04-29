from abc import ABC, abstractmethod


class OutputStrategy(ABC):
    @abstractmethod
    def output(self, rows):
        pass