from django.urls import path
from Mfb import views
app_name="Mfb"
urlpatterns = [
   path('mfbhomepage/',views.mfbhomepage,name="mfbhomepage"),
   path('mfbprofile/',views.mfbprofile,name="mfbprofile"),
   path('editmfbprofile/<int:mfbid>',views.editmfbprofile,name="editmfbprofile"),
   path('changemfbpswd/<int:mfbid>',views.changemfbpswd,name="changemfbpswd"),
   path('mfbbooking/',views.mfbbooking,name="mfbbooking"),
   path('acceptmfbbooking/<int:acceptid>',views.acceptmfbbooking,name="acceptmfbbooking"),
   path('rejectmfbbooking/<int:rejectid>',views.rejectmfbbooking,name="rejectmfbbooking"),
   path('aceptedmfbbookings/',views.aceptedmfbbookings,name="aceptedmfbbookings"),
   path('rejectedmfbbookings/',views.rejectedmfbbookings,name="rejectedmfbbookings"),
   path('payedbookings/',views.payedbookings,name="payedbookings"),
   path('ontheway/<int:rid>',views.ontheway,name="ontheway"),
   path('deliverycompleted/<int:rid>',views.deliverycompleted,name="deliverycompleted"),
   path('logout/',views.logout,name="logout"),
]