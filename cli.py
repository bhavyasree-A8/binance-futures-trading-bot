import argparse

from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.order_formatter import (
    print_order_summary,
    print_order_response
)


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True
    )

    parser.add_argument(
        "--price",
        required=False
    )

    args = parser.parse_args()

    try:

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        price = None

        if order_type == "LIMIT":

            if not args.price:
                raise ValueError(
                    "Price is required for LIMIT orders"
                )

            price = validate_price(args.price)

        print_order_summary(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        manager = OrderManager()

        if order_type == "MARKET":

            response = manager.place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            response = manager.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print_order_response(response)

    except Exception as e:

        print("\nFAILED ❌")
        print(str(e))


if __name__ == "__main__":
    main()