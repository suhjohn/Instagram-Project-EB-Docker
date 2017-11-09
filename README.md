# Instagram

## Requirements

Refer to the requirements.txt 

After cloning the repository, run the following command to install all the necessary 
dependencies:

```
pip install -r requirements.txt
```

## Secret config JSON FILES

Files have been ommitted for security reasons. When cloning the project to test, it is required that you create your 
own DB for local use. Refer to the official Postgresql Guide on this issue. 

`.config-secret/settings_common.json`

```
{
    "django":{
        "secret_key": "<Django secret key value>",
        "databases": {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "HOST": "<insert host name>",
                "PORT": "<insert port number: default is 5432>",
                "NAME": "<insert name of db>",
                "USER": "<insert username>",
                "PASSWORD": "<insert password>"
            }
        }
    }
}
```

## Techniques Used

- Username & Email Validation on Login
- Facebook Login authentication & validation from backend
- Image Editing (Coming soon)
- Tag / User Search (Coming soon)
- Unlimited Scrolling with Ajax (Coming soon)
