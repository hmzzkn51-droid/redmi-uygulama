[app]

# (str) Title of your application
title = AI Master Assistant

# (str) Package name
package.name = aimasterassistant

# (str) Package domain (needed for android packaging)
package.domain = org.ai

# (str) Source directory where the main.py file is located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,db

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests,certifi,urllib3,idna,charset_normalizer

# (str) Supported orientations
orientation = portrait

# (list) List of permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API supported
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (str) Android Build Tools version (Hatanın çözümü için sabit stabil sürüm)
android.build_tools_version = 33.0.2

# (bool) Accept Android SDK licenses automatically
android.accept_sdk_license = True

# (bool) Enable Android auto backup
android.autopm = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
