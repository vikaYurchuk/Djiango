FAVOURITE_KEY = "product_favourite_key"


def add_to_favourite(session, id, quantity=1):

    favourite = session.get(FAVOURITE_KEY, {})

    if id not in favourite:
        favourite[id] = quantity
    else:
        favourite[id] += quantity

    session[FAVOURITE_KEY] = favourite


def get_favourite(session):
    return session.get(FAVOURITE_KEY, {})


def clear_favourite(session):
    session[FAVOURITE_KEY] = {}


def get_count(session):
    return len(get_favourite(session).keys())

def remove_from_favourite(session, id):
    favourite = session.get(FAVOURITE_KEY, {})
    id = str(id)
    if id in favourite:
        del favourite[id]
        session[FAVOURITE_KEY] = favourite

# TODO: implement remove item from cart by id