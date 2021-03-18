# -*- coding: utf-8 -*-
# app/account.py
import requests

class Account:

    def __init__(self, data_interface):
        self.di = data_interface
    
    def get_account(self, id_num):
        try:
            result = self.di.get(id_num)
        except ConnectionError:
            result = 'Connection error occurred.'
        return result

    def get_current_balance(self, id_num):
        return requests.get('http://some-account-uri/' + id_num)
    
    def get_current_balance_adv(self, id_num):
        response = requests.get('http://some-account-uri/' + id_num)
        return {
            'status': response.status_code,
            'data': response.text
        }