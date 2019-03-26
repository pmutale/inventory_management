import factory
from stock.models.items.assets.audio_visual import Kind


class BookFactory(factory.Factory):
    class Meta:
        model = Kind

    name = factory.Faker('sentence', nb_words=4)
    screen_size = factory.Faker('name')
