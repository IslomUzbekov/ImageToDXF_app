from src.utils.dxf_operations import save_to_dxf
from src.utils.image_processing import process_image


def convert_image_to_dxf(image_path, dxf_path):
    # Обработка изображения
    processed_data = process_image(image_path)

    # Сохранение в DXF
    save_to_dxf(processed_data, dxf_path)
