from django.shortcuts import render,redirect
from .models import Info

# Home view
def home(request):
    mydata = Info.objects.all()
    if mydata != '' :
        return render(request, 'home.html',{'mydatas':mydata})
    else :
        return render(request, 'home.html')

# Add view
def Add(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        contact = request.POST['contact']
        mail = request.POST['mail'] 
        # Create and save new Info object
        obj = Info(Name=name, Age=age, Contact=contact, Mail=mail)     
        obj.save()
               
        # Fetch updated data after saving
        mydata = Info.objects.all()
        return redirect( 'home')
    
    return render(request, 'home.html')

def Update(request,id):
    mydata=Info.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        contact = request.POST['contact']
        mail = request.POST['mail']
        
        mydata.Name=name
        mydata.Age=age
        mydata.Contact=contact
        mydata.Mail=mail
        mydata.save()
        return redirect('home') 
    return render(request , 'update.html',{'data':mydata})

def Delete(request,id):
    mydata=Info.objects.get(id=id)
    mydata.delete()
    return redirect('home')