def validate_order(symbol,side,order_type,quantity,price):
    if not symbol:
        raise ValueError("Symbol is required")
    if side not in ["BUY","SELL"]:
        raise ValueError("Side must be buy or sell")
    if order_type not in ["MARKET","LIMIT"]:
        raise ValueError("order type must be")
    if quantity<=0:
        raise ValueError("")
    if order_type=="LIMIT" and price is None:
        raise ValueError("price is required for LIMIT orders")
    

