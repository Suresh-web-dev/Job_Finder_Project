
from django.urls import path
from job_finder_app.views import home,post_form,jobs,search,apply_form,apply_datas,one,admin_page,delete,signup_view,signup_datas,login_view,login_datas,logout_view

urlpatterns = [
    path('home',home),
    path('post_form/',post_form),
    path('jobs',jobs),
    path('search',search),
    path('apply_form',apply_form),
    path('apply_datas/',apply_datas),
    path('one/<int:id>/',one),
    path('admin_page',admin_page),
    path('delete/<id>',delete),
    path('signup/',signup_view),
    path('signup_datas',signup_datas),
    path('login_view/',login_view),
    path('login_datas',login_datas),
    path('logout/',logout_view)
]