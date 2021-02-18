import requests
import json
import pandas
import os
import datetime


def main():

    #url = 'https://scanner.tradingview.com/forex/scan'
    url = 'https://scanner.tradingview.com/america/scan'
# headers = {
#     "Host": "scanner.tradingview.com",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
#     "Accept": "text/plain, */*; q=0.01",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Referer": "https://www.tradingview.com/",
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Content-Length": 585,
#     "Origin": "https://www.tradingview.com",
#     "Connection": "keep-alive",
#     "Cookie": "_sp_ses.cf1a=*; _sp_id.cf1a=ca881a4d-48f3-45a8-a330-99e315e00cde.1609378590.1.1609379216.1609378590.82f1a15a-7e8a-4918-a091-a325f5471f80; sessionid=3ht9460hu1psmkszpl7wmaiqy4zoppd1; etg=undefined; cachec=undefined",
#     "TE": "Trailers"
# }


#body = {"filter":[{"left":"name","operation":"nempty"},{"left":"sector","operation":"in_range","right":["Major","Minor"]},{"left":"EMA200|15","operation":"greater","right":"close|15"}],"options":{"lang":"en"},"symbols":{"query":{"types":["forex"]},"tickers":[]},"columns":["base_currency_logoid","currency_logoid","name","close|15","EMA200|15","MACD.macd|15","MACD.signal|15","description","name","type","subtype","update_mode|15","pricescale","minmov","fractional","minmove2","EMA200|15","close|15","MACD.macd|15","MACD.signal|15"],"sort":{"sortBy":"name","sortOrder":"asc"},"range":[0,150]}
    body = {"filter": [{"left": "volume|15", "operation": "nempty"}, {"left": "type", "operation": "in_range", "right": ["stock", "dr", "fund"]}, {"left": "subtype", "operation": "in_range", "right": ["common", "", "etf", "unit", "mutual", "money", "reit", "trust"]}, {"left": "exchange", "operation": "in_range", "right": ["AMEX", "NASDAQ", "NYSE"]}, {"left": "volume|15", "operation": "egreater", "right": 200000}, {"left": "EMA200|15", "operation": "greater", "right": "close|15"}, {"left": "MACD.macd|15", "operation": "greater", "right": "MACD.signal|15"}, {
        "left": "MACD.signal|15", "operation": "greater", "right": 0}], "options": {"active_symbols_only": "true", "lang": "en"}, "symbols": {"query": {"types": []}, "tickers": []}, "columns": ["logoid", "name", "close|15", "volume|15", "EMA200|15", "MACD.macd|15", "MACD.signal|15", "description", "name", "type", "subtype", "update_mode|15", "pricescale", "minmov", "fractional", "minmove2", "EMA200|15", "close|15", "MACD.macd|15", "MACD.signal|15"], "sort": {"sortBy": "volume|15", "sortOrder": "desc"}, "range": [0, 150]}


    r = requests.post(url, json=body)
    print("Printing DATA\n")


    #cur_path = os.getcwd()
    cur_path = r'C:\Users\wjddj\Desktop\Project Penguin\projectpenguin'
    print(cur_path)
    newpath = cur_path + r'\.data'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    os.chdir('.data')

    data_json = r.json()

    n = data_json["totalCount"]

# for i in range(n) :
#     print(data_json["data"][i]["d"][1])

    datalist = []
    for i in range(n):
        datalist.append((data_json["data"][i]["d"][1], data_json["data"][i]["d"][2], data_json["data"][i]["d"]
                     [3], data_json["data"][i]["d"][4], data_json["data"][i]["d"][5], data_json["data"][i]["d"][6]))

    df = pandas.DataFrame(datalist, columns=[
                      'Ticker', 'Last', 'Volume', 'Exponential Moving Average (200)', 'MACD Level (12, 26)', 'MACD Signal (12, 26)'])
    df.to_excel('stockscreener.xlsx', index=False)

    #cur_path = os.getcwd()
    print(cur_path)
    newpath = cur_path + r'\stock_by_tickers'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    split_values = df['Ticker']
# print(split_values)

    for value in split_values:
        df1 = df[df['Ticker'] == value]
        df1 = df1.assign(datetime=datetime.datetime.now())
        output_file_name = "Ticker_" + str(value) + ".xlsx"
        complete_file_directory = cur_path + "\\stock_by_tickers\\" + output_file_name
        if os.path.isfile(complete_file_directory):
            df2 = pandas.read_excel(complete_file_directory)
            df2 = df2.append(df1, ignore_index=False)
            df2.to_excel(complete_file_directory, index=False)
        else:
            df1.to_excel(complete_file_directory, index=False)
