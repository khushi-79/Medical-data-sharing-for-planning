from django.shortcuts import redirect, render
from datetime import date
from xmlrpc.client import DateTime
import  datetime
#from HospitalApp.models.HospitalAuthModel import *
from django.contrib import messages
from HospitalApp.models.HospitalAuthModel import tbl_hospital_register
from HospitalApp.models.PatientModel import tbl_patient_information
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from HospitalSite.settings import LOGIN_REDIRECT_URL
from django.conf import settings
from qrcode import *
import time

# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf 

def generate(gender):
    final = ""
    if gender=="Male":
        final = final+"01"
        return final
    elif gender=="Female":
        final = final+"10"
        return final
    elif gender=="Other ":
        final = final+"11"
        return final
    

        
        
@login_required(login_url= LOGIN_REDIRECT_URL)
def Add_PersonalInfo(request): 
    if request.method == "POST":
        AadhaarID = request.POST.get('AadhaarId')
        AadhaarID = AadhaarID.replace('-', '')
        
        pname = request.POST.get('pname')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        bgroup = request.POST.get('bloodgroup')
        bpressure = request.POST.get('bp')
        diabetes = request.POST.get('Diabetes')
        colestrol = request.POST.get('Colestrol')

        fdoc = request.POST.get('fdoc')
        fdocnumber = request.POST.get('fdocnumber')
        allergies = request.POST.get('Allergies')
        surgery = request.POST.get('Surgery')
        category = request.POST.get('category')
        father_name = request.POST.get('m_pname')
        surname  = request.POST.get('l_pname')
        surname  = str(surname)
        AddedBy = request.session['loggedin_user']
        health_card_number = pname[0].upper()+pname[-1].upper()+surname[0].upper()+surname[-1].upper()+generate(gender)
        count= tbl_patient_information.objects.all().count()
        test  = "00000"
        final_health_num = health_card_number+test +str(count+1)
        pname = pname+" "+surname

        

        if tbl_patient_information.objects.filter(AadhaarId=AadhaarID).first():
                messages.warning(request, 'Patient data already added!')
                return redirect('/personal-info')
        else:
            request.session['Aadhaar_ID'] = AadhaarID 
            patient_obj = tbl_patient_information.objects.create( AadhaarId = AadhaarID,
                        name =pname,number =  phone,dob = dob,gender = gender,category=category,address = address,bloodgroup = bgroup,bloodpressure = bpressure,diabetes=diabetes,colestrol = colestrol,
                        familydoctor_name =fdoc,  health_card=final_health_num,  doctor_number = fdocnumber,allergies = allergies,surgeryhistory = surgery, AddedBy=AddedBy,created_at= datetime.datetime.now())
            patient_obj.save()
          
          

            messages.success(request, "Data Added Successfully")
           
            #return redirect('/pdf')
            img = make("patient name              :"+pname 
                    +"\nMiddle name               :"+surname
                    +"\nFather name               :"+father_name
                    +"\nPatient Health Card Number:"+AadhaarID
                    +"\nDOB                       :"+dob
                    +"\ngender                    :"+gender
                    +"\nBlood Group               :"+bgroup
                    +"\nBlood Pressure            :"+bpressure
                    +"\nDiabetes                  :"+diabetes
                    +"\nColestrol                 :"+colestrol
                    +"\nFamily Doctor             :"+fdoc
                    +"\nFamily Doctor Number      :"+fdocnumber
                    +"\nAllergies                 :"+allergies
                    +"\nsurgery details           :"+surgery)
            img_name = 'qr' + str(time.time()) + '.png'
            img.save("static/"+ img_name)
            pdata = tbl_patient_information.objects.filter(AadhaarId=AadhaarID).first()                 
            return render(request, 'dashboard/card-generator.html',{'data':pdata,'img_name': img_name}) 
        
            

      
    return render(request, 'dashboard/patient-personal-info.html')

  


#Creating a class based view

def GeneratePdf(request):
         
        # getting the template
    
    #pdf = html_to_pdf('dashboard/card-generator.html')
         
        # rendering the template
        #
        #  
    
    return render(request, 'dashboard/patient-personal-info.html',{'data':pdata})        
    #return HttpResponse(pdf, content_type='application/pdf',)