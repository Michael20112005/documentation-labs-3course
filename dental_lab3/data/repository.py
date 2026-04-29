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

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, patient_id):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self, patient):
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

    def get_all(self):
        return self.session.query(Patient).all()

    def get_by_id(self, patient_id):
        return self.session.query(Patient).filter_by(id=patient_id).first()

    def update(self):
        self.session.commit()

    def delete(self, patient):
        self.session.delete(patient)
        self.session.commit()