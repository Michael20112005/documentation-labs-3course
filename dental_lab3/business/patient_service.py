from data.models import Patient


class PatientService:
    def __init__(self, repo, reader):
        self.repo = repo
        self.reader = reader

    def load_from_csv(self, path):
        rows = self.reader.read(path)

        for row in rows:
            existing_patient = self.repo.find_by_data(
                row["name"],
                row["phone"],
                row["birth_date"]
            )

            if existing_patient is None:
                patient = Patient(
                    name=row["name"],
                    phone=row["phone"],
                    birth_date=row["birth_date"]
                )
                self.repo.save(patient)

    def get_all_patients(self):
        return self.repo.get_all()

    def get_patient_by_id(self, patient_id):
        return self.repo.get_by_id(patient_id)

    def add_patient(self, name, phone, birth_date):
        existing_patient = self.repo.find_by_data(name, phone, birth_date)

        if existing_patient is None:
            patient = Patient(
                name=name,
                phone=phone,
                birth_date=birth_date
            )
            self.repo.save(patient)

    def update_patient(self, patient_id, name, phone, birth_date):
        patient = self.repo.get_by_id(patient_id)

        if patient is not None:
            patient.name = name
            patient.phone = phone
            patient.birth_date = birth_date
            self.repo.update()

    def delete_patient(self, patient_id):
        patient = self.repo.get_by_id(patient_id)

        if patient is not None:
            self.repo.delete(patient)