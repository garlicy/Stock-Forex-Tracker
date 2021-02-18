# Stock-Forex-Tracker

# Description
Tracks the data from tradingview.com
Was gonna scrape the data by OCR-Optical Character Recognition or something else but found out the simpler and easier way that works on Tradingview.com

Records a data of filtered tickers and save it into separate files by tickers with timestamp.
Enables other application to use this data.

# Tasks
## Python
  * Send POST request to tradingview.com to get data. Can also set the filters by putting the JSON format filter code inside the BODY.
## Postman
   * Experimented in Postman to find out where can the filter JSON to be put in. Was not sure if it should go in parameter or somewhere else.
## Firefox
   * Used developer mode to find out where and how the data's are coming from.
   * [Finding Signal](./tradingview.png)
   
## Used Library
 * Pandas
 * Requests
 * Datetime
 * Os
 * Json

# More
 * Can this method also grab a graph?
