# Binance Futures Testnet Trading Bot

## Overview

A Python-based trading bot for Binance Futures Testnet (USDT-M) that supports:

* Market Orders
* Limit Orders
* BUY and SELL operations
* CLI-based user input
* Input validation
* Logging
* Error handling

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── order_formatter.py
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── cli.py
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Clone Repository

```bash
git clone <repository_url>
cd trading_bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file:

```env
API_KEY=YOUR_API_KEY
SECRET_KEY=YOUR_SECRET_KEY
```

---

## Running the Application

### Market Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

---

## Features

* Binance Futures Testnet Integration
* Market Order Support
* Limit Order Support
* BUY and SELL Support
* Input Validation
* Structured Logging
* Exception Handling
* Clean CLI Output

---

## Logging

Logs are stored in:

```text
logs/trading_bot.log
```

The application records:

* Order Requests
* Order Responses
* Errors and Exceptions

---

## Assumptions

* Binance Futures Testnet account is active.
* Valid API Key and Secret Key are provided.
* User has sufficient testnet balance.
* Supported order types are MARKET and LIMIT.
