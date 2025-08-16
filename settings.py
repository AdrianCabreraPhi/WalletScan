
import re

EVM_REGEX = re.compile(r'^0x[a-fA-F0-9]{40}$')
TRON_REGEX = re.compile(r'^T[1-9A-HJ-NP-Za-km-z]{33}$')
# SOLANA_REGEX = re.compile(r'^[1-9A-HJ-NP-Za-km-z]{43,44}$')

list_chains_available = [
    {"name":"Ethereum","symbol": "ETH","wallet_rules":EVM_REGEX, "img": "ethereum.png"},
    {"name":"Binance","symbol": "BNB","wallet_rules":EVM_REGEX, "img": "bnb.png"},
    {"name":"Arbitrum One","symbol": "ARB","wallet_rules":EVM_REGEX, "img": "arbitrum.png"},
    {"name":"Polygon","symbol": "POL","wallet_rules":EVM_REGEX, "img": "polygon.png"},
    {"name":"Optimism","symbol": "OP","wallet_rules":EVM_REGEX, "img": "optimism.png"},
    {"name":"Avalanche","symbol": "AVAX","wallet_rules":EVM_REGEX, "img": "avalanche.png"},
    {"name":"Base","symbol": "BASE","wallet_rules":EVM_REGEX, "img": "base.png"},
    {"name":"zkSync","symbol": "zkSync","wallet_rules":EVM_REGEX, "img": "zkSync.png"},
    {"name":"Tron","symbol": "TRX","wallet_rules":TRON_REGEX,"img": "tron.png"},
#    {"name":"Solana","symbol": "SOL","wallet_rules":SOLANA_REGEX,"img": "solana.png"}

]

#evm: Ethereum virtual machine
#use etherscan api
list_chains_id = {
    "ETH":{"code":1},
    "BNB":{"code":56},
    "ARB":{"code":42161},
    "OP":{"code":10},
    "AVAX":{"code":43114},
    "BASE":{"code":8453},
    "POL":{"code":137},
    "zkSync":{"code":324},
#   "SOL":{"code":"solana-mainnet"}
}

