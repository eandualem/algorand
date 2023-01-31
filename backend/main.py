import os
import json
import base64
from algosdk import constants
from dotenv import load_dotenv
from algosdk import transaction
from algosdk.v2client import algod
from algosdk import account, mnemonic


class AlgodHelper():
    def __init__(self):
        load_dotenv()
        self.algod_address = os.getenv('algod_address')
        self.algod_token = os.getenv('algod_token')
        self.algod_client = os.getenv('algod_client')

    def generate_algorand_keypair(self):
        private_key, address = account.generate_account()
        print("My address: {}".format(address))
        print("My private key: {}".format(private_key))
        print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))

    def check_balance(self, address):
        account_info = self.algod_client.account_info(address)
        print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")
        return account_info

    def sign_transaction(self, unsigned_txn):
        signed_txn = unsigned_txn.sign(self.private_key)
        return signed_txn

    def submit_transaction(self, signed_txn):
        txid = self.algod_client.send_transaction(signed_txn)
        print("Successfully sent transaction with txID: {}".format(txid))
        return txid

    def wait_confirmation(self, txid):
        # wait for confirmation
        try:
            return transaction.wait_for_confirmation(self.algod_client, txid, 4)
        except Exception as err:
            print(err)
            return

    def make_transaction(self, private_key, my_address, receiver, note, amount):
        params = self.algod_client.suggested_params()
        params.flat_fee = True
        params.fee = constants.MIN_TXN_FEE

        unsigned_txn = transaction.PaymentTxn(my_address, params, receiver, amount, None, note)
        signed_txn = self.sign_transaction(unsigned_txn)
        self.submit_transaction(signed_txn)
        self.wait_confirmation()
