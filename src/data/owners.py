import datetime
import mongoengine

class Owner(mongoengine.Document):
    registered_data = mongoengine.DateTimeField(default=datetime.datetime.now)

    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)

    snake_id =mongoengine.ListField()
    cage_id = mongoengine.ListField()

    meta =  {
        'db_alias': 'core'
        'collection': 'owners'
    }