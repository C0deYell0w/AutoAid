from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import Usrfeedback,Repairschedule
# Create your views here.

def mechreg(request):
    st=State.objects.all()
    dist=District.objects.all()
    place=Place.objects.all()
    lp=Localplace.objects.all()
    if request.method=="POST":
        s=State.objects.get(id=request.POST.get('statedrop'))
        dt=District.objects.get(id=request.POST.get('distdrop'))
        pl=Place.objects.get(id=request.POST.get('selplace'))
        locpl=Localplace.objects.get(id=request.POST.get('localplace'))
        Newmechanic.objects.create(mech_name=request.POST.get('txtname'),mech_contact=request.POST.get('txtcontact'),mech_email=request.POST.get('txtemail'),mech_address=request.POST.get('txtaddress'),mech_certificate=request.FILES.get('photo1'),password=request.POST.get('pswd'),localplace=locpl)
        return render(request,"Guest/mechanicregistration.html",{'dist':dist,'localplace':lp,'state':st,'place':place})
    else:
        return render(request,"Guest/mechanicregistration.html",{'dist':dist,'localplace':lp,'state':st,'place':place})

def Ajaxlocalplace(request):
    dt=District.objects.get(id=request.GET.get('isdd'))
    pl=Place.objects.filter(district=dt)
    return render(request,"Admin/ajaxlocalplace.html",{'dist':pl})

def Ajaxnewmech(request):
    pla=Place.objects.get(id=request.GET.get('lpdd'))
    lp=Localplace.objects.filter(place=pla)
    return render(request,"Guest/ajaxmech.html",{'localplace':lp})

def mfbreg(request):
    st=State.objects.all()
    dist=District.objects.all()
    place=Place.objects.all()
    lp=Localplace.objects.all()
    if request.method=="POST":
        s=State.objects.get(id=request.POST.get('statedrop'))
        dt=District.objects.get(id=request.POST.get('distdrop'))
        pl=Place.objects.get(id=request.POST.get('selplace'))
        locpl=Localplace.objects.get(id=request.POST.get('localplace'))
        Newmfb.objects.create(mfb_name=request.POST.get('txtmfbname'),mfb_contact=request.POST.get('txtmfbcontact'),mfb_email=request.POST.get('txtmfbemail'),mfb_address=request.POST.get('txtmfbaddress'),mfb_liscence=request.FILES.get('mfblicense'),password=request.POST.get('pswd'),localplace=locpl)
        return render(request,"Guest/newmfb.html",{'dist':dist,'localplace':lp,'state':st,'place':place})
    else:
        return render(request,"Guest/newmfb.html",{'dist':dist,'localplace':lp,'state':st,'place':place})

def usrreg(request):
    st=State.objects.all()
    dist=District.objects.all()
    place=Place.objects.all()
    lp=Localplace.objects.all()
    if request.method=="POST":
        s=State.objects.get(id=request.POST.get('statedrop'))
        dt=District.objects.get(id=request.POST.get('distdrop'))
        pl=Place.objects.get(id=request.POST.get('selplace'))
        locpl=Localplace.objects.get(id=request.POST.get('localplace'))
        Newusr.objects.create(usr_name=request.POST.get('txtusrname'),usr_contact=request.POST.get('txtusrcontact'),usr_email=request.POST.get('txtusremail'),usr_address=request.POST.get('txtusraddress'),usr_gender=request.POST.get('usrrdo'),usr_photo=request.FILES.get('usrphoto'),usr_dob=request.POST.get('usrdob'),password=request.POST.get('pswd'),localplace=locpl)
        return render(request,"Guest/newuser.html",{'dist':dist,'localplace':lp,'state':st,'place':place})
    else:
        return render(request,"Guest/newuser.html",{'dist':dist,'localplace':lp,'state':st,'place':place})

def login(request):
    if request.method=="POST":
        Email=request.POST.get('txtemail')
        Password=request.POST.get('pswd')
        usrlogin=Newusr.objects.filter(usr_email=Email,password=Password).count()
        mfblogin=Newmfb.objects.filter(mfb_email=Email,password=Password).count()
        mechlogin=Newmechanic.objects.filter(mech_email=Email,password=Password).count()
        adminlogin=Admindb.objects.filter(admn_email=Email,password=Password).count()
        if usrlogin > 0:
            usr=Newusr.objects.get(usr_email=Email,password=Password)
            request.session['usrid']=usr.id
            return redirect('User:usrhomepage')
        elif mfblogin > 0:
            mfb=Newmfb.objects.get(mfb_email=Email,password=Password)
            request.session['mfbid']=mfb.id
            return redirect('Mfb:mfbhomepage')
        elif mechlogin > 0:
            mech=Newmechanic.objects.get(mech_email=Email,password=Password)
            request.session['mechid']=mech.id
            return redirect('Mechanic:mechhomepage')
        elif adminlogin > 0:
            admn=Admindb.objects.get(admn_email=Email,password=Password)
            request.session['admnid']=admn.id
            return redirect('projectadmin:adminhome')
        else:
            error="Invalid  Email/Password.!!"
            return render(request,"Guest/Login.html",{'ERR':error})
    else:
        return render(request,"Guest/Login.html")  

def Home(request):
    usrcount=Newusr.objects.all().count()
    feedbacks=Usrfeedback.objects.all()
    mechcount=Newmechanic.objects.all().count()
    workscount=Repairschedule.objects.filter(booking_status=5).count()
    return render(request,'Guest/Home.html',{'usrcount':usrcount,'fedb':feedbacks,'mechcount':mechcount,'workscount':workscount})

def mechtermsandconditions(request):
    return render(request,'Guest/mechterms.html')

def mfbtermsandconditions(request):
    return render(request,'Guest/mfbterms.html')