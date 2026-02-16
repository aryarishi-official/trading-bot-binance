# Simplified Trading Bot – Binance Spot Testnet

## 📖 Overview

This project is a CLI-based trading bot built using Python 3.  
It connects to Binance Spot Testnet and allows placing MARKET and LIMIT orders.  
The application follows a structured architecture with proper logging, validation, and exception handling.

---

# 1 Project Structure

trading-bot-binance/
│
├── bot/
│ ├── init.py
│ ├── client.py # Binance client wrapper
│ ├── orders.py # Order placement logic
│ ├── validators.py # Input validation
│ ├── logging_config.py
│
├── cli.py # CLI entry point
├── requirements.txt
├── README.md
├── .env (not committed)


---

# 2 Setup Instructions

    1 Clone Repository

    ```bash
        git clone https://github.com/aryarishi-official/trading-bot-binance.git
        cd trading-bot-binance

    2 Create Virtual Environment
        python -m venv venv
        source venv/bin/activate   # macOS/Linux

    3 Install Dependencies
        pip install -r requirements.txt

    4 Configure API Keys

        Create a .env file in the project root:

        API_KEY=your_api_key_here
        API_SECRET=your_api_secret_here

        API keys must be generated from:

        https://testnet.binance.vision (Choose Generate HMAC-SHA-256 Key)

---

# 3 How To Run

    Market Order Example
    python cli.py BTCUSDT BUY MARKET 0.001

    Limit Order Example
    python cli.py BTCUSDT SELL LIMIT 0.001 --price 70000

 # 3.1 Logging

    All API requests, responses, and errors are logged to:

    trading.log

    The log file contains:

        1. Order request summary

        2. API response

        3. Error handling details

---

# 4 Assumptions

    Binance Futures Testnet endpoints were not accessible during development.
    Therefore, Binance Spot Testnet was used to demonstrate API integration.

    The architecture remains compatible with Futures endpoints by:

    Replacing client.create_order() with client.futures_create_order()

    Updating the base URL to the Futures Testnet endpoint

# 4.1 Key Features

    Structured modular architecture

    CLI-based input using Typer

    Input validation layer

    Exception handling

    API request/response logging

    Environment variable configuration


---

Save the file.

---

# 5 Make Sure `.gitignore` Exists

    Open `.gitignore`.

    It must contain:
        venv/
        .env
        pycache/
        *.pyc
        trading.log

    This prevents secrets and logs from being pushed.

    If `.gitignore` doesn’t exist:

    ```bash
    touch .gitignore