from PIL import Image


def process_image(image_path):
    # Открываем изображение и преобразуем его в необходимый формат
    with Image.open(image_path) as img:
        # Выполняем необходимые операции
        processed_data = img.convert("L")
    return processed_data
