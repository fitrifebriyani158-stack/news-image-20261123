import os
import shutil
# Create the output directory if it does not exist
if not os.path.exists(os.environ['MAKEFUN_OUTPUT_DIR']):
    os.makedirs(os.environ['MAKEFUN_OUTPUT_DIR'])
# Copy the entry.png file
shutil.copy('entry.png', os.path.join(os.environ['MAKEFUN_OUTPUT_DIR'], 'entry.png'))
# Print a confirmation message
print("Folder created and entry.png copied")