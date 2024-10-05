from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Set the home view for the root URL of the app
    path('reports/', views.report_list, name='report_list'),
    path('education/', views.education, name='education'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('submit/', views.submit_report, name='submit_report'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Add the dashboard URL pattern
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:post_id>/', views.blog_detail, name='blog_detail'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)