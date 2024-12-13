class CreditCardStr:
    def __init__(self, card_number):
        self.card_number = card_number


    @staticmethod
    def cc_format_string(card_number):
        return card_number.replace("-", "")
    
card_number = input("Enter your credit card number: ")
formatted_cc = CreditCardStr.cc_format_string(card_number)
print(formatted_cc)
    
