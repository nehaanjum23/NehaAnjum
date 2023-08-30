from django.urls import path
from . import views
urlpatterns = [
    path('stu/',views.studentView.as_view()),
    path('stuget/',views.studentGetView.as_view()),
    path('stupdate/<int:id>/',views.studentUpdate.as_view()),
    path('studel/<int:id>/',views.studentDeleteView.as_view()),
   
]