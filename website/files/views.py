# from pathlib import Path
# import mimetypes

from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.http import Http404, HttpResponse

# from .azure_file_controller import upload_file_to_blob, download_blob



def index(request):
    return render(request, "files/index.html", {})

def upload_file(request):
    return render(request, "files/upload_file.html", {})

def list_files(request):
    return render(request, "files/list_files.html", {})

def download_file(request, file_id):
    pass

def delete_file(request,file_id):
    return redirect("list_files")