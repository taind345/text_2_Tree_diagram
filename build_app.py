import PyInstaller.__main__
import os
import shutil

# Remove existing build/dist folders if they exist
for folder in ["build", "dist"]:
    if os.path.exists(folder):
        shutil.rmtree(folder)

# Define PyInstaller arguments
args = [
    'app.py',                     # Your main script
    '--onefile',                  # Bundle into a single executable
    '--windowed',                 # Don't show terminal window
    '--name=Text2Tree',           # Name of the executable
    '--add-data=templates;templates', # Include templates directory (Windows syntax)
    '--clean',                    # Clean PyInstaller cache before building
]

# Run PyInstaller
PyInstaller.__main__.run(args)

print("\n--- Build Complete! ---")
print("Your executable is located in the 'dist' folder.")
