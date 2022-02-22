from hashlib import new
from pathlib import Path
import mimetypes

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404, HttpResponse

from .azure_file_controller import ALLOWED_EXTENTIONS, download_blob, upload_file_to_blob

from . import models


def index(request):
    return render(request, "files/index.html", {})

def upload_file(request):
    return render(request, "files/upload_file.html",{})
    # TODO
    # check request method and if Files in POST request
    # store file in variable
    # store extention in variable
    # upload file to blob and save return in a variable
    # save file metadata in DB ie (name, exttention)
    # broadcast success message
    # render template

    # TODO Later add check extension

def list_files(request):
    return render(request, "files/list_files.html",{})
    # TODO 
    # assign not deleted files in a variable
    # add to request context
    # render page

def download_file(request, file_id):
    return redirect("list_files")
    ## TODO
    ## load file metadata from DB (get)
    # save file name in a variable
    # check file type with mimetypes.guess_type
    # assign Url to variable
    # strip blob name from url
    # save blob content in a variable
    # create response instance and store data
    # return as attachment and assign file name
    # if not file content found return 404


def delete_file(request,file_id):
    pass
    # TODO
    # load file in a variable from DB
    # update deleted to  1
    # save
    # redirect to list_files
    return redirect("list_files")