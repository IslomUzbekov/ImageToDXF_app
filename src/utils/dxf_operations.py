import ezdxf


def save_to_dxf(processed_data, dxf_path):
    # Создаем новый DXF документ
    doc = ezdxf.new('R2010', setup=True)
    msp = doc.modelspace()

    # Пример добавления данных в DXF
    msp.add_line((0, 0), (10, 0))

    # Сохраняем документ
    doc.saveas(dxf_path)
