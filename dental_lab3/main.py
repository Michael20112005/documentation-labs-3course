from sqlalchemy import create_engine
from data.models import Base
from data.repository import PatientRepository
from data.csv_reader import CSVReader
from business.patient_service import PatientService

engine = create_engine("sqlite:///db.sqlite")
Base.metadata.create_all(engine)

repo = PatientRepository(engine)
reader = CSVReader()
service = PatientService(repo, reader)

service.load_from_csv("data.csv")

print("DONE: Data loaded into DB")