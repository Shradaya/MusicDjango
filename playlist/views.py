from django.shortcuts import render
from .models import videoUpload, Order
from urllib.parse import urlparse
import random
from django.db import connection
from .forms import PostForm
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        videos =  videoUpload.objects.filter(Title__icontains=q)
        list_of_bought_videos = authvid(request)
        return render(request, 'playlist/creations.html', {'videos':videos,"list_of_bought_videos":list_of_bought_videos})
    else:
        return HttpResponse('Please submit a search term.')

def authvid(request):
    list_videos = []
    auth_videos = Order.objects.filter(userID=request.user.id)
    auth_videos = list(auth_videos.values_list())
    length = len(auth_videos)
    if length!=0:
        for i in range(length):
            list_videos.append(int(auth_videos[i][2]))
    return list_videos




def playVideo(request, video_id):
    video_id = int(video_id)
    video = videoUpload.objects.get(id=video_id)
    videos = videoUpload.objects.exclude(id=video_id)[:10]
    list_of_bought_videos = authvid(request)
    try:
        orderid = int(Order.objects.latest('orderID'))
        orderid+=1
    except:
        orderid=1
    return render(request, 'playlist/play.html',{"video":video, "videos":videos, "list_of_bought_videos":list_of_bought_videos,"orderid":orderid})

def listVideo(request):
    videos = videoUpload.objects.all()
    list_of_bought_videos = authvid(request)
    return render(request, 'playlist/creations.html', {"videos":videos, "list_of_bought_videos":list_of_bought_videos} )

def renderAdd(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/videos/')
    else:
        form = PostForm()
    if request.user.is_authenticated:
        return render(request, 'playlist/UploadUpdate.html', {"form": form })
    else:
        return render(request, '/videos/')

def update_video_info(request, video_id):
    video_id = int(video_id)
    try:
        video_sel = videoUpload.objects.get(id = video_id)
    except uploadVideo.DoesNotExist:
        return render(request, 'home.html')
    video_form = PostForm(request.POST or None, request.FILES, instance = video_sel)
    if video_form.is_valid():
       video_form.save()
       return redirect('/videos/')
    if request.user.is_authenticated:
        return render(request, 'playlist/UploadUpdate.html', {"form": video_form })
    else:
        return render(request, '/videos/')


def delete_video(request, video_id):
    video_id = int(video_id)
    try:
        video_grp = videoUpload.objects.get(id = video_id)
    except videoUploads.DoesNotExist:
        return render(request, 'Home/error.html')
    if request.user.has_perm("playlist.delete_posting"):
        video_grp.delete()
        messages.success(request, 'Video Deleted Successfully')
        return redirect('/videos/')
    else:
        messages.success(request, "You are not Authorized to perform delete operation")
        return redirect('/videos/')
