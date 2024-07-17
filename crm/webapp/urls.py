from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    
    path('register',views.register, name='register'),

    path('my-login', views.my_login, name='login'),

    path('logout', views.user_logout, name='logout'),

    # CRUD

    path('my-dashboard', views.dashboard, name='dashboard'),

    path('create-record', views.create_record, name='create_record'),

    path('update-record/<int:record_id>', views.update_record, name='update_record'),

    path('view-record/<int:record_id>', views.view_record, name='view_record'),

    path('delete-record/<int:record_id>', views.delete_record, name='delete_record'),

    path('search', views.search, name='search'),



]
