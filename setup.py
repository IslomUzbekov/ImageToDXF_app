from setuptools import find_packages, setup

# Чтение файла README.md для использования в long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ImageToDXF",
    version="0.1.0",
    author="Islom",
    author_email="uzbekov32@mail.ru",
    description="Приложения для конвертации картинки в dxf файл.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IslomUzbekov/ImageToDXF",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "Pillow",    # Для обработки изображений
        "ezdxf",     # Для работы с DXF файлами
    ],
    entry_points={
        'console_scripts': [
            'image_to_dxf=image_to_dxf.main:main',
        ],
    },
)
