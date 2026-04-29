import csv


class CSVReader:
    def __init__(self, file_path, limit=None):
        self.file_path = file_path
        self.limit = limit

    def read(self):
        rows = []

        with open(self.file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for index, row in enumerate(reader):
                if self.limit is not None and index >= self.limit:
                    break

                rows.append(row)

        return rows