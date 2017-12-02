# Image Resizer

**This module resize image.**

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

*Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.*

```bash
pip install -r requirements.txt # alternatively try pip3
```

# Quickstart
**Ways to use:**
*- Have to use  module `image_resize.py` after `python3`, with `arguments`.*
   - You must use `scale` without `width` or `height`!
   - You must enter `width` or `height` or `scale` how argument!
   - You may use `width` and `height`, but you may get message:
   `***The proportions do not match the original image.***`


Example of script launch on Linux, Python 3.5:

```bash
$ python3 image_resize.py -h
usage: image_resize.py [-h] [-w WIDTH] [-he HEIGHT] [-sc SCALE] [-out OUTPUT]
                       image

Module for resize image.

positional arguments:
  image                 Where get the image.

optional arguments:
  -h, --help            show this help message and exit

  -w WIDTH, --width WIDTH           Input new width image.

  -he HEIGHT, --height HEIGHT       Input new height image.

  -sc SCALE, --scale SCALE Input    how scale image.

  -out OUTPUT, --output OUTPUT      Where to put the image.

```
**RuntimeError example:**

```bash
$ python3 image_resize.py panda.jpg

Traceback (most recent call last):
  File "image_resize.py", line 71, in <module>
    namespace.scale)
  File "image_resize.py", line 42, in get_new_size
    raise RuntimeError('Width or height or scale required!')
RuntimeError: Width or height or scale required!
```

```bash
python3 image_resize.py panda.jpg -w 900 -he 700 -sc 2
Traceback (most recent call last):
  File "image_resize.py", line 75, in <module>
    namespace.scale)
  File "image_resize.py", line 32, in get_new_size
    raise RuntimeError('You must use scale without width or height!')
RuntimeError: You must use scale without width or height!

```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
