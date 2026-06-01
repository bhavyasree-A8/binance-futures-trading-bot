from bot.order_formatter import (
    print_order_summary,
    print_order_response
)

sample_response = {
    "orderId": 12345,
    "status": "FILLED",
    "executedQty": "0.001",
    "avgPrice": "72000"
}

print_order_summary(
    symbol="BTCUSDT",
    side="BUY",
    order_type="MARKET",
    quantity=0.001
)

print_order_response(sample_response)