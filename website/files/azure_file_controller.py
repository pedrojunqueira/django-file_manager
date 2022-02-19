# import uuid
# from pathlib import Path
# from io import BytesIO

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobClient
from django.conf import settings

# from . import models

def create_blob_client(file_name):

    default_credential = DefaultAzureCredential()

    secret_client = SecretClient(
        vault_url=settings.AZURE_VAULT_ACCOUNT, credential=default_credential
    )

    storage_credentials = secret_client.get_secret(name="storage-key")

    return BlobClient(
        account_url=settings.AZURE_STORAGE_ACCOUNT,
        container_name=settings.AZURE_APP_BLOB_NAME,
        blob_name=file_name,
        credential=storage_credentials.value,
    )


def check_file_ext(path):
    pass

def download_blob(file):
    pass


def save_file_url_to_db(file_url):
    pass

def upload_file_to_blob(file):
    pass