from django.urls import path
from django.views.generic import ListView
from .models import videoUpload
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                path('', views.listVideo, name='VideoList'),
                path('<int:video_id>',views.playVideo, name='VideoPlayer'),
                path('search/', views.search, name='search'),
                path('upload/', views.renderAdd, name='Add'),
                path('update/<int:video_id>', views.update_video_info, name='update'),
                path('delete/<int:video_id>', views.delete_video, name='delete'),


                #path('UploadVideo/',views.uploadVideo, name='uploadVideo')
                ]
