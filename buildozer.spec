[app]

title = AI Assistant App
package.name = aiassistant
package.domain = org.app

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0
requirements = python3,kivy,requests,certifi,pip

orientation = portrait

[app:android]
permissions = INTERNET

android.api = 34
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 34.0.0

android.private_storage = True
fullscreen = False
android.enable_androidx = True
android.numeric_version = 1
android.skip_bytecompile = False

[buildozer]
log_level = 2
warn_on_root = 1
