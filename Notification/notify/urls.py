from django.urls import path
from . import views
urlpatterns = [
    path('',views.email_compose,name='create'),
    path('mail_all/',views.mail_bulk,name='mail_all'),
path('detail/<id>',views.mail_detail,name='detail'),
    path('list',views.mail_list,name='list')

]