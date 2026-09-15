
def is_valid_order(order):
    """True if the order passes every rule."""

    # TODO: check that distance is greater than 0
    if order["distance_km"] <= 0:
        return False

    # TODO: check that preparation time is 0 or more
    if order["prep_time_min"] < 0:
        return False

    # TODO: check that traffic level is 1, 2, or 3
    if order["traffic_level"] not in [1, 2, 3]:
        return False

    # TODO: check that rain is 0 or 1
    if order["rain"] not in [0, 1]:
        return False

    return True
