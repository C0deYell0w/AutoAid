from django.shortcuts import render,redirect
from Guest.models import *
from User.models import Mfbschedule,Usrfeedback

# Create your views here.

def mfbhomepage(request):
    if 'mfbid' in request.session:
        mfb=Newmfb.objects.get(id=request.session['mfbid'])
        feedbacks=Usrfeedback.objects.all()
        return render(request,"Mfb/mfbhomepage.html",{'mfb':mfb,'fedb':feedbacks})
    else:
        return redirect("Guest:login")

def mfbprofile(request):
    if 'mfbid' in request.session:
        mfb=Newmfb.objects.get(id=request.session['mfbid'])
        return render(request,"Mfb/mfbprofile.html",{'mfb':mfb})
    else:
        return redirect("Guest:login")

def editmfbprofile(request,mfbid):
    if 'mfbid' in request.session:
        mfbs=Newmfb.objects.get(id=mfbid)
        if request.method=="POST":
            mfbs.mfb_name=request.POST.get('txtname')
            mfbs.mfb_contact=request.POST.get('txtcontact')
            mfbs.mfb_email=request.POST.get('txtemail')
            mfbs.mfb_address=request.POST.get('txtaddress')
            mfbs.save()
            return redirect("Mfb:mfbprofile")
        else:    
            return render(request,"Mfb/editmfbprofile.html",{'mfb':mfbs})
    else:
        return redirect("Guest:login")

def changemfbpswd(request,mfbid):
    if 'mfbid' in request.session:
        mfb=Newmfb.objects.get(id=mfbid)
        if request.method=="POST":
            currpswd=mfb.password
            oldpswd=request.POST.get('cpswd')
            if currpswd != oldpswd:
                error="Incorrect Password.!!"
                return render(request,"Mfb/changemfbpswd.html",{'ER':error})
            else:
                mfb=Newmfb.objects.get(id=mfbid)
                newpswd=request.POST.get('npswd')
                mfb.password=newpswd
                mfb.save()
                return redirect('Guest:login')
        else:
            return render(request,"Mfb/changemfbpswd.html")
    else:
        return redirect("Guest:login")

def mfbbooking(request):
    if 'mfbid' in request.session:
        mfb=Newmfb.objects.get(id=request.session["mfbid"])
        data=Mfbschedule.objects.filter(mfbid=mfb,mfbbooking_status=0)
        return render(request,"Mfb/mfbbooking.html",{'data':data})
    else:
        return redirect("Guest:login")

def acceptmfbbooking(request,acceptid):
    bookid=Mfbschedule.objects.get(id=acceptid)
    bookid.mfbbooking_status=1
    bookid.save()
    return redirect("Mfb:mfbbooking")

def rejectmfbbooking(request,rejectid):
    bookid=Mfbschedule.objects.get(id=rejectid)
    bookid.mfbbooking_status=2
    bookid.save()
    return redirect("Mfb:mfbbooking")

def aceptedmfbbookings(request):
    if 'mfbid' in request.session:
        mfb=Newmfb.objects.get(id=request.session["mfbid"])
        data=Mfbschedule.objects.filter(mfbid=mfb,mfbbooking_status=1)
        return render(request,"Mfb/acceptedmfbbookings.html",{'data':data})
    else:
        return redirect("Guest:login")

def rejectedmfbbookings(request):
    if 'mfbid' in request.session:
        mfb=Newmfb.objects.get(id=request.session["mfbid"])
        data=Mfbschedule.objects.filter(mfbid=mfb,mfbbooking_status=2)
        return render(request,"Mfb/rejectedmfbbookings.html",{'data':data})
    else:
        return redirect("Guest:login")

def payedbookings(request):
    if 'mfbid' in request.session:
        mfb=Newmfb.objects.get(id=request.session["mfbid"])
        data=Mfbschedule.objects.filter(mfbid=mfb,mfbbooking_status__gte=3,mfbbooking_status__lt=5)
        completed=Mfbschedule.objects.filter(mfbid=mfb,mfbbooking_status=5)
        return render(request,"Mfb/payedbookings.html",{'data':data,'completed':completed})
    else:
        return redirect("Guest:login")

def ontheway(request,rid):
    bid=Mfbschedule.objects.get(id=rid)
    bid.mfbbooking_status=4
    bid.save()
    return redirect("Mfb:payedbookings")

def deliverycompleted(request,rid):
    bid=Mfbschedule.objects.get(id=rid)
    bid.mfbbooking_status=5
    bid.save()
    return redirect("Mfb:payedbookings")

def logout(request):
    del request.session["mfbid"]
    return redirect("Guest:Home")       