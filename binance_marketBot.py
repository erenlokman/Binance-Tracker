import config
from binance.client import Client
from datetime import datetime
from pandas import DataFrame as df

#API KEY is stored in Config.py
client = Client(config.API_KEY,config.API_SECRET)

pair = input('Type your pair ETHUSDT, BTCUSDT, BNBBTC, ROSEUSDT \n')

if pair == 'ETHUSDT':
    #Candle data for ETH each 1 DAY - 24H
    candles = client.get_klines(symbol = 'ETHUSDT', interval = Client.KLINE_INTERVAL_1DAY)

    #By using pandas library we can display it as table on terminal
    candles_data_frame = df(candles)

    candles_data_frame_date = candles_data_frame[0]

    final_date = []

    # To make the dates clear
    for time in candles_data_frame_date.unique():
        readable = datetime.fromtimestamp(int(time/1000))
        final_date.append(readable)


    candles_data_frame.pop(0)
    
    candles_data_frame.pop(11)

    dataframe_final_date = df(final_date)

    
    dataframe_final_date.columns = ['DATE']

    final_dataframe = candles_data_frame.join(dataframe_final_date)


    final_dataframe.set_index('DATE', inplace=True)

    final_dataframe.columns = ['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'CLOSE_TIME', 'ASSET_VOLUME', 'TRADE_NUMBER', 'TAKER_BUY_BASE', 'TAKER_BUY_QUOTE']

    print(final_dataframe)

elif pair == 'BTCUSDT':
    #Candle data for ETH each 1 DAY - 24H
    candles = client.get_klines(symbol = 'BTCUSDT', interval = Client.KLINE_INTERVAL_1DAY)

    #By using pandas library we can display it as table on terminal
    candles_data_frame = df(candles)

    candles_data_frame_date = candles_data_frame[0]

    final_date = []

    # To make the dates clear
    for time in candles_data_frame_date.unique():
        readable = datetime.fromtimestamp(int(time/1000))
        final_date.append(readable)


    candles_data_frame.pop(0)
    candles_data_frame.pop(11)

    dataframe_final_date = df(final_date)

    dataframe_final_date.columns = ['DATE']

    final_dataframe = candles_data_frame.join(dataframe_final_date)


    final_dataframe.set_index('DATE', inplace=True)

    final_dataframe.columns = ['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'CLOSE_TIME', 'ASSET_VOLUME', 'TRADE_NUMBER', 'TAKER_BUY_BASE', 'TAKER_BUY_QUOTE']

    print(final_dataframe)


elif pair == 'BNBBTC':
    #Candle data for ETH each 1 DAY - 24H
    candles = client.get_klines(symbol = 'BNBBTC', interval = Client.KLINE_INTERVAL_1DAY)

    #By using pandas library we can display it as table on terminal
    candles_data_frame = df(candles)

    candles_data_frame_date = candles_data_frame[0]

    final_date = []

    # To make the dates clear
    for time in candles_data_frame_date.unique():
        readable = datetime.fromtimestamp(int(time/1000))
        final_date.append(readable)


    candles_data_frame.pop(0)
    candles_data_frame.pop(11)

    dataframe_final_date = df(final_date)

    dataframe_final_date.columns = ['DATE']

    final_dataframe = candles_data_frame.join(dataframe_final_date)


    final_dataframe.set_index('DATE', inplace=True)

    final_dataframe.columns = ['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'CLOSE_TIME', 'ASSET_VOLUME', 'TRADE_NUMBER', 'TAKER_BUY_BASE', 'TAKER_BUY_QUOTE']

    print(final_dataframe)


elif pair == 'ROSEUSDT':
    #Candle data for ETH each 1 DAY - 24H
    candles = client.get_klines(symbol = 'ROSEUSDT', interval = Client.KLINE_INTERVAL_1DAY)

    #By using pandas library we can display it as table on terminal
    candles_data_frame = df(candles)

    candles_data_frame_date = candles_data_frame[0]

    final_date = []

    # To make the dates clear
    for time in candles_data_frame_date.unique():
        readable = datetime.fromtimestamp(int(time/1000))
        final_date.append(readable)


    candles_data_frame.pop(0)
    candles_data_frame.pop(11)

    dataframe_final_date = df(final_date)

    dataframe_final_date.columns = ['DATE']

    final_dataframe = candles_data_frame.join(dataframe_final_date)


    final_dataframe.set_index('DATE', inplace=True)

    final_dataframe.columns = ['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'CLOSE_TIME', 'ASSET_VOLUME', 'TRADE_NUMBER', 'TAKER_BUY_BASE', 'TAKER_BUY_QUOTE']

    print(final_dataframe)
