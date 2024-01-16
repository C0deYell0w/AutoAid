from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Guest.models import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def usrhomepage(request):
    if 'usrid' in request.session:
        usr=Newusr.objects.get(id=request.session['usrid'])
        feedbacks=Usrfeedback.objects.all()
        usrcount=Newusr.objects.all().count()
        mechcount=Newmechanic.objects.all().count()
        workscount1=Repairschedule.objects.filter(booking_status=5).count()
        workscount2=Mfbschedule.objects.filter(mfbbooking_status=5).count()
        completedprojects=workscount1+workscount2
        return render(request,"User/usrhomepage.html",{'user':usr,'fedb':feedbacks,'usrcount':usrcount,'mechcount':mechcount,'completedprojects':completedprojects})
    else:
        return redirect("Guest:login")

def usrprofile(request):
    if 'usrid' in request.session:
        usr=Newusr.objects.get(id=request.session['usrid'])
        return render(request,"User/usrprofile.html",{'user':usr})
    else:
        return redirect("Guest:login")

def editusrprofile(request,usrid):
    if 'usrid' in request.session:
        user=Newusr.objects.get(id=usrid)
        if request.method=="POST":
            user.usr_name=request.POST.get('txtname')
            user.usr_contact=request.POST.get('txtcontact')
            user.usr_email=request.POST.get('txtemail')
            user.usr_address=request.POST.get('txtaddress')
            user.save()
            return redirect("User:usrprofile")
        else:    
            return render(request,"User/editusrprofile.html",{'user':user})
    else:
        return redirect("Guest:login")

def changeusrpswd(request,usrid):
    if 'usrid' in request.session:
        user=Newusr.objects.get(id=usrid)
        if request.method=="POST":
            currpswd=user.password
            oldpswd=request.POST.get('cpswd')
            if currpswd != oldpswd:
                error="incorrect password.!!"
                return render(request,"User/changeusrpswd.html",{'ER':error})
            else:
                user=Newusr.objects.get(id=usrid)
                newpswd=request.POST.get('npswd')
                user.password=newpswd
                user.save()
                return redirect('Guest:login')
        else:
            return render(request,"User/changeusrpswd.html")
    else:
        return redirect("Guest:login")

def searchmechanic(request):
    if 'usrid' in request.session:
        usr=Newusr.objects.get(id=request.session['usrid'])
        st=State.objects.all()
        mech=Newmechanic.objects.all()
        return render(request,"User/SearchMechanic.html",{'state':st,'mech':mech,"usr":usr})
    else:
        return redirect("Guest:login")

def searchmfb(request):
    if 'usrid' in request.session:
        st=State.objects.all()
        mfb=Newmfb.objects.all()
        return render(request,"User/SearchMfb.html",{'state':st,'mfb':mfb})
    else:
        return redirect("Guest:login")
        
def Ajaxmech(request):
    if request.GET.get('lpid')!="":
        lp=Localplace.objects.get(id=request.GET.get('lpid'))
        mech=Newmechanic.objects.filter(localplace=lp)
        return render(request,"User/Ajaxmech.html",{'data':mech})
    elif request.GET.get('pid')!="":
        pl=Place.objects.get(id=request.GET.get('pid'))
        mech=Newmechanic.objects.filter(localplace__place=pl)
        return render(request,"User/Ajaxmech.html",{'data':mech})
    elif request.GET.get('did')!="":
        dis=District.objects.get(id=request.GET.get('did'))
        mech=Newmechanic.objects.filter(localplace__place__district=dis)
        return render(request,"User/Ajaxmech.html",{'data':mech})
    else:
        st=State.objects.get(id=request.GET.get('sid'))
        mech=Newmechanic.objects.filter(localplace__place__district__state=st)
        return render(request,"User/Ajaxmech.html",{'data':mech})

def Ajaxmfb(request):
    if request.GET.get('lpid')!="":
        lp=Localplace.objects.get(id=request.GET.get('lpid'))
        mfb=Newmfb.objects.filter(localplace=lp)
        return render(request,"User/Ajaxmfb.html",{'data':mfb})
    elif request.GET.get('pid')!="":
        pl=Place.objects.get(id=request.GET.get('pid'))
        mfb=Newmfb.objects.filter(localplace__place=pl)
        return render(request,"User/Ajaxmfb.html",{'data':mfb})
    elif request.GET.get('did')!="":
        dis=District.objects.get(id=request.GET.get('did'))
        mfb=Newmfb.objects.filter(localplace__place__district=dis)
        return render(request,"User/Ajaxmfb.html",{'data':mfb})
    else:
        st=State.objects.get(id=request.GET.get('sid'))
        mfb=Newmfb.objects.filter(localplace__place__district__state=st)
        return render(request,"User/Ajaxmfb.html",{'data':mfb})

def repairscheduling(request,mid):
    if 'usrid' in request.session:
        vt=Vehicletype.objects.all()
        brand=Brand.objects.all()
        mech=Newmechanic.objects.get(id=mid)
        name=mech.mech_name
        usr=Newusr.objects.get(id=request.session['usrid'])
        name1=usr.usr_name
        email1=mech.mech_email
        email2=usr.usr_email
        if request.method=="POST":
            veh=Vehicletype.objects.get(id=request.POST.get('vehtypdrop'))
            brnd=Brand.objects.get(id=request.POST.get('branddrop'))
            Repairschedule.objects.create(mechid=mech,uid=usr,current_location=request.POST.get('locationurl'),landmark=request.POST.get('landmarktxt'),veh_brand=brnd,model_name=request.POST.get('modelname'),model_year=request.POST.get('modelyear'),issue_note=request.POST.get('issuenote'))
            send_mail(
                'Dear Associate '+name, #subject
                "Dear Associate You Have a new Booking Request, Login To Your AutoAid Account To view Further Booking Details, Please Respond To Your Booking's Immeadiately. Thank You Team AutoAid.",#body
                settings.EMAIL_HOST_USER,
                [email1],

            )
            send_mail(
                ' Dear '+name1, #subject
                "Dear User We Have Recieved Your Service Request On Mechanic Booking And Is Currently Being Processed, We Kindly Request You To Wait Until Your Booking Is Confirmed And Accepted From The Mechanic  Thank You For Choosing Our SERVICE,  Team AutoAid.",#body
                settings.EMAIL_HOST_USER,
                [email2],

            )
            return redirect("User:mechbookingstatus")
        else:   
            return render(request,"User/repairscheduling.html",{'vehtype':vt})
    else:
        return redirect("Guest:login")

def Ajaxbrand(request):
    vt=Vehicletype.objects.get(id=request.GET.get('brandid'))
    brand=Brand.objects.filter(vehicle_type=vt)
    return render(request,"User/Ajaxbrand.html",{'brand':brand})

def mfbscheduling(request,mfbid):
    if 'usrid' in request.session:
        vt=Vehicletype.objects.all()
        mfb=Newmfb.objects.get(id=mfbid)
        usr=Newusr.objects.get(id=request.session['usrid'])
        if request.method=="POST":
            veh=Vehicletype.objects.get(id=request.POST.get('vehtypdrop'))
            Mfbschedule.objects.create(mfbid=mfb,usrid=usr,current_location=request.POST.get('locationurl'),landmark=request.POST.get('landmarktxt'),vehicle_type=veh,fuel_type=request.POST.get('fueltypedrop'),fuel_amount=request.POST.get('fuelamountdrop'))
            return render(request,"User/mfbscheduling.html",{'vehtype':vt})
        else:   
            return render(request,"User/mfbscheduling.html",{'vehtype':vt})
    else:
        return redirect("Guest:login")

def paymentpage(request,bookid):
    if request.method=="POST":
        booking=Mfbschedule.objects.get(id=bookid)
        booking.mfbbooking_status=3
        booking.save()
        return render(request,"User/processingpayment.html")
    else:
        return render(request,"User/payment.html")

def processingpayment(request):
    return render(request,"User/processingpayment.html")

def paymentsuccessful(request):
    return render(request,"User/paymentsuccessful.html")

def mfbbookingstatus(request):
    if 'usrid' in request.session:
        usr=Newusr.objects.get(id=request.session["usrid"])
        data=Mfbschedule.objects.filter(usrid=usr,mfbbooking_status__gte=0,mfbbooking_status__lt=5)
        completed=Mfbschedule.objects.filter(usrid=usr,mfbbooking_status=5)
        return render(request,"User/mfbbookingstatus.html",{'data':data,'completed':completed})
    else:
        return redirect("Guest:login")

def mechbookingstatus(request):
    if 'usrid' in request.session:
        usr=Newusr.objects.get(id=request.session["usrid"])
        data=Repairschedule.objects.filter(uid=usr,booking_status__gte=0,booking_status__lt=5)
        completed=Repairschedule.objects.filter(uid=usr,booking_status=5)
        return render(request,"User/mechbookingstatus.html",{'data':data,'completed':completed})
    else:
        return redirect("Guest:login")
        
def mechpayment(request,bookingid):
    if request.method=="POST":
        booking=Repairschedule.objects.get(id=bookingid)
        booking.booking_status=3
        booking.save()
        return render(request,"User/mechprocessingpayment.html")
    else:
        return render(request,"User/mechpayment.html")

def mechprocessingpayment(request):
    return render(request,"User/mechprocessingpayment.html")

def mechpaymentsuccessful(request):
    return render(request,"User/mechpaymentsuccessful.html")

def complaint(request):
    if 'usrid' in request.session:
        if request.method=="POST":
            usr=Newusr.objects.get(id=request.session["usrid"])
            Usrcomplaint.objects.create(usrid=usr,complaint=request.POST.get('txtcomplaint'))
            return render(request,"User/complaint.html")
        else:
            return render(request,"User/complaint.html")
    else:
        return redirect("Guest:login")

def feedback(request):
    if 'usrid' in request.session:
        if request.method=="POST":
            usr=Newusr.objects.get(id=request.session["usrid"])
            Usrfeedback.objects.create(usrid=usr,feedback=request.POST.get('txtfeed'))
            return render(request,"User/feed.html")
        else:
            return render(request,"User/feed.html")
    else:
        return redirect("Guest:login")

def viewresponse(request):
    if 'usrid' in request.session:
        usr=Newusr.objects.get(id=request.session["usrid"])
        data=Usrcomplaint.objects.filter(usrid=usr,complaint_status=1)
        return render(request,"User/viewresponse.html",{'data':data})
    else:
        return redirect("Guest:login")

def starrating(request):
    return render(request,"User/starrating.html")

def logout(request):
    del request.session["usrid"]
    return redirect("Guest:Home")    

def clock(request):
    return render(request,"User/clock.html")