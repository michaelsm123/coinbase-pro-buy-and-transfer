import cbpro
from cbpro.authenticated_client import AuthenticatedClient

api_key = ""
api_secret = ""
api_passphrase = ""

class bankTransfer:

    client = AuthenticatedClient("","","")

    def __init__(self,key,secret,passphrase) -> cbpro.AuthenticatedClient:
        self.client =  cbpro.AuthenticatedClient(key,secret,passphrase)

    def getBankPaymentId(self):
        method_id = ""
        paymentMethods = self.client.get_payment_methods()
        for method in paymentMethods:
            type = method.get('type',None)
            currency = method.get('currency',None)
            if currency == 'USD' and type == 'ach_bank_account':
                method_id = method.get('id',None)
                break
        return method_id

    def deposit(self, amount, currency, method):
        self.client.deposit(amount,currency,method)

if __name__ == "__main__":

    RB = bankTransfer(api_key,api_secret,api_passphrase)
    bankID = RB.getBankPaymentId()
    RB.deposit(300,'USD',bankID)

    print("Deposited 300 into coinbase pro account")