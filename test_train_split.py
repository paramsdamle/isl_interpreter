from pathlib import Path
import os
import random
import shutil

test_fraction = 0.1
source = 'Data/'

filenames = os.listdir(source)
without_extensions = set([Path(name).stem for name in filenames])

for name in without_extensions:
  destination = 'Tensorflow/workspace/images/train/'
  if random.random() < test_fraction:
    destination = 'Tensorflow/workspace/images/test/'

  # Copy the files
  shutil.copy(source + name + '.xml', destination + name + '.xml')
  shutil.copy(source + name + '.jpg', destination + name + '.jpg')
