## Example of uploading/downloading file to azure storage using Django backend

### **Why would you want to store in a Blob storage or Object Storage instead of in your back-end server?**

Django offer a facility to conveniently store files in the server in a folder
however, I always prefer to store this in an object store or the cloud blob storage (Binary Large Object Storage) for a few reasons

- Cheaper
- Portability
- Scalability

Then I keep only in the application the metadata of the files and also never "hard" delete them but do a simple "soft" delete

### Setup

To set up the project you will need to

1. Clone this repository

move to a folder in your computer and then clone it by

`git clone https://github.com/pedrojunqueira/django-file_manager.git`

then move into the code directory

`cd django-file_manager`

2. Create and activate a Python virtual environment

Create by the following command

`python3 -m venv .venv`

Activate by the following command (for mac and unix)

`source .venv/bin/activate`

3.Install dependencies

`pip install -r requirements.txt`

4. Set up environment variables for your azure subscription

if you use bash shell then you can just paste the following in your `.bash_profile` file

It is located in your user root directory `~/.bash_profile`

```bash
export AZURE_TENANT_ID=<tenant_id>
export AZURE_CLIENT_ID=<client-id>
export AZURE_CLIENT_SECRET=<client-secret>
export AZURE_SUBSCRIPTION_ID=<subscription-id>
```

on the above put your credentials on the placeholders in between angle brackets.

If you use zsh then you need to past on your `~/.zshenv`

but there just do not use the word export

```zsh
AZURE_TENANT_ID=<tenant_id>
AZURE_CLIENT_ID=<client-id>
AZURE_CLIENT_SECRET=<client-secret>
AZURE_SUBSCRIPTION_ID=<subscription-id>
```

to understand this better you can access this excellent resource in YouTube [SigmaCode channel](https://www.youtube.com/watch?v=PjOjrIZOetM)

5. Set up environment variable to your django application

create a .env file with the following key value pairs and include your configuration

```text
AZURE_STORAGE_ACCOUNT=https://<your storage account>.blob.core.windows.net
AZURE_VAULT_ACCOUNT=https://<your key vault>.vault.azure.net/
AZURE_STORAGE_KEY_NAME=<storage-key>
AZURE_APP_BLOB_NAME=files

```

make sure this file is save on the following directory from the root directory

`./django-file-upload/website/website/.env`

6. Migrate database and models

`python3 manage.py makemigrations`

`python3 manage.py migrate`

You should see output like that

```python
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

migrate files app model

`python3 manage.py makemigrations files`

`python3 manage.py migrate files`

output

```python
Operations to perform:
  Apply all migrations: files
Running migrations:
  Applying files.0001_initial... OK
```

### Start you app

Once you you complete all the set up above you are good to go.

You just need to start you Django development server

navigate to the folder `website`

`cd website`

then start the server by

`python3 manage.py runserver`

open you browser on `http://127.0.0.1:8000/`

congrats !!!

### Resources

#### Django documentation

- [file uploads](https://docs.djangoproject.com/en/4.0/topics/http/file-uploads/)

#### Azure Storage Python SDK

- [blob_client](https://docs.microsoft.com/en-us/azure/developer/python/sdk/storage/azure-storage-blob/azure.storage.blob.blobclient?view=storage-py-v12)
- [blob_client.upload_blob](https://docs.microsoft.com/en-us/azure/developer/python/sdk/storage/azure-storage-blob/azure.storage.blob.blobclient?view=storage-py-v12#upload-blob-data--blob-type--blobtype-blockblob---blockblob----length-none--metadata-none----kwargs-)
- [blob_client.download_blob](https://docs.microsoft.com/en-us/azure/developer/python/sdk/storage/azure-storage-blob/azure.storage.blob.blobclient?view=storage-py-v12#download-blob-offset-none--length-none----kwargs-)
