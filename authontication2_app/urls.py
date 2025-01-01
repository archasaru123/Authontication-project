from django.urls import path
from . import views  # Import your views file (if views are in the same directory)

urlpatterns = [
    path('', views.signup, name='signup'),  # The view function 'data' and the URL name 'data'
    path('login/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home,name='home'),
]
 













 