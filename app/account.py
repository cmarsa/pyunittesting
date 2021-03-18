# -*- coding: utf-8 -*-
# app/account.py


class Account:

    def __init__(self, data_interface):
        self.di = data_interface
    
    def get_account(self, id_num):
        return self.di.get(id_num)
