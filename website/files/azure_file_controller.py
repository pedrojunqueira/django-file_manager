from io import BytesIO
import uuid
from pathlib import Path

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobClient
from django.conf import settings

from . import models


ALLOWED_EXTENTIONS = ['.pdf','.doc','.docx']

def create_blob_client(file_name):

    default_credential = DefaultAzureCredential()

    secret_client = SecretClient(
        vault_url=settings.AZURE_VAULT_ACCOUNT, credential=default_credential
    )

    storage_credentials = secret_client.get_secret(name=settings.AZURE_STORAGE_KEY_NAME)

    return BlobClient(
        account_url=settings.AZURE_STORAGE_ACCOUNT,
        container_name=settings.AZURE_APP_BLOB_NAME,
        blob_name=file_name,
        credential=storage_credentials.value,
    )


def check_file_ext(path):
    pass
    # TODO 
    # extract extention
    # check if extention is in allowed extensions
    # if yes return True


def download_blob(file):
    pass
    # TODO
    # instantiate blob client
    # check if blob does not exist and return
    # download blob contant in a variable and return
    

def save_file_url_to_db(file_url):
    pass
    # TODO 
    # create new file object in db and save blob irl
    # return new file

def upload_file_to_blob(file):
    pass
    # TODO
    # create file name with prefix and extension
    # store file content in a variable
    # create BitesIO Object
    # Instantiate blob client
    # upload data to blob
    # save url in DB
    # return file Object

    # later add check file extension
