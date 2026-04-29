from flask import Blueprint, render_template, request, redirect
from sqlalchemy import create_engine

from data.repository import PatientRepository
from data.csv_reader import CSVReader
from business.patient_service import PatientService

patient_bp = Blueprint("patients", __name__)

engine = create_engine("sqlite:///db.sqlite")

repo = PatientRepository(engine)
reader = CSVReader()
service = PatientService(repo, reader)


@patient_bp.route("/")
def index():
    patients = service.get_all_patients()
    return render_template("index.html", patients=patients)


@patient_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        birth_date = request.form["birth_date"]

        service.add_patient(name, phone, birth_date)
        return redirect("/")

    return render_template("create.html")


@patient_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    patient = service.get_patient_by_id(id)

    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        birth_date = request.form["birth_date"]

        service.update_patient(id, name, phone, birth_date)
        return redirect("/")

    return render_template("edit.html", patient=patient)


@patient_bp.route("/delete/<int:id>")
def delete(id):
    service.delete_patient(id)
    return redirect("/")