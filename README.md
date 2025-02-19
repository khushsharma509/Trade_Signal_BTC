This project is a real-time cryptocurrency trading dashboard that fetches live Binance BTC/USDT price data and displays key trading indicators like EMA, RSI, MACD, and Market Trends using Flask and Tailwind CSS.

✅ Live BTC Price Updates Every 10 Seconds
✅ EMA 9 & EMA 21 for Trend Analysis
✅ RSI & MACD Indicators for Trade Signals
✅ Modern UI with Dark Mode & Responsive Design

🌟 How to Run This Project Locally
Follow these simple steps to clone, install, and run this Flask-powered crypto dashboard on your system.

📥 1. Clone the Repository
Open your terminal and run:
git clone https://github.com/your-username/crypto-trading-dashboard.git
cd crypto-trading-dashboard

📦 2. Install Dependencies
Make sure you have Python 3.x installed. Then, install the required dependencies:
pip install flask pandas numpy requests


🚀 3. Run the Flask Server
Start the server by running:
python app.py
After running, you should see output like:

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

   
🌐 4. Open the Dashboard in Your Browser
Go to http://127.0.0.1:5000/ in your browser, and you’ll see the real-time crypto market dashboard with live price updates.

📂 Project Structure
crypto-trading-dashboard/
│── templates/
│   ├── index.html  # Frontend UI (Styled with Tailwind CSS)
│── app.py          # Flask API Server
│── requirements.txt # List of dependencies (optional)
│── README.md       # Project Documentation
🛠 Tech Stack
🔹 Flask - Python Web Framework
🔹 Binance API - Fetches real-time BTC/USDT data
🔹 Pandas & NumPy - Data processing & technical indicators
🔹 Tailwind CSS - Beautiful, responsive UI

📡 Live Features
✅ Automatic Live Updates Every 10 Seconds
✅ Bullish & Bearish Trend Detection
✅ Mobile-Friendly & Dark Mode
✅ Fast API Responses with Flask
