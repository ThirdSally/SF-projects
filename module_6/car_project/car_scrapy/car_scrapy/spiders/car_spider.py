import scrapy

from scrapy.spiders import Spider
from scrapy.crawler import CrawlerProcess

import json

from ..items import CarItem


class Car_Spider(Spider):

    name = 'car_spider'
    allowed_domains = ['auto.ru']


    start_urls = [
            'https://auto.ru/moskva/cars/audi/used/',
            'https://auto.ru/moskva/cars/bmw/used/',
            'https://auto.ru/moskva/cars/chevrolet/used/',
            'https://auto.ru/moskva/cars/citroen/used/',
            'https://auto.ru/moskva/cars/honda/used/',
            'https://auto.ru/moskva/cars/hyundai/used/',
            'https://auto.ru/moskva/cars/infiniti/used/',
            'https://auto.ru/moskva/cars/kia/used/',
            'https://auto.ru/moskva/cars/land_rover/used/',
            'https://auto.ru/moskva/cars/lexus/used/',
            'https://auto.ru/moskva/cars/mazda/used/',
            'https://auto.ru/moskva/cars/mercedes/used/',
            'https://auto.ru/moskva/cars/mitsubishi/used/',
            'https://auto.ru/moskva/cars/nissan/used/',
            'https://auto.ru/moskva/cars/opel/used/',
            'https://auto.ru/moskva/cars/peugeot/used/',
            'https://auto.ru/moskva/cars/porsche/used/',
            'https://auto.ru/moskva/cars/renault/used/',
            'https://auto.ru/moskva/cars/skoda/used/',
            'https://auto.ru/moskva/cars/ssang_yong/used/',
            'https://auto.ru/moskva/cars/toyota/used/',
            'https://auto.ru/moskva/cars/volkswagen/used/',
            'https://auto.ru/moskva/cars/volvo/used/',
        ]


    def parse(self, response):

        car_links = response.xpath('//a[@class="Link ListingItemTitle-module__link"]/@href')
        links_to_follow = car_links.extract()

        for url in links_to_follow:
            yield response.follow(url=url, callback=self.parse_pages)

        next_page = response.css('.ListingPagination-module__next').xpath('@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)

    def parse_pages(self, response):

        car = CarItem()

        main_content = response.xpath('//script[@type="application/ld+json"]/text()').extract_first()
        main_data = json.loads(main_content)

        bodyType = main_data['bodyType']
        brand = main_data['brand']
        car_url = main_data['offers']['url']
        color = main_data['color']
        description = main_data['description']
        engineDisplacement = main_data['vehicleEngine']['engineDisplacement']
        enginePower = main_data['vehicleEngine']['enginePower']
        fuelType = main_data['fuelType']
        image = main_data['image']
        modelDate = main_data['modelDate']
        numberOfDoors = main_data['numberOfDoors']
        priceCurrency = main_data['offers']['priceCurrency']
        productionDate = main_data['productionDate']
        vehicleConfiguration = main_data['vehicleConfiguration']
        vehicleTransmission = main_data['vehicleTransmission']
        price = main_data['offers']['price']

        ownersCount = response.xpath(
            '//li[@class="CardInfoRow CardInfoRow_ownersCount"]/span[@class="CardInfoRow__cell"]/text()').extract()
        owningTime = response.xpath(
            '//li[@class="CardInfoRow CardInfoRow_owningTime"]/span[@class="CardInfoRow__cell"]/text()').extract()
        passport = response.xpath(
            '//li[@class="CardInfoRow CardInfoRow_pts"]/span[@class="CardInfoRow__cell"]/text()').extract()
        drive = response.xpath(
            '//li[@class="CardInfoRow CardInfoRow_drive"]/span[@class="CardInfoRow__cell"]/text()').extract()
        steer_wheel = response.xpath(
            '//li[@class="CardInfoRow CardInfoRow_wheel"]/span[@class="CardInfoRow__cell"]/text()').extract()
        condition = response.xpath(
            '//li[@class="CardInfoRow CardInfoRow_state"]/span[@class="CardInfoRow__cell"]/text()').extract()
        customs = response.xpath(
            '//li[@class="CardInfoRow CardInfoRow_customs"]/span[@class="CardInfoRow__cell"]/text()').extract()

        sell_id = response.xpath('//div[@title="Идентификатор объявления"]/text()').re(r'\d+')

        dict_data = json.loads(response.xpath('//script[@id="initial-state"]/text()').extract_first())

        complectation = dict_data['card']['vehicle_info']['complectation']
        complectation_dict = dict(list(complectation.items())[0:3])
        equipment_dict = dict_data['card']['vehicle_info']['equipment']
        mileage = dict_data['card']['state']['mileage']
        model_info = dict_data['card']['vehicle_info']['model_info']
        model_name = model_info['name']
        super_gen = dict_data['card']['vehicle_info']['tech_param']
        name = super_gen['human_name']
        vendor = dict_data['card']['vehicle_info']['vendor']

        car['bodyType'] = bodyType
        car['brand'] = brand
        car['car_url'] = car_url
        car['color'] = color
        car['complectation_dict'] = complectation_dict
        car['description'] = description
        car['engineDisplacement'] = engineDisplacement
        car['enginePower'] = enginePower
        car['equipment_dict'] = equipment_dict
        car['fuelType'] = fuelType
        car['image'] = image
        car['mileage'] = mileage
        car['modelDate'] = modelDate
        car['model_info'] = model_info
        car['model_name'] = model_name
        car['name'] = name
        car['numberOfDoors'] = numberOfDoors
        car['priceCurrency'] = priceCurrency
        car['productionDate'] = productionDate
        car['sell_id'] = sell_id
        car['super_gen'] = super_gen
        car['vehicleConfiguration'] = vehicleConfiguration
        car['vehicleTransmission'] = vehicleTransmission
        car['vendor'] = vendor
        car['Владельцы'] = ownersCount
        car['Владение'] = owningTime
        car['ПТС'] = passport
        car['Привод'] = drive
        car['Руль'] = steer_wheel
        car['Состояние'] = condition
        car['Таможня'] = customs
        car['price'] = price

        yield car