# Bitcoin Market Live chart
This project is a real-time Bitcoin candlestick chart built using the Dash web framework. It fetches live Bitcoin price data from the CoinGecko API and visualizes the latest 100 candles in a candlestick chart. The chart is updated every 6 seconds to provide a dynamic view of Bitcoin's price movement.


![newplot](https://github.com/akhilkarthik/bitcoin_Live_chart/assets/40953068/d130578b-0326-4171-abcd-29dba5fee28c)

Table of Contents
Requirements
Installation
Usage
Project Structure
Dependencies
Contributing
License
Requirements
To run this project, you need the following:

Python 3.x
Dash (installed via pip install dash)
Plotly (installed via pip install plotly)
Pandas (installed via pip install pandas)
NumPy (installed via pip install numpy)
Pycoingecko (installed via pip install pycoingecko)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/dash-bitcoin-candlestick.git
Navigate to the project directory:

bash
Copy code
cd dash-bitcoin-candlestick
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Dash application:

bash
Copy code
python app.py
Open your web browser and go to http://127.0.0.1:8050/ to view the live Bitcoin candlestick chart.

Project Structure
The project structure is organized as follows:

app.py: The main script containing the Dash application.
requirements.txt: A file specifying the required Python packages.
README.md: This readme file.
Dependencies
This project relies on the following Python packages:

Dash: A web framework for building interactive web applications.
Plotly: A graphing library for creating interactive plots.
Pandas: A data manipulation and analysis library.
NumPy: A library for numerical operations.
Pycoingecko: A Python wrapper for the CoinGecko API.
