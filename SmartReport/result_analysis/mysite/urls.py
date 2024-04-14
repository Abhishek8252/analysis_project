from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .core import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('results/', views.result_list, name='result_list'),
    # path('analysis_list/', views.analysis_list, name='analysis_list'),
    path('result_analysis/', views.result_analysis, name='result_analysis'),
    path('results/upload/', views.upload_result, name='upload_result'),
    path('results/<int:pk>/', views.delete_result, name='delete_result'),
    path('result_analysis/<int:pk>/', views.delete_analysis, name='delete_analysis'),
    path('results', views.read_more, name='read_more'),
    # path('report', views.report, name='report'),
    path('report/', views.report, name='report'),
    path('report/download/<str:file_name>', views.download_file, name='download_file'),
    path('results/<int:pk>/', views.delete_result, name='delete_result'),
    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
