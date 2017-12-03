import os
import argparse
from PIL import Image


def create_parser():
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
                 new_height):

    width_original, height_original = original_image.size
    if new_width and new_height:
        if width_original / height_original != new_width / new_height:
            print('***The proportions do not match the original image.***')
        new_size = (new_width, new_height)
    elif new_width:
        height = int(new_width * height_original / width_original)
        new_size = (new_width, height)
    elif new_height:
        width = int(new_height * width_original / height_original)
        new_size = (width, new_height)
    return new_size


def get_new_scale_size(original_image, scale):
    return [round(scale * size) for size in original_image.size]


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
    parser = create_parser()
    namespace = parser.parse_args()

    image = get_image(namespace.image)

    if namespace.scale and (namespace.width or namespace.height):
        raise RuntimeError('You must use scale without width or height!')
    elif not namespace.scale and not namespace.width and not namespace.height:
        raise RuntimeError('Width or height or scale required!')
    elif namespace.scale:
        new_size = get_new_scale_size(image, namespace.scale)
    else:
        new_size = get_new_size(image,
                                namespace.width,
                                namespace.height)

    resized_image = resize_image(image, new_size)

    chosen_path_to_result = chose_path_to_result(
        namespace.output, namespace.image, resized_image)

    save_image(resized_image, chosen_path_to_result)
