[app]

# (str) Title of your application
title = AI Assistant App

# (str) Package name
package.name = aiassistant

# (str) Package domain (needed for android packaging)
package.domain = org.app

# (str) Source directory where the application files are located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 1.0

# (list) Application requirements (KivyMD eklendi)
requirements = python3,kivy,kivymd,requests,certifi,pip

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 34

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android NDK version
android.ndk = 25b

# (bool) Automatically accept Android SDK licenses (Hatanın sebebi olan lisans onayını çözer)
android.accept_sdk_license = True

# (bool) Use --private data storage
android.private_storage = True

# (bool) Fullscreen
fullscreen = False

# (bool) AndroidX support
android.enable_androidx = True

# (str) Automatic versionCode generation
android.numeric_version = 1

# (bool) Skip byte-compiling python files
android.skip_bytecompile = False

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
