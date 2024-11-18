def inventorymonitorcontroller(stock_level, critical_level=10):
    if stock_level < critical_level:
        return True
    return False
