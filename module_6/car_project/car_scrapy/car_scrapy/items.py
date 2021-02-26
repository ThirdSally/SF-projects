# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CarItem(Item):
    # define the fields for your item here like:
    bodyType = Field()
    brand = Field()
    car_url = Field()
    color = Field()
    complectation_dict = Field()
    description = Field()
    engineDisplacement = Field()
    enginePower = Field()
    equipment_dict = Field()
    fuelType = Field()
    image = Field()
    mileage = Field()
    modelDate = Field()
    model_info = Field()
    model_name = Field()
    name = Field()
    numberOfDoors = Field()
    priceCurrency = Field()
    productionDate = Field()
    sell_id = Field()
    super_gen = Field()
    vehicleConfiguration = Field()
    vehicleTransmission = Field()
    vendor = Field()
    Владельцы = Field()
    Владение = Field()
    ПТС = Field()
    Привод = Field()
    Руль = Field()
    Состояние = Field()
    Таможня = Field()
    price = Field()
