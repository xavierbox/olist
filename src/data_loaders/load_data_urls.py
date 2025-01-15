
import pandas as pd 

def load_url_raw_data( sources ):

    '''
    sources: dict { 'customer_df_url': url, 'order_reviews_url': url }
    '''

    customer_df = pd.read_csv(sources['customer_df_url'])
    order_reviews_df = pd.read_csv(sources['order_reviews_url'])

    return{ 'customer_df':customer_df,'order_reviews_df':order_reviews_df }