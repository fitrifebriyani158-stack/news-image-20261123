import os
import shutil
if not os.path.exists(os.environ['MAKEFUN_OUTPUT_DIR']):
    os.makedirs(os.environ['MAKEFUN_OUTPUT_DIR'])
shutil.copy('entry.png', os.path.join(os.environ['MAKEFUN_OUTPUT_DIR'], 'entry.png'))
print('copy done')