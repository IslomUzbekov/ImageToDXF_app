import os


def file_exists(file_path):
    """
    Проверяет, существует ли указанный файл.
    """
    return os.path.isfile(file_path)


def create_directory_if_not_exists(directory_path):
    """
    Создает указанную директорию, если она не существует.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def get_file_extension(file_path):
    """
    Возвращает расширение файла.
    """
    return os.path.splitext(file_path)[1]


def is_valid_image_file(file_path):
    """
    Проверяет, является ли файл изображением, основываясь на его расширении.
    """
    valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp']
    return get_file_extension(file_path).lower() in valid_extensions


def is_valid_dxf_file(file_path):
    """
    Проверяет, является ли файл DXF файлом, основываясь на его расширении.
    """
    return get_file_extension(file_path).lower() == '.dxf'


def get_filename_without_extension(file_path):
    """
    Возвращает имя файла без расширения.
    """
    return os.path.splitext(os.path.basename(file_path))[0]


def get_directory_path(file_path):
    """
    Возвращает директорию файла.
    """
    return os.path.dirname(file_path)
