from django.urls import path
from Mechanic import views
app_name="Mechanic"
urlpatterns = [
    path('mechhomepage/',views.mechhomepage,name="mechhomepage"),
    path('mechprofile/',views.mechprofile,name="mechprofile"),
    path('editmechprofile/<int:mechid>',views.editmechprofile,name="editmechprofile"),
    path('changemechpswd/<int:mechid>',views.changemechpswd,name="changemechpswd"),
    path('bookings/',views.bookings,name="bookings"),
    path('acceptbooking/<int:aid>',views.acceptbooking,name="acceptbooking"),
    path('rejectbooking/<int:rid>',views.rejectbooking,name="rejectbooking"),
    path('acceptedbookings/',views.Acceptedbookings,name="Acceptedbookings"),
    path('rejectedbookings/',views.Rejectedbookings,name="Rejectedbookings"),
    path('Paidbookings/',views.Paidbookings,name="paidbookings"),
    path('ontheway/<int:rid>',views.ontheway,name="ontheway"),
    path('workcompleted/<int:rid>',views.workcompleted,name="workcompleted"),
    path('logout/',views.logout,name="logout"),
]