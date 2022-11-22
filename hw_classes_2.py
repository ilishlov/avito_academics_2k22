import json
import keyword


class DynamicAttributes:
    """
    динамически создает атрибуты экземпляра класса
    из атрибутов JSON-объекта
    """
    def __init__(self, attr_dict: dict) -> None:
        for key, value in attr_dict.items():
            if keyword.iskeyword(key):
                key = key + '_'
            if isinstance(value, dict):
                setattr(self, key, DynamicAttributes(value))
            else:
                setattr(self, key, value)


class ColorizeMixin:
    """
    Выводит в функции print() текст другого цвета
    """
    def __repr__(self) -> str:
        return f"\033[0;{self.repr_color_code};" \
               f"40m {self.title} | {self.price} ₽"


class Advert(ColorizeMixin, DynamicAttributes):
    """
    - динамически создает атрибуты экземпляра класса из атрибутов JSON-объекта
    - имеет свойство price
    – имеется текстовое представление объекта (в том числе с/без миксином)
    """
    repr_color_code = 33 # желтый, согласно условию
    def __init__(self, data: dict) -> None:
        self.data = data
        super().__init__(self.data)
        if not hasattr(self, "title"):
            raise ValueError("Не указано название товара")
        if not hasattr(self, "price"):
            self.price = 0
        if self.price < 0:
            raise ValueError("Указана отрицательная цена")
            
    def __repr__(self) -> str:
        if issubclass(Advert, ColorizeMixin):
            return ColorizeMixin.__repr__(self)
        return f"{self.title} | {self.price} ₽"


if __name__ == "__main__":
    lesson_str = """{
        "title": "iPhone X",
        "class": "mobile phone",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"] }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad)

    # проверить, что к полям можно обращаться через точку:
    # print(lesson_ad.title)
    # print(lesson_ad.location.address)

    # проверить, что есть поле title, иначе выбросить ValueError:
    # print(lesson_ad.title)

    # проверить, что выводится для keyword-ного class_:
    # print(lesson_ad.class_)

    # проверить, что выводится прайс
    # print(lesson_ad.price)

    # проверить, что если прайса нет, то выводится 0
    # print(lesson_ad.price)

    # проверить, что прайс неотрицательный, иначе выбросить ValueError
    # print(lesson_ad.price)
