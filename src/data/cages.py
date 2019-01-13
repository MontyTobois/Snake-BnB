import mongoengine
import datetime

from data.bookings import Booking


class Cage(mongoengine.Document):
    registered_data = mongoengine.DateTimeField(default=datetime.datetime.now)

    price = mongoengine.FloatField(required=True)
    square_meter = mongoengine.BooleanField(required=True)
    name = mongoengine.StringField(required=True)
    has_toy = mongoengine.BooleanField(required=True)
    is_carpeted = mongoengine.BooleanField(required=True)
    allow_dangerous_snakes = mongoengine.BooleanField(default=False)

    bookings = mongoengine.EmbeddedDocumentListField(Booking)

    meta = {
        'db_alias': 'core',
        'collection': 'cages'
    }