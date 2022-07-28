
from blueshift.api import(    symbol,
                            order_target_percent,
                            schedule_function,
                            date_rules,
                            time_rules,
                            record,
                       )
 
import numpy as np
 
import pandas as pd 
 
def initialize(context):
    context.jj = symbol("ETH") 
 
    schedule_function(check_bands, date_rules.every_day(),time_rule=time_rules.market_open())
    
   
 
 
def check_bands(context, data):
    
    cur_price =  data.current(context.jj, 'close')
    prices = data.history(context.jj, "close", 20, '1d')  
    lower_band = prices.mean() - 2*prices.std()
    upper_band = prices.mean() + 2*prices.std()
    
    if cur_price <= lower_band:
        order_target_percent(context.jj, 1.0)
        print('Buying')
        print('Current price is: '+ str(cur_price))
        print("Lower band is: "+ str(lower_band))
        
        
    elif cur_price >= upper_band:
        order_target_percent(context.jj, -1.0)
        print('Shorting')
        print('Current price is: '+ str(cur_price))
        print("Upper band is: "+ str(upper_band))
    else:
        pass
        
    record(upper=upper_band,
           lower=lower_band,
           mvag_20=prices.mean(),
           price=cur_price)
