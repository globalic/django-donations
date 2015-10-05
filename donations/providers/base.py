'Base Provider for provding donations'



class DonationProvider(object):

    def __init__(self, donation):
        self.amount = donation.amount
        self.currency = donation.amount.currency
        self.verify_donation = donation.verify
        self.donation = donation

    def get_value(self):
        return self.amount.amount

    def get_currency(self):
        return self.currency

    def donate(self, verify_uri):
        '''Make the api calls to give money
        Given this library is not handling payment details this should
        simply construct the url to redirect to on the 3rd party provider site'''
        raise NotImplementedError

    def verify(self):
        '''Optional method to verify donation has been successfully recieved
        Should return True if verified correctly or False otherwise'''
        raise NotImplementedError