from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger()


class OrderManager:

    def __init__(self):
        self.client = BinanceClient().client

    def place_market_order(self, symbol, side, quantity):

        try:

            logger.info(
                f"MARKET ORDER REQUEST | Symbol={symbol} Side={side} Qty={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"MARKET ORDER RESPONSE | {response}")

            return response

        except Exception as e:

            logger.error(f"MARKET ORDER FAILED | {str(e)}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):

        try:

            logger.info(
                f"LIMIT ORDER REQUEST | Symbol={symbol} Side={side} Qty={quantity} Price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(f"LIMIT ORDER RESPONSE | {response}")

            return response

        except Exception as e:

            logger.error(f"LIMIT ORDER FAILED | {str(e)}")
            raise