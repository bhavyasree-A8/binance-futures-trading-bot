def print_order_summary(
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    print("\n===== ORDER REQUEST =====")

    print(f"Symbol   : {symbol}")
    print(f"Side     : {side}")
    print(f"Type     : {order_type}")
    print(f"Quantity : {quantity}")

    if price:
        print(f"Price    : {price}")


def print_order_response(response):

    print("\n===== ORDER RESPONSE =====")

    print(f"Order ID      : {response.get('orderId')}")
    print(f"Status        : {response.get('status')}")
    print(f"Executed Qty  : {response.get('executedQty')}")
    print(f"Average Price : {response.get('avgPrice')}")

    print("\nSUCCESS ✅")