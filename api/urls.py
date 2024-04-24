from django.urls import path
from .views import *
from api import views


urlpatterns = [
    path('languagelist/', views.LanguageListCreateView.as_view(), name='languagelist'),
    path('languagelist/<int:pk>/',views.LanguageRetrieveUpdateDestroyView.as_view(), name='languagelist_detail'),
    # path('signup/', views.signup),
    # path('login/', views.login),    


]
