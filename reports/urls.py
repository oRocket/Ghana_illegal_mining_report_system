from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from .views import report_edit, report_delete

urlpatterns = [
    path('', views.home, name='home'),
    path('reports/', views.report_list, name='report_list'),
    path('reports/<int:pk>/', views.report_detail, name='report_detail'),
    path('reports/<int:pk>/edit/', views.report_edit, name='report_edit'),  # Refer to views.report_edit
    path('reports/<int:pk>/delete/', views.report_delete, name='report_delete'),  # Refer to views.report_delete
    path('education/', views.education, name='education'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('submit/', views.submit_report, name='submit_report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('blog/edit/<int:post_id>/', views.edit_blog, name='edit_blog'),
    path('blog/<int:id>/delete/', views.delete_blog, name='delete_blog'),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)