from django.urls import path
from .import views as v 

urlpatterns = [
    path('', v.home, name='home'),
    path('about/', v.about, name='about'),
    path('indextem/', v.indextem, name='indextem'),
    path('list/', v.list, name='list'),
    path('contact/', v.contact, name='contact'),
    path('success/',v.success, name='success'),
    path('register/',v.register, name='register'),
    path('login/',v.uslogin, name='uslogin'),
    path('logout/',v.uslogout, name='uslogout'),
    path('list/', v.list, name='list'),
    path('item/<int:pk>/edit/', v.editt, name='editt'),
    path('item/<int:pk>/delete/', v.delte, name='delte'),
    path('add/', v.add, name='add'),
    path('upload/', v.upload, name='upload'),
]




