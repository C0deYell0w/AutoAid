from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import*
# Create your views here.

def state(request):
    if 'admnid' in request.session:
        st=State.objects.all()
        if request.method=="POST":
            State.objects.create(state_name=request.POST.get("txtstate"))
            return render(request,"Admin/state.html",{'data':st})
        else:
            return render(request,"Admin/state.html",{'data':st})
    else:
        return redirect("Guest:login")

def district(request):
    if 'admnid' in request.session:
        st=State.objects.all()
        dist=District.objects.all()
        if request.method=="POST":
            s=State.objects.get(id=request.POST.get('statedrop'))
            District.objects.create(district_name=request.POST.get('txtdist'),state=s)
            return render(request,"Admin/district.html",{'state':st,'dist':dist})
        else:   
            return render(request,"Admin/district.html",{'state':st,'dist':dist})
    else:
        return redirect("Guest:login")

def vehicletype(request):
    if 'admnid' in request.session:
        vt=Vehicletype.objects.all()
        if request.method=="POST":
            Vehicletype.objects.create(vehicle_type=request.POST.get("txtvehicletype"))
            return render(request,"Admin/vehicletype.html",{'data':vt})
        else:
            return render(request,"Admin/vehicletype.html",{'data':vt})
    else:
        return redirect("Guest:login")

def brand(request):
    if 'admnid' in request.session:
        vt=Vehicletype.objects.all()
        brand=Brand.objects.all()
        if request.method=="POST":
            v=Vehicletype.objects.get(id=request.POST.get('vehicletypedrop'))
            Brand.objects.create(brand_name=request.POST.get('txtbrand'),vehicle_type=v)
            return render(request,"Admin/vehiclebrand.html",{'vehicletype':vt,'brand':brand})
        else:   
            return render(request,"Admin/vehiclebrand.html",{'vehicletype':vt,'brand':brand})
    else:
        return redirect("Guest:login")

def editstate(request,sid):
    if 'admnid' in request.session:
        st=State.objects.get(id=sid)
        if request.method=="POST":
            st.state_name=request.POST.get('txtstate')
            st.save()
            return redirect("projectadmin:state")
        else:
            return render(request,"Admin/editstate.html",{'state':st})
    else:
        return redirect("Guest:login")

def delstate(request,sid):
    state=State.objects.get(id=sid)
    state.delete()
    return redirect("projectadmin:state")

def deldistrict(request,did):
    dis=District.objects.get(id=did)
    dis.delete()
    return redirect("projectadmin:district")

def editvehicletype(request,vtid):
    if 'admnid' in request.session:
        vt=Vehicletype.objects.get(id=vtid)
        if request.method=="POST":
            vt.vehicle_type=request.POST.get('txtvehicletype')
            vt.save()
            return redirect("projectadmin:vehicletype")
        else:
            return render(request,"Admin/editvehicletype.html",{'vehtyp':vt})
    else:
        return redirect("Guest:login")

def delvehicletype(request,vtid):
    vt=Vehicletype.objects.get(id=vtid)
    vt.delete()
    return redirect("projectadmin:vehicletype")

def delbrand(request,bid):
    br=Brand.objects.get(id=bid)
    br.delete()
    return redirect("projectadmin:brand")

def place(request):
    if 'admnid' in request.session:
        st=State.objects.all()
        dist=District.objects.all()
        pl=Place.objects.all()
        if request.method=="POST":
            s=State.objects.get(id=request.POST.get('statedrop'))
            dt=District.objects.get(id=request.POST.get('distdrop'))
            Place.objects.create(place_name=request.POST.get('txtplace'),district=dt)
            return render(request,"Admin/place.html",{'state':st,'place':pl,'dist':dist})
        else:
            return render(request,"Admin/place.html",{'state':st,'place':pl,'dist':dist})
    else:
        return redirect("Guest:login")
        
def Ajaxplace(request):
    st=State.objects.get(id=request.GET.get('disd'))
    dist=District.objects.filter(state=st)
    return render(request,"Admin/ajaxplace.html",{'dist':dist})

def delplace(request,pid):
    pl=Place.objects.get(id=pid)
    pl.delete()
    return redirect("projectadmin:place")

def localplace(request):
    if 'admnid' in request.session:
        st=State.objects.all()
        dist=District.objects.all()
        lp=Localplace.objects.all()
        if request.method=="POST":
            s=State.objects.get(id=request.POST.get('statedrop'))
            dt=District.objects.get(id=request.POST.get('distdrop'))
            pl=Place.objects.get(id=request.POST.get('placedrop'))
            Localplace.objects.create(local_place=request.POST.get('txtlocalplace'),place=pl)
            return render(request,"Admin/localplace.html",{'dist':dist,'localplace':lp,'state':st,})
        else:
            return render(request,"Admin/localplace.html",{'dist':dist,'localplace':lp,'state':st,})
    else:
        return redirect("Guest:login")

def Ajaxlocalplace(request):
    dt=District.objects.get(id=request.GET.get('isdd'))
    pl=Place.objects.filter(district=dt)
    return render(request,"Admin/ajaxlocalplace.html",{'dist':pl})

def dellocalplace(request,lpid):
    lp=Localplace.objects.get(id=lpid)
    lp.delete()
    return redirect("projectadmin:localplace")

def adminhome(request):
    if 'admnid' in request.session:
        admn=Admindb.objects.get(id=request.session['admnid'])
        data=Repairschedule.objects.filter(booking_status=5)
        data2=Mfbschedule.objects.filter(mfbbooking_status=5) 
        photo=Newusr.objects.all()
        usrcount=Newusr.objects.all().count()
        bookingscount=Repairschedule.objects.filter(booking_status=5).count()
        ordercount=Mfbschedule.objects.filter(mfbbooking_status=5).count()
        return render(request,"Admin/adminhomepage.html",{'admn':admn,'data':data,'data2':data2,'usrcount':usrcount,'bookingscount':bookingscount,'ordercount':ordercount,'photo':photo })
    else:
        return redirect("Guest:login")

def mechverification(request):
    if 'admnid' in request.session:
        data=Newmechanic.objects.filter(mech_status=0)
        return render(request,"Admin/mechverification.html",{'data':data})
    else:
        return redirect("Guest:login")
        
def acceptmech(request,acceptmechid):
    reqid=Newmechanic.objects.get(id=acceptmechid)
    reqid.mech_status=1
    reqid.save()
    return redirect("projectadmin:mechverification")

def rejectmwech(request,rejectmechid):
    reqid=Newmechanic.objects.get(id=rejectmechid)
    reqid.mech_status=2
    reqid.save()
    return redirect("projectadmin:mechverification")

def aceptedrequests(request):
    if 'admnid' in request.session:
        data=Newmechanic.objects.filter(mech_status=1)
        return render(request,"Admin/acceptedrequests.html",{'data':data})
    else:
        return redirect("Guest:login")

def rejectedrequests(request):
    if 'admnid' in request.session:
        data=Newmechanic.objects.filter(mech_status=2)
        return render(request,"Admin/rejectedrequests.html",{'data':data})
    else:
        return redirect("Guest:login")

def mfbverification(request):
    if 'admnid' in request.session:
        data=Newmfb.objects.filter(mfb_status=0)
        return render(request,"Admin/mfbverification.html",{'data':data})
    else:
        return redirect("Guest:login")

def acceptmfb(request,acceptmfbid):
    mfbreqid=Newmfb.objects.get(id=acceptmfbid)
    mfbreqid.mfb_status=1
    mfbreqid.save()
    return redirect("projectadmin:mfbverification")

def rejectmfb(request,rejectmfbid):
    mfbreqid=Newmfb.objects.get(id=rejectmfbid)
    mfbreqid.mfb_status=2
    mfbreqid.save()
    return redirect("projectadmin:mfbverification")

def aceptedmfbrequests(request):
    if 'admnid' in request.session:
        data=Newmfb.objects.filter(mfb_status=1)
        return render(request,"Admin/aceptedmfbrequests.html",{'data':data})
    else:
        return redirect("Guest:login")

def rejectedmfbrequests(request):
    if 'admnid' in request.session:
        data=Newmfb.objects.filter(mfb_status=2)
        return render(request,"Admin/rejectedmfbrequests.html",{'data':data})
    else:
        return redirect("Guest:login")

def viewfeedback(request):
    if 'admnid' in request.session:
        data=Usrfeedback.objects.all()
        return render(request,"Admin/viewfeedback.html",{'data':data})
    else:
        return redirect("Guest:login")

def complaints(request):
    if 'admnid' in request.session:
        data=Usrcomplaint.objects.filter(complaint_status=0)
        return render(request,"Admin/complaints.html",{'data':data})
    else:
        return redirect("Guest:login")

def respond(request,compid):
    if 'admnid' in request.session:
        response=request.POST.get("response")
        if request.method=="POST":
            resid=Usrcomplaint.objects.get(id=compid)
            resid.complaint_response=response
            resid.complaint_status=1
            resid.save()
            return redirect("projectadmin:complaints")
        else:
            return render(request,"Admin/respond.html")
    else:
        return redirect("Guest:login")

def logout(request):
    del request.session["admnid"]
    return redirect("Guest:Home")        

def paymentreportmechanic(request):
    if request.method=="POST":
        if request.POST.get('txtf')!="" and request.POST.get('txtt')!="":
            data=Repairschedule.objects.filter(dt_of_booking__gte=request.POST.get('txtf'),dt_of_booking__lte=request.POST.get('txtt'),booking_status=5)
            return render(request,"Admin/PaymentReportMechanic.html",{'data':data})
        elif  request.POST.get('txtf')!="":
            data=Repairschedule.objects.filter(dt_of_booking__gte=request.POST.get('txtf'),booking_status=5)
            return render(request,"Admin/PaymentReportMechanic.html",{'data':data})
        else:
            data=Repairschedule.objects.filter(dt_of_booking__lte=request.POST.get('txtt'),booking_status=5)
            return render(request,"Admin/PaymentReportMechanic.html",{'data':data})
    else:
        return render(request,"Admin/PaymentReportMechanic.html")
    
def paymentreportmfb(request):
    if request.method=="POST":
        if request.POST.get('txtf')!="" and request.POST.get('txtt')!="":
            data=Mfbschedule.objects.filter(dt_of_booking__gte=request.POST.get('txtf'),dt_of_booking__lte=request.POST.get('txtt'),mfbbooking_status=5)
            return render(request,"Admin/PaymentReportMechanic.html",{'data':data})
        elif  request.POST.get('txtf')!="":
            data=Mfbschedule.objects.filter(dt_of_booking__gte=request.POST.get('txtf'),mfbbooking_status=5)
            return render(request,"Admin/PaymentReportMechanic.html",{'data':data})
        else:
            data=Mfbschedule.objects.filter(dt_of_booking__lte=request.POST.get('txtt'),mfbbooking_status=5)
            return render(request,"Admin/PaymentReportMfb.html",{'data':data})
    else:
        return render(request,"Admin/PaymentReportMfb.html")