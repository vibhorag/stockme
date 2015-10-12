import requests
import datetime
import pandas as pd
import numpy as np

def getstockdata(stock):
    url_link = "https://www.quandl.com/api/v3/datasets/WIKI"

    today     = datetime.date.today()    
    startdate = today - datetime.timedelta(30)

    quandl_api = "%s/%s.json?start_date=%s&end_date=%s"%(url_link,stock,startdate,today)
    
    print quandl_api
    
    # Grab the data from Quandl 
    r = requests.get(quandl_api)

    # Load data into a pandas dataframe
    df0 = pd.read_json(r.text)['dataset']
    df  = pd.DataFrame(df0['data'],columns=df0['column_names'])
    df['Date'] = pd.to_datetime(df['Date'])

    return df.loc[:,['Date','Close','Adj. Close','Volume']]


if __name__=="__main__":


    stock = "GOOG"
    df = getstockdata(stock)
    import IPython
    IPython.embed()
