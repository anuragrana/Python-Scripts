#
# Script to perform the basic setup tasks in Django Project
# Author - Anurag Rana
# Homepage - anuragrana.in
#

import os
import sys
import urllib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_NAME = BASE_DIR.split("/")[-1]
ENV_FILE = "this_is_dev_env"


def usage():
    msg = """
    This script automate the mundane tasks of setting up a django project.
    usage : python setup.py <action> [param]
    Action can take below values:
    ip : initiate project. Initialize git in project directory. create gitignore file. Add paths to gitignore file.
         creates the environment specific settings files. etc.
         {python setup.py ip}
    ca : create app. needs appname as another argument. Creates the app. creates the directories and init file in them.
         {python setup.py ca appname}

    """
    print(msg)


def create_logger_settings():
    try:
        link = "https://gist.githubusercontent.com/anuragrana/151129fb715980dfdef52ca464825087/raw/f12d3f48c32759b36c8e1c73eec37d378e9dfb8b/logger_settings.py"
        f = urllib.request.request(link)
        myfile = f.read()

        with open(PROJECT_NAME+"/settings.py", 'a+') as fh:
            fh.write("\n"+myfile)
            fh.write("\n\n")

    except Exception as e:
        print(e)


def create_gitignore():
    gitignore = '.gitignore'
    try:
        with open(gitignore, 'a+') as fh:
            fh.write("./logs\n")
            fh.write("./static\n")
            fh.write("./media\n")
            fh.write("**/*.pyc\n")
            fh.write("**/migrations/*\n")
            # because we will not commit prod setting file. Copy securely.
            fh.write(PROJECT_NAME + "/settings_prod.py\n")
            fh.write(PROJECT_NAME + "/" + ENV_FILE + "\n")
    except Exception as e:
        print(e)


def update_settings():
    f = open(PROJECT_NAME+"/settings.py", "r")
    contents = f.readlines()
    f.close()

    index = 0

    for l in contents:
        if "ALLOWED_HOSTS" in l:
            index = contents.index(l)
            break

    msg = "\n\nif os.path.isfile(os.path.join(BASE_DIR,'"+ENV_FILE+"')):\n\tfrom .settings_dev import *"
    msg += "\nelse:\n\tfrom .settings_prod import *\n\n"

    contents.insert(index+1, msg)

    f = open(PROJECT_NAME+"/settings.py", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

    # add static and media root and urls
    with open(PROJECT_NAME + "/settings.py", "a+") as fh:
        fh.write("STATIC_ROOT = os.path.join(BASE_DIR, \"static/\")\n")
        fh.write("MEDIA_ROOT = os.path.join(BASE_DIR,\"media/\")\n")
        fh.write("MEDIA_URL = \"/media/\"\n")


def create_env_settings_files():
    try:
        with open(PROJECT_NAME + "/settings_prod.py", 'w') as fh:
            fh.write("DEBUG = False\n")
            fh.write('ALLOWED_HOSTS = ["*"]')

        with open(PROJECT_NAME + "/settings_dev.py", 'w') as fh:
            fh.write("DEBUG = True\n")
            fh.write('ALLOWED_HOSTS = []')
    except Exception as e:
        print(e)


def update_project_urls_file():
    try:
        with open(PROJECT_NAME + "/urls.py", 'a+') as fh:
            fh.write("\n\nfrom django.conf.urls import include\n")
            fh.write("from django.conf.urls import handler404, handler500\n")
            fh.write("from django.conf import settings\n")
            fh.write("from django.conf.urls.static import static\n\n")
            fh.write("urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n\n")
            fh.write("#handler404 = views.error_404\n")
            fh.write("#handler500 = views.error_500\n\n")

    except Exception as e:
        print(e)


def init_project():
    print("Initializing the project...")

    print("Current working directory: " + BASE_DIR)
    print("Name of Project: " + PROJECT_NAME)

    print("Initializing git... ")
    os.system("git init")

    print("Creating Environment identification file.")
    os.system("touch "+PROJECT_NAME+"/"+ENV_FILE)

    print("creating .gitignore file...")
    create_gitignore()

    print("creating different local and prod environment setting files...")
    create_env_settings_files()
    update_settings()

    print("Creating logs directory...")
    os.system("mkdir logs")

    print("Updating project URL file...")
    update_project_urls_file()

    create_logger_settings()

    msg = """
    Project has been initialized. Please look into your settings files and update the settings accordingly.
    """
    print(msg)


def update_project_urls_file_with_app_url(appname):
    try:
        with open(PROJECT_NAME + "/urls.py", 'a+') as fh:
            fh.write("urlpatterns += [\n")
            fh.write("    url(r'^"+appname+"/', include('"+appname+".urls', namespace='"+appname+"')),\n")
            fh.write("]")

    except Exception as e:
        print(e)


def create_app_urls(appname):
    try:
        with open(appname + "/urls.py", 'a+') as fh:
            fh.write("from django.conf.urls import url\n")
            fh.write("from "+appname+" import views\n")
    except Exception as e:
        print(e)


def create_app():
    if len(sys.argv) < 3:
        print("\nERROR: Please mention the name of app as well\n\n")
        usage()
        sys.exit(1)
    appname = sys.argv[2]
    print("Creating new app '" + appname + "' ...")
    os.system("python manage.py startapp " + appname)

    print("creating app URLs file")
    create_app_urls(appname)

    print("updating project URL file")
    update_project_urls_file_with_app_url(appname)

    list_dirs = ["models", "views", "forms", "services", "utilities", "templatetags"]

    for directory in list_dirs:
        print("Creating " + directory + " directory...")
        os.system("mkdir " + appname + "/" + directory)
        os.system("touch " + appname + "/" + directory + "/__init__.py")

    print("Creating templates directory...")
    os.system("mkdir -p " + appname + "/templates/" + appname + "/")

    print("Creating static directory...")
    list_static_dirs = ["img", "css", "js"]
    for directory in list_static_dirs:
        os.system("mkdir -p " + appname + "/static/" + appname + "/"+directory)

    print("Renaming unnecessary files...")
    os.rename(appname + "/views.py", appname + "/views.py.backup")
    os.rename(appname + "/models.py", appname + "/models.py.backup")


def start():
    action = sys.argv[1]

    if "ip" == action:
        # ip - initialize project
        init_project()
    elif "ca" == action:
        # ca - create app
        create_app()
    elif "help" == action:
        # help - show usage
        usage()


start()
