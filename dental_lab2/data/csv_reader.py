from abc import ABC, abstractmethod
import csv


class ICSVReader(ABC):
    @abstractmethod
    def read(self, path):
        pass


class CSVReader(ICSVReader):
    def read(self, path):
        with open(path, newline='', encoding="utf-8") as f:
            return list(csv.DictReader(f))