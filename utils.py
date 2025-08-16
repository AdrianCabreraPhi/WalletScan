
import pandas as pd
import settings
import streamlit as st
import re

# String format
# function to return available chains in message on interface
def list_of_available_chains():
        msg = "Available chains: "
        for chain in settings.list_chains_available:
                msg += f" :red[{chain['name']}], "
        return msg


def delete_no_balance_tokens(contract_decimals,balance):
        if int(balance) > 0 and contract_decimals is not None:
              return round(int(balance) / 10**contract_decimals,2)
        return False


def create_data_frame(list_names,list_value_usd,list_balance):
    df = pd.DataFrame({
             "Token": list_names,
             "$": list_value_usd,
             "Units": list_balance
        })
    return df

def filter_available_chains(wallet):
              filter_chains = []
              for idx, chain in enumerate(settings.list_chains_available):
                     if chain['wallet_rules'].match(wallet):
                            filter_chains.append(settings.list_chains_available[idx])            
              return filter_chains


def plot_data(df):
        if isinstance(df,pd.DataFrame):
                        st.dataframe(df)
                        st.bar_chart(df.set_index("Token")["$"])
                        msg = True
        else:
                st.toast("Unexpected error")
                msg = False
        
        return msg
                


                             
                            
              
              

