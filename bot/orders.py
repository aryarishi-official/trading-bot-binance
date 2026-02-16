import logging
from bot.client import get_client

def place_order(symbol,side,order_type,quantity,price=None):
    client=get_client()

    try:
        logging.info(f"placing order:{symbol} {side} {order_type} {quantity}")
        if order_type == "MARKET":
            response=client.create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
                )
        elif order_type == "LIMIT": 
            response=client.create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
                ) 
        logging.info(f"order placed {response}") 
        return response
    except Exception as e:
        logging.error(f"order failed:{str(e)}")  
        raise 


