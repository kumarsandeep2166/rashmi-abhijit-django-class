from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.simpleview),
    path('apicbv/',views.SimpleViewCBV.as_view()),
    # passed id through url
    path('apicbv/<int:id>/',views.SimpleViewGETCBV.as_view()),
    path('listcbv/', views.SimpleListCBV.as_view()),
]