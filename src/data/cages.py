class Cage:
    registered_data = None

    price = None
    square_meter = None
    name = None
    has_toy = None
    is_carpeted = None
    allow_dangerous_snakes = None

    bookings = list()

    meta =  {
        'db_alias': 'core'
        'collection': 'cages'
    }