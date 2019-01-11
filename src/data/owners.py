class Owner:
    registered_data = None

    name = None
    email = None
    snake_id = None
    cage_id = None

    meta =  {
        'db_alias': 'core'
        'collection': 'owners'
    }