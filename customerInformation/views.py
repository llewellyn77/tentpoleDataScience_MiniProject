
# Create your views here.
from django.contrib import messages
from django.shortcuts import render 
from django.http import HttpResponse
from customerInformation.models import CustomerInformation

# Create your views here.

def getCustomerInformation(request):
    #print(request.POST)
    if request.method == "POST":
      
      fName = request.POST['fname']
      lName = request.POST['lname']
      dateOfBirth = request.POST['dateOfBirth']

      #File not uploading/posting multidictkey error
      #filename = request.FILES['filename'].filename
     
      #Test If post was hit
      print("POST hit") 
      print(fName,lName,dateOfBirth)
      getCustomerInformation = CustomerInformation(fName=fName,lName=lName,dateOfBirth=dateOfBirth)
      getCustomerInformation.save()
      messages.success(request,"Submitted succefully")
      #Sent

    #Did not include file to submit due to errors but the rest is sent to the local postgresql database successfully


    

    # dateOfBirth = request.POST['dateOfBirth'] 
    # 
       
       #print(fname,lname,dateOfBirth,filename)
      # ins = customerInformation(fname=fname,lname=lname,dateOfBirth=dateOfBirth,filename=filename)
       #customerInformation.objects.create(fname=fname,lname=lname,dateOfBirth=dateOfBirth,file=file)
    #context{}
    return render(request,'templates/pages/customerInformation.html')