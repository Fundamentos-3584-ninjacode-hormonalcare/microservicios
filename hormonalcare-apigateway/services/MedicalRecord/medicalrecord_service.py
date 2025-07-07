from fastapi import APIRouter, Request, HTTPException, File, UploadFile, Form, Path
from fastapi.responses import JSONResponse
import requests
from configs.url_services import MICROSERVICE_MEDICAL_RECORD

medical_record_router = APIRouter()

# =============== MEDICAL RECORDS ===============


@medical_record_router.get("/medical-records")
async def get_all_medical_records(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medicalRecords"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/medical-records/{medicalRecordId}")
async def get_medical_record_by_id(request: Request, medicalRecordId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medicalRecords/{medicalRecordId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.post("/medical-records")
async def create_medical_record(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medicalRecords"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.post(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})

# =============== DOCTORS ===============


@medical_record_router.get("/doctors")
async def get_all_doctors(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/doctor/doctor"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/doctors/{doctorId}")
async def get_doctor_by_id(request: Request, doctorId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/doctor/doctor/{doctorId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/doctors/profile/{profileId}")
async def get_doctor_by_profile_id(request: Request, profileId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/doctor/doctor/profile/{profileId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.post("/doctors")
async def create_doctor(request: Request,
                        firstName: str = Form(...),
                        lastName: str = Form(...),
                        gender: str = Form(...),
                        phoneNumber: str = Form(...),
                        birthday: str = Form(...),
                        userId: int = Form(...),
                        medicalLicenseNumber: str = Form(...),
                        yearsOfExperience: int = Form(...),
                        specialization: str = Form(...),
                        professionalIdentificationNumber: int = Form(...),
                        subSpecialty: str = Form(...),
                        file: UploadFile = File(None)
                        ):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/doctor/doctor"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]

    data = {
        "firstName": firstName,
        "lastName": lastName,
        "gender": gender,
        "phoneNumber": phoneNumber,
        "birthday": birthday,
        "userId": str(userId),
        "medicalLicenseNumber": medicalLicenseNumber,
        "yearsOfExperience": str(yearsOfExperience),
        "specialization": specialization,
        "professionalIdentificationNumber": str(professionalIdentificationNumber),
        "subSpecialty": subSpecialty
    }

    files = None
    if file is not None:
        files = {"file": (file.filename, await file.read(), file.content_type)}

    try:
        response = requests.post(url, headers=headers, data=data, files=files)
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})

# =============== PATIENTS ===============


@medical_record_router.get("/patients")
async def get_all_patients(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/patient"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/patients/{patientId}")
async def get_patient_by_id(request: Request, patientId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/patient/{patientId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/patients/profile/{profileId}")
async def get_patient_by_profile_id(request: Request, profileId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/patient/profile/{profileId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/patients/doctor/{doctorId}")
async def get_patients_by_doctor_id(request: Request, doctorId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/patient/doctor/{doctorId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.post("/patients")
async def create_patient(request: Request,
                         firstName: str = Form(...),
                         lastName: str = Form(...),
                         gender: str = Form(...),
                         phoneNumber: str = Form(...),
                         birthday: str = Form(...),
                         userId: int = Form(...),
                         typeOfBlood: str = Form(...),
                         emergencyContactName: str = Form(...),
                         emergencyContactPhone: str = Form(...),
                         file: UploadFile = File(None)
                         ):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/patient"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]

    data = {
        "firstName": firstName,
        "lastName": lastName,
        "gender": gender,
        "phoneNumber": phoneNumber,
        "birthday": birthday,
        "userId": str(userId),
        "typeOfBlood": typeOfBlood,
        "emergencyContactName": emergencyContactName,
        "emergencyContactPhone": emergencyContactPhone
    }

    files = None
    if file is not None:
        files = {"file": (file.filename, await file.read(), file.content_type)}

    try:
        response = requests.post(url, headers=headers, data=data, files=files)
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.put("/patients/{patientId}")
async def update_patient(request: Request, patientId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/patient/{patientId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.put(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})

# =============== MEDICAL APPOINTMENTS ===============


@medical_record_router.get("/medical-appointments")
async def get_all_medical_appointments(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medicalAppointment"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/medical-appointments/{appointmentId}")
async def get_medical_appointment_by_id(request: Request, appointmentId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medicalAppointment/{appointmentId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/medical-appointments/doctor/{doctorId}")
async def get_medical_appointments_by_doctor_id(request: Request, doctorId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medicalAppointment/medicalAppointments/doctor/{doctorId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/medical-appointments/patient/{patientId}")
async def get_medical_appointments_by_patient_id(request: Request, patientId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medicalAppointment/medicalAppointments/patient/{patientId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.post("/medical-appointments")
async def create_medical_appointment(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medicalAppointment"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.post(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.put("/medical-appointments/{appointmentId}")
async def update_medical_appointment(request: Request, appointmentId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medicalAppointment/{appointmentId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.put(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.delete("/medical-appointments/{appointmentId}")
async def delete_medical_appointment(request: Request, appointmentId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medicalAppointment/{appointmentId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return {"message": "Medical appointment deleted successfully"}
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})

# =============== MEDICATIONS ===============


@medical_record_router.get("/medications")
async def get_all_medications(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/medications/{medicationId}")
async def get_medication_by_id(request: Request, medicationId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications/{medicationId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.post("/medications")
async def create_medication(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.post(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.put("/medications/{medicationId}")
async def update_medication(request: Request, medicationId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications/{medicationId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.put(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})

# =============== PRESCRIPTIONS ===============


@medical_record_router.get("/prescriptions")
async def get_all_prescriptions(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications/prescriptions"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/prescriptions/{prescriptionId}")
async def get_prescription_by_id(request: Request, prescriptionId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications/prescriptions/{prescriptionId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/prescriptions/medicalRecord/{medicalRecordId}")
async def get_prescriptions_by_medical_record_id(request: Request, medicalRecordId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications/prescriptions/medicalRecordId/{medicalRecordId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.post("/prescriptions")
async def create_prescription(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications/prescriptions"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.post(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.put("/prescriptions/{prescriptionId}")
async def update_prescription(request: Request, prescriptionId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications/prescriptions/{prescriptionId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.put(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})

# =============== TREATMENTS ===============


@medical_record_router.get("/treatments")
async def get_all_treatments(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/treatments"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/treatments/{treatmentId}")
async def get_treatment_by_id(request: Request, treatmentId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/treatments/{treatmentId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/treatments/medicalRecord/{medicalRecordId}")
async def get_treatments_by_medical_record_id(request: Request, medicalRecordId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/treatments/medicalRecordId/{medicalRecordId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.post("/treatments")
async def create_treatment(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/treatments"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.post(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.put("/treatments/{treatmentId}")
async def update_treatment(request: Request, treatmentId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/treatments/{treatmentId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.put(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})

# =============== MEDICAL EXAMS ===============


@medical_record_router.get("/medical-exams")
async def get_all_medical_exams(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medical-exam"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/medical-exams/{medicalExamId}")
async def get_medical_exam_by_id(request: Request, medicalExamId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medical-exam/{medicalExamId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/medical-exams/medicalRecord/{medicalRecordId}")
async def get_medical_exams_by_medical_record_id(request: Request, medicalRecordId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medical-exam/medicalRecordId/{medicalRecordId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.post("/medical-exams")
async def create_medical_exam(request: Request,
                              title: str = Form(...),
                              description: str = Form(...),
                              date: str = Form(...),
                              medicalRecordId: int = Form(...),
                              file: UploadFile = File(None)
                              ):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medical-exam"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]

    data = {
        "title": title,
        "description": description,
        "date": date,
        "medicalRecordId": str(medicalRecordId)
    }

    files = None
    if file is not None:
        files = {"file": (file.filename, await file.read(), file.content_type)}

    try:
        response = requests.post(url, headers=headers, data=data, files=files)
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.delete("/medical-exams/{medicalExamId}")
async def delete_medical_exam(request: Request, medicalExamId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medical-exam/{medicalExamId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return {"message": "Medical exam deleted successfully"}
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})

# =============== REASONS OF CONSULTATION ===============


@medical_record_router.get("/reasons-of-consultation")
async def get_all_reasons_of_consultation(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/reasons-of-consultation"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/reasons-of-consultation/{reasonId}")
async def get_reason_of_consultation_by_id(request: Request, reasonId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/reasons-of-consultation/{reasonId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/reasons-of-consultation/medicalRecord/{medicalRecordId}")
async def get_reasons_of_consultation_by_medical_record_id(request: Request, medicalRecordId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/reasons-of-consultation/medicalRecordId/{medicalRecordId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.post("/reasons-of-consultation")
async def create_reason_of_consultation(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/reasons-of-consultation"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.post(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.put("/reasons-of-consultation/{reasonId}")
async def update_reason_of_consultation(request: Request, reasonId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/reasons-of-consultation/{reasonId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.put(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})

# =============== MEDICATION TYPES ===============


@medical_record_router.get("/medication-types")
async def get_all_medication_types(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications/medicationTypes"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.get("/medication-types/{medicationTypeId}")
async def get_medication_type_by_id(request: Request, medicationTypeId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications/medicationTypes/{medicationTypeId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.post("/medication-types")
async def create_medication_type(request: Request):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications/medicationTypes"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.post(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})


@medical_record_router.put("/medication-types/{medicationTypeId}")
async def update_medication_type(request: Request, medicationTypeId: int = Path(...)):
    url = f"{MICROSERVICE_MEDICAL_RECORD}/medical-record/medications/medicationTypes/{medicationTypeId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.put(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Medical Record error: {response.text}"})
