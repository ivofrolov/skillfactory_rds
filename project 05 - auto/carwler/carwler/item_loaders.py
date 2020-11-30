# Define here specific loaders for your models
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/loaders.html

from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, Compose, TakeFirst


def select_spec(spec_list, loader_context):
    label = loader_context.get('label')
    if not label:
        return None
    for name, value in zip(spec_list[::2], spec_list[1::2]):
        if name == label:
            return value
    return None


class AutoruCarSpecLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()

    brand_country_in = Compose(select_spec, label='Страна марки')
    grade_in = Compose(select_spec, label='Класс автомобиля')
    doors_count_in = Compose(select_spec, label='Количество дверей')
    seats_count_in = Compose(select_spec, label='Количество мест')
    length_in = Compose(select_spec, label='Длина')
    width_in = Compose(select_spec, label='Ширина')
    height_in = Compose(select_spec, label='Высота')
    wheel_base_in = Compose(select_spec, label='Колёсная база')
    clearance_in = Compose(select_spec, label='Клиренс')
    front_track_width_in = Compose(select_spec, label='Ширина передней колеи')
    rear_track_width_in = Compose(select_spec, label='Ширина задней колеи')
    wheel_size_in = Compose(select_spec, label='Размер колёс')
    trunk_capacity_in = Compose(select_spec, label='Объем багажника мин/макс, л')
    fuel_tank_capacity_in = Compose(select_spec, label='Объём топливного бака, л')
    curb_weight_in = Compose(select_spec, label='Снаряженная масса, кг')
    total_weight_in = Compose(select_spec, label='Полная масса, кг')
    transmission_type_in = Compose(select_spec, label='Коробка передач')
    gears_count_in = Compose(select_spec, label='Количество передач')
    wheel_drive_in = Compose(select_spec, label='Тип привода')
    front_suspension_type_in = Compose(select_spec, label='Тип передней подвески')
    rear_suspension_type_in = Compose(select_spec, label='Тип задней подвески')
    front_brake_type_in = Compose(select_spec, label='Передние тормоза')
    rear_brake_type_in = Compose(select_spec, label='Задние тормоза')
    max_speed_in = Compose(select_spec, label='Максимальная скорость, км/ч')
    acceleration_in = Compose(select_spec, label='Разгон до 100 км/ч, с')
    fuel_consumption_in = Compose(select_spec, label='Расход топлива, л город/трасса/смешанный')
    fuel_type_in = Compose(select_spec, label='Марка топлива')
    eco_class_in = Compose(select_spec, label='Экологический класс')
    engine_type_in = Compose(select_spec, label='Тип двигателя')
    engine_layout_in = Compose(select_spec, label='Расположение двигателя')
    engine_volume_in = Compose(select_spec, label='Объем двигателя, см³')
    boost_type_in = Compose(select_spec, label='Тип наддува')
    engine_power_in = Compose(select_spec, label='Максимальная мощность, л.с./кВт при об/мин')
    torque_in = Compose(select_spec, label='Максимальный крутящий момент, Н*м при об/мин')
    cylinders_layout_in = Compose(select_spec, label='Расположение цилиндров')
    cylinders_count_in = Compose(select_spec, label='Количество цилиндров')
    valves_per_cylinder_in = Compose(select_spec, label='Число клапанов на цилиндр')
    compression_ratio_in = Compose(select_spec, label='Степень сжатия')
    cylinder_spec_in = Compose(select_spec, label='Диаметр цилиндра и ход поршня, мм')
