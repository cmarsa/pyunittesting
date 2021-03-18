# -*- coding: utf-8 -*-
# test/unit/app/test_account.py
import unittest
from mock import Mock
from mock import patch
from app.account import Account


class TestAccount(unittest.TestCase):
    
    def test_account_returns_data_for_id_1(self):
        account_data = {'id': '1', 'name': 'test'}
        mock_data_interface = Mock()
        mock_data_interface.get.return_value = account_data
        account = Account(mock_data_interface)
        self.assertDictEqual(account_data, account.get_account(1))
    
    def test_account_when_connection_error_raised(self):
        mock_data_interface = Mock()
        mock_data_interface.get.side_effect = ConnectionError
        account = Account(mock_data_interface)
        self.assertEqual('Connection error occurred.', account.get_account(1))
    
    @patch('app.account.requests')
    def test_get_current_balance_returns_data_correctly(self, mock_requests):
        mock_requests.get.return_value = '500'
        account = Account(Mock())
        self.assertEqual('500', account.get_current_balance('1'))



if __name__ == '__main__':
    unittest.main()