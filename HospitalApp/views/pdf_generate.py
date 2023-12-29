from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from HospitalApp.models.PatientModel import tbl_patient_information
from HospitalSite.settings import LOGIN_REDIRECT_URL
from django.shortcuts import redirect, render
from django.contrib import messages
from HospitalApp.views.personalinfo import Add_PersonalInfo
from django.template import loader
from django.db import models
from django import template


def generate_pdf(request):
    
    buff = io.BytesIO()
    canvass = canvas.Canvas(buff, pagesize=letter, bottomup=0)
    text_obj = canvass.beginText()
    text_obj.setTextOrigin(inch, inch)
    text_obj.setFont("Helvetica", 14)
   
    ai = template.Library()
    

    data = tbl_patient_information.objects.filter(AadhaarId = 446767677676)
    print("Hello")
    lines = []

    for d in data:
        lines.append("Personal details")
        lines.append(d.name)
        # lines.append(d.dob)
        # lines.append(d.AadhaarId)
        lines.append(d.address)
        lines.append(d.gender)
        lines.append(d.category)
        lines.append(d.bloodgroup)
        lines.append(d.name)
        lines.append("")
        lines.append("Medical details")
        lines.append("")
        lines.append(d.bloodpressure)
        lines.append(d.diabetes)
        lines.append(d.colestrol)
        lines.append(d.familydoctor_name)
        lines.append(d.doctor_number)
        lines.append(d.allergies)
        lines.append(d.surgeryhistory)



    for i in lines:
        print(i)



    for l in lines:
        text_obj.textLines(l)

    canvass.drawText(text_obj)
    canvass.showPage()
    canvass.save()
    buff.seek(0)

    return (FileResponse(buff, as_attachment=True, filename='details.pdf'))