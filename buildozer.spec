[app]

# (str) Title of your application
title = AI Master Assistant

# (str) Package name
package.name = aimasterassistant

# (str) Package domain (needed for android packaging)
package.domain = org.ai

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas,json,db

# (list) List of inclusion/exclusion patterns
source.include_patterns = assets/*,images/*.png

# (str) Application versioning
version = 1.0

# (list) Application requirements
# Asla python kodu içermez, sadece paket adları virgülle ayrılır:
requirements = python3,kivy,requests,certifi,urllib3,idna,charset_normalizer

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (list) List of permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Enable Android auto backup
android.autopm = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
