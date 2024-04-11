from django.urls import path
from . import views

urlpatterns = [
    
    path("bmi/", views.home, name="home"),
    path("bmi/<int:pk>/", views.BMIRecordDetailView.as_view(), name="detail"),
]
