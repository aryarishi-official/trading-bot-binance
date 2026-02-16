from bot.logging_config import setup_logging
import logging,typer
from bot.client import get_client
from bot.validators import validate_order
from bot.orders import place_order

app=typer.Typer()

@app.command()
def trade(
    symbol:str,
    side:str,
    order_type:str,
    quantity:float,
    price:float=None
 ):
    setup_logging()
    side = side.upper()
    order_type = order_type.upper()
    print("Processing order...")
    try:
        validate_order(symbol,side,order_type,quantity,price)
        response=place_order(symbol,side,order_type,quantity,price)
        print("\nOrder Summary:")
        print("Symbol:",response.get("symbol"))
        print("Side:",response.get("side"))
        print("Type:",response.get("type"))
        print("Status:",response.get("status"))

        print("\n Excecution Details:")
        print("Order ID:",response.get("orderId"))
        print("Excecuted Quantity:",response.get("executedQty"))

        if response.get("fills"):
            avg_price=response["fills"][0]["price"]
            print("average Price:",avg_price)

        print("\nOrder Placed Successfully")   
    except Exception as e:
        print("\nOrder failed",e) 
if __name__ == "__main__":
    app()            
    

