import streamlit as st
import endpoints
import os
import utils
from settings import list_chains_id


def select_chain(chain):
    msg = st.toast("Loading data ...",icon="⌛")
    if chain in list_chains_id :
        df = endpoints.get_balance_evm_chain(wallet,chain)
        if df['result'] is None:
            msg.toast(df['message'],icon="❌")
            return
        
        utils.plot_data(df['result'])
        
            
    if chain == "TRX":
        df = endpoints.get_balance_tron(wallet)
        utils.plot_data(df)

# SIDEBAR
with st.sidebar:
    st.logo(os.path.join("static", "logo.png"),size="large")
    text,icon = st.columns([0.92,0.08],vertical_alignment="bottom")
    with text:
        st.subheader("Insert your wallet address") 
    with icon:
        st.button("", type="tertiary", icon=":material/info:", help=utils.list_of_available_chains()) # info tooltip

    wallet = st.text_input(label="", label_visibility="collapsed",icon="🗒")
    scanButton = st.button("Scan 🔎 ",use_container_width=True,type="primary")
#SIDEBAR END



if scanButton:
    chains = utils.filter_available_chains(wallet)
    if chains:
        st.caption("Choose chain to see your tokens")
        num_cols = 3 
        for i in range(0, len(chains), num_cols):
            row_chains = chains[i:i+num_cols]
            coin_cols = st.columns(num_cols, gap="small", vertical_alignment="center", border=False)

            for col, coin in zip(coin_cols, row_chains):
                with col:
                    img_col, btn_col = st.columns([0.25, 0.75], vertical_alignment="center")
                    with img_col: # img col
                        st.image(
                            os.path.join("static", coin["img"]),
                            width=30
                        )
                    with btn_col: # btn col
                        st.button(
                            coin['name'],
                            key=f"btn_{coin['symbol']}",
                            use_container_width=True,
                            on_click=select_chain,
                            kwargs={"chain": coin["symbol"]}
                        )
    else:
        st.toast("Invalid wallet", icon="❌")






