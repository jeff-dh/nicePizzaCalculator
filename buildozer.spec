[app]

# (str) Title of your application
title = nicePizzaCalculator

# (str) Package name
package.name = nicePizzaCalculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.pizza

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
# source.include_exts = py,png,jpg,kv,atlas,svg

# include all files (at least svg & html is required, probably more....)
# this is neccessary since we need the patched nicegui library from ./nicegui
# since we still need nicegui as requirement (otherwise we're missing 'package
# metadata') the apk file is huge for now o_O
source.include_exts =

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,urllib3,httpcore,bidict,Jinja2,vbuild,simple-websocket,aiohttp,yarl,frozenlist,httpx,uvicorn,sniffio,requests,wsproto,propcache,python-socketio,charset-normalizer,idna,anyio,annotated-types,certifi,orjson,itsdangerous,pydantic_core,ifaddr,python-engineio,multidict,click,h11,MarkupSafe,starlette,aiofiles,aiosignal,attrs,fastapi,Pygments,markdown2,python-multipart,pscript,typing_extensions,docutils,pydantic,typing-inspection,watchfiles,aiohappyeyeballs,wait_for2,nicegui

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoptions/#build-options-1 for all the supported syntaxes and properties)
android.permissions = android.permission.INTERNET, (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18)

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
# android.archs = arm64-v8a, armeabi-v7a
android.archs = arm64-v8a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) Bootstrap to use for android builds
p4a.bootstrap = webview

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
p4a.port = 8080

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

