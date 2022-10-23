#main
import json
import re

#parcing
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#APIs
from etherscan import Etherscan

#parcing inputs
UserAgent().chrome

#eth inputs
eth_key = 'P1ARR161VTV5F45APSFDNWZ12I1DAK18J43'
eth = Etherscan(eth_key)

#tg inputs
tg_key = '5505192199:AAEtTqH_KvSXTFcue0NKCYj7zQbIMkkIKoo'


class gas:
    def price():
        response = requests.get('https://ethgasstation.info/json/ethgasAPI.json')
        table = json.loads(response.content)
        return table


class moby:
    def tx(contract):
        contract_link = 'https://etherscan.io/address/' + contract + '?utm_source=moby.gg'
        href_tx = '/txs?a=' + contract

        response_tx = requests.get(contract_link, headers={'User-Agent': UserAgent().chrome})
        html_tx = response_tx.content
        soup_tx = BeautifulSoup(html_tx, 'html.parser')
        num_of_tx = soup_tx.find('a', href=href_tx).text
        return num_of_tx


    def pending(contract):
        pending_link = 'https://etherscan.io/txsPending?a=' + contract + '&m=hf'

        response_pending = requests.get(pending_link, headers={'User-Agent': UserAgent().chrome})
        html_pending = response_pending.content
        soup_pending = BeautifulSoup(html_pending, 'html.parser')
        num_of_pending = soup_pending.find('p', class_='mb-2 mb-md-0').text
        return num_of_pending[12:-20]

    def name(contract):
        contract_link = 'https://etherscan.io/address/' + contract + '?utm_source=moby.gg'
        href_name = '/token/' + contract

        response_name = requests.get(contract_link, headers={'User-Agent': UserAgent().chrome})
        html_name = response_name.content
        soup_name = BeautifulSoup(html_name, 'html.parser')
        collection_name = soup_name.find('a', href=href_name).text
        return collection_name


    def write(contract):
        write_link = 'https://etherscan.io/address/' + contract + '?utm_source=moby.gg#writeContract'
        return write_link


def find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]