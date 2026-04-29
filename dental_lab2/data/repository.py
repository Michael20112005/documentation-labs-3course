from abc import ABC, abstractmethod
from sqlalchemy.orm import sessionmaker
from data.models import Patient


class IPatientRepository(ABC):
    @abstractmethod
    def save(self, patient):
        pass

    @abstractmethod
    def find_by_data(self, name, phone, birth_date):
        pass


class PatientRepository(IPatientRepository):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def save(self, patient):
        self.session.add(patient)
        self.session.commit()

    def find_by_data(self, name, phone, birth_date):
        return self.session.query(Patient).filter_by(
            name=name,
            phone=phone,
            birth_date=birth_date
        ).first()