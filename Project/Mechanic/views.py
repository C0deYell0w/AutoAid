from django.shortcuts import render,redirect
from Guest.models import *
from User.models import Repairschedule,Usrfeedback
# Create your views here.
def mechhomepage(request):
    if 'mechid' in request.session:
        mech=Newmechanic.objects.get(id=request.session['mechid'])
        feedbacks=Usrfeedback.objects.all()
        return render(request,"Mechanic/mechhomepage.html",{'mech':mech,'fedb':feedbacks})
    else:
        return redirect("Guest:login")

def mechprofile(request):
    if 'mechid' in request.session:
        mech=Newmechanic.objects.get(id=request.session['mechid'])
        return render(request,"Mechanic/mechprofile.html",{'mech':mech})
    else:
        return redirect("Guest:login")

def editmechprofile(request,mechid):
    if 'mechid' in request.session:
        mech=Newmechanic.objects.get(id=mechid)
        if request.method=="POST":
            mech.mech_name=request.POST.get('txtname')
            mech.mech_contact=request.POST.get('txtcontact')
            mech.mech_email=request.POST.get('txtemail')
            mech.mech_address=request.POST.get('txtaddress')
            mech.save()
            return redirect("Mechanic:mechprofile")
        else:    
            return render(request,"Mechanic/editmechprofile.html",{'mech':mech})
    else:
        return redirect("Guest:login")

def changemechpswd(request,mechid):
    if 'mechid' in request.session:
        mech=Newmechanic.objects.get(id=mechid)
        if request.method=="POST":
            currpswd=mech.password
            oldpswd=request.POST.get('cpswd')
            if currpswd != oldpswd:
                error="incorrect password.!!"
                return render(request,"Mechanic/changemechpswd.html",{'ER':error})
            else:
                mech=Newmechanic.objects.get(id=mechid)
                newpswd=request.POST.get('npswd')
                mech.password=newpswd
                mech.save()
                return redirect('Guest:login')
        else:
            return render(request,"Mechanic/changemechpswd.html")
    else:
        return redirect("Guest:login")

def bookings(request):
    if 'mechid' in request.session:
        mech=Newmechanic.objects.get(id=request.session["mechid"])
        data=Repairschedule.objects.filter(mechid=mech,booking_status=0)
        return render(request,"Mechanic/bookings.html",{'data':data})
    else:
        return redirect("Guest:login")

def acceptbooking(request,aid):
    bid=Repairschedule.objects.get(id=aid)
    bid.booking_status=1
    bid.save()
    return redirect("Mechanic:bookings")

def rejectbooking(request,rid):
    bid=Repairschedule.objects.get(id=rid)
    bid.booking_status=2
    bid.save()
    return redirect("Mechanic:bookings")

def Acceptedbookings(request):
    if 'mechid' in request.session:
        mech=Newmechanic.objects.get(id=request.session["mechid"])
        data=Repairschedule.objects.filter(mechid=mech,booking_status=1)
        return render(request,"Mechanic/acceptedbookings.html",{'data':data})
    else:
        return redirect("Guest:login")

def Paidbookings(request):
    if 'mechid' in request.session:
        mech=Newmechanic.objects.get(id=request.session["mechid"])
        data=Repairschedule.objects.filter(mechid=mech,booking_status__gte=3,booking_status__lt=5)
        completed=Repairschedule.objects.filter(mechid=mech,booking_status=5)
        return render(request,"Mechanic/paidbookings.html",{'data':data,'completed':completed})
    else:
        return redirect("Guest:login")

def Rejectedbookings(request):
    if 'mechid' in request.session:
        mech=Newmechanic.objects.get(id=request.session["mechid"])
        data=Repairschedule.objects.filter(mechid=mech,booking_status=2)
        return render(request,"Mechanic/rejectedbookings.html",{'data':data})
    else:
        return redirect("Guest:login")

def ontheway(request,rid):
    bid=Repairschedule.objects.get(id=rid)
    bid.booking_status=4
    bid.save()
    return redirect("Mechanic:paidbookings")

def workcompleted(request,rid):
    bid=Repairschedule.objects.get(id=rid)
    bid.booking_status=5
    bid.save()
    return redirect("Mechanic:paidbookings")

def logout(request):
    del request.session["mechid"]
    return redirect("Guest:Home")