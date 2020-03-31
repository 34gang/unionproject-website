from django.shortcuts import render
from pytube import YouTube
import os.path
from django.contrib import messages

def index(request):
    return render(request,'tools/templates/index.html')

def download(request):
    try:
        homedir = os.path.expanduser("~")
        dirs = homedir + '/Downloads'
        if request.method == "POST":
            url = request.POST['kualitas']
            yt = YouTube(request.POST.get('link'))
            if url == "rendah":
                try:
                    yt.streams.filter(progressive=True).get_lowest_resolution().download(homedir + '/Downloads')
                    messages.success(request, 'Video berhasil diunduh! (Kualitas Rendah)')
                except:
                    messages.error(request,'Maaf, video dengan resolusi itu tidak ditemukan')
            else:
                try:
                    yt.streams.filter(progressive=True).get_highest_resolution().download(homedir + '/Downloads')
                    messages.success(request, 'Video berhasil diunduh!')
                except:
                    messages.error(request,'Maaf Video gagal diunduh')
    except:
        messages.error(request, "Masukkan link dengan benar")

    return render(request, 'tools/templates/download.html')
