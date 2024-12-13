class CreditCardStr:
    def __init__(self, card_number):
        self.card_number = card_number

    cc_inp = input("Enter your credit card number: ")

    @staticmethod
    def cc_format_string(card_number):
        return card_number.replace("-", "")
    
formatted_cc = CreditCardStr.cc_format_string("1234-5678-1234-5678")
print(formatted_cc)
    
