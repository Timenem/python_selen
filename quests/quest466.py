def find_routes(routes):
    routes = dict(routes)
    places = list(routes.keys() - routes.values())
    try:
        for place in places:
            places.append(routes[place])
    finally:
        return ', '.join(places)
