from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [
    path('mechreg/',views.mechreg,name="mechreg"),
    path('ajaxmechplace/',views.Ajaxnewmech,name="Ajax-mechplace"),
    path('mfbreg/',views.mfbreg,name="mfbreg"),
    path('usrreg/',views.usrreg,name="usrreg"),
    path('loginpage/',views.login,name="login"),
    path('mechtermsandconditions/',views.mechtermsandconditions,name="mechtermsandconditions"),
    path('mfbtermsandconditions/',views.mfbtermsandconditions,name="mfbtermsandconditions"),
    path('',views.Home,name="Home"),

]