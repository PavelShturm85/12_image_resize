import os
import argparse
from PIL import Image


def createParser():
        parser = argparse.ArgumentParser(
            description='Module for resize image.')
        parser.add_argument(
            'image', help='Where get the image.')
        parser.add_argument(
            '-w', '--width', type=int, help='Input new width image.')
        parser.add_argument(
            '-he', '--height', type=int, help='Input new height image.')
        parser.add_argument(
            '-sc', '--scale', type=float, help='Input how scale image.')
        parser.add_argument(
            '-out', '--output', help='Where to put the image.')
        return parser


def get_image(path_to_original):
    return Image.open(path_to_original)


def get_new_size(original_image,
                 new_width,
                 new_height,
                 scale):

    width_original, height_original = original_image.size
    if new_width and new_height and scale:
        raise RuntimeError('You must use scale without width or height!')
    elif new_width and new_height:
        if width_original / height_original != new_width / new_height:
            print('***The proportions do not match the original image.***')
        new_size = (new_width, new_height)
    elif new_width:
        height = int(new_width * height_original / width_original)
        new_size = (new_width, height)
    elif new_height:
        width = int(new_height * width_original / height_original)
        new_size = (width, new_height)
    elif scale:
        new_size = [round(scale * s) for s in original_image.size]
    else:
        raise RuntimeError('Width or height or scale required!')
    return new_size


def resize_image(original_image, new_size):
    return original_image.resize(new_size, Image.ANTIALIAS)


def chose_path_to_result(path_to_result, path_to_original, resized_image):
    if path_to_result:
        return path_to_result
    else:
        name_file, file_extension = os.path.splitext(path_to_original)

        created_path = '{}__{}x{}{}'.format(
            name_file,
            *resized_image.size,
            file_extension)
        return created_path


def save_image(resized_image, path_to_result):
    resized_image.save(path_to_result)


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    path_to_original = namespace.image
    path_to_result = namespace.output
    image = get_image(path_to_original)
    new_size = get_new_size(image,
                            namespace.width,
                            namespace.height,
                            namespace.scale)

    resized_image = resize_image(image, new_size)

    chosen_path_to_result = chose_path_to_result(
        path_to_result, path_to_original, resized_image)

    save_image(resized_image, chosen_path_to_result)
