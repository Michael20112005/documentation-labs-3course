import csv
import random

names = ["Ivan", "Petro", "Oleg", "Anna", "Maria", "Olha", "Nazar", "Iryna"]

phones = [
    "0971112233",
    "0502223344",
    "0633334455",
    "0664445566",
    "0685556677",
    "0936667788"
]

birth_dates = [
    "1990-01-15",
    "1995-03-22",
    "1988-07-10",
    "2000-11-05",
    "1993-09-18",
    "1985-12-30"
]

with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "phone", "birth_date"])

    for _ in range(1000):
        writer.writerow([
            random.choice(names),
            random.choice(phones),
            random.choice(birth_dates)
        ])