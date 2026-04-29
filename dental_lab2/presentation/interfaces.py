from abc import ABC, abstractmethod


class IPatientPresentation(ABC):
    @abstractmethod
    def show_message(self, message: str):
        pass