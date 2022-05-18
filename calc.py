def calculate_unit_price(data):
    """Calculate price per unit."""
    for item in data:
        item['unit_price'] = round(item['total_price'] / item['quantity'], 2)
    return data
