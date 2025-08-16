
from dotenv import load_dotenv
import os
import requests
import utils
from settings import list_chains_id
load_dotenv()


def get_balance_tron(wallet):

    url =  f"https://apilist.tronscanapi.com/api/account/tokens?address={wallet}&start=0&limit=20&hidden=0&show=0&sortType=0&sortBy=0&token="
    response = requests.get(url)
    result = response.json()
    if "status" in result and result['status'] is "1":
         list_names,list_balance,list_value_usd = [],[],[]
         for token in result['data']:
              list_names.append(token['tokenName'])
              list_balance.append(token['quantity'])
              list_value_usd.append(token['amountInUsd'])
        
         df = utils.create_data_frame(list_names,list_value_usd,list_balance)
         return df
    return False


def get_balance_evm_chain(wallet,chain):
    url = f"https://api.covalenthq.com/v1/{list_chains_id[chain]['code']}/address/{wallet}/balances_v2/?key={os.getenv('GOLD_RUSH_API_KEY')}"
    response = requests.get(url)
    if response.status_code is 200:
        data = response.json()
        list_names,list_balance,list_value_usd = [],[],[]
        
        for token in data['data']['items']:
               balance = utils.delete_no_balance_tokens(token['contract_decimals'],token['balance'])
               if balance and token['quote'] is not None and token['quote'] > 1:
                    list_names.append(token['contract_ticker_symbol'])
                    list_balance.append(balance)
                    list_value_usd.append(round(token['quote'],0))
        df = utils.create_data_frame(list_names,list_value_usd,list_balance)

        return df
    return False




