[app]
# (str) Title of your application
title = Standoff2Cheats

# (str) Application versioning (required)
version = 0.1

# (str) Package name
package.name = standoff2cheats

# (str) Package domain (needed for android)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Icon of the application
icon.filename = icon.png

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Supported orientation
orientation = portrait

# (str) Android API level
android.api = 33

# (str) Android minimum API
android.minapi = 21

# (str) Android SDK version
android.sdk = 33

# (str) Android NDK version
android.ndk = 25b

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (list) Pattern to whitelist for the whole project
# whitelist = 

# (bool) Use debug mode
debug = 1

# (int) Request code for android activity
android.request_permissions = True
