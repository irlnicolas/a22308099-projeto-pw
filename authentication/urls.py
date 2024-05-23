from django.urls import path
from .views import view_login, view_register, view_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', view_login, name='login'),
    path('register/', view_register, name='register'),
    path('logout/', view_logout, name='logout'),

    # recuperação de password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/custom_password_reset_form.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/custom_password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/custom_password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/custom_password_reset_complete.html'), name='password_reset_complete'),
]
