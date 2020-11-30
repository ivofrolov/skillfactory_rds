# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CarSpecification(Item):
    title = Field()
    rating = Field()
    reviews = Field()
    brand = Field()
    model = Field()
    generation = Field()
    body_type = Field()
    engine_type = Field()
    modification = Field()
    engine_volume = Field()
    fuel = Field()
    engine_power = Field()
    wheel_drive = Field()
    transmission = Field()
    acceleration = Field()
    fuel_consumption = Field()
    brand_country = Field()
    grade = Field()
    doors = Field()
    seats = Field()
    length = Field()
    width = Field()
    height = Field()
    wheel_base = Field()
    clearance = Field()
    front_track_width = Field()
    rear_track_width = Field()
    wheel_size = Field()
    trunk_capacity = Field()
    fuel_tank_capacity = Field()
    curb_weight = Field()
    total_weight = Field()
    gears = Field()
    front_suspension_type = Field()
    rear_suspension_type = Field()
    front_brake = Field()
    rear_brake = Field()
    max_speed = Field()
    eco_class = Field()
    engine_layout = Field()
    boost_type = Field()
    torque = Field()
    cylinders_layout = Field()
    cylinders = Field()
    valves_per_cylinder = Field()
    compression_ratio = Field()
    cylinder_diameter_stroke = Field()
