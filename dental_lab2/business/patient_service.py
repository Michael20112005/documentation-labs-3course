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