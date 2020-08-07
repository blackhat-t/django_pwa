from . import views
from django.urls import path

urlpatterns = [
    path('',views.MpesaLisst.as_view(), name='home'),
    path('mpesa/', views.MpesaList.as_view()),
    path('mpesa/<int:pk>/', views.MpesaDetail.as_view(),)

]
