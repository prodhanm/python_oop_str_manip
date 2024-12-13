import sys
sys.path.append('../src')
from cc_str import CreditCardStr


class TestCreditCardStr:

    # Test 1 only passes as the expected value is the same as the result
    @staticmethod
    def test_cc_format_1():
        input_val = "1234-5678-1234-5678"
        expected_val = "1234567812345678"
        result = CreditCardStr.cc_format_string(input_val)
        
        if result == expected_val:
            print(f"Test passed: {result}")
        else:
            print("Test failed")

    @staticmethod
    def test_cc_format_2():
        input_val_2 = "1234 5678 1234 5678"
        expected_val_2 = "1234567812345678"
        result2 = CreditCardStr.cc_format_string(input_val_2)
        assert result2 != expected_val_2

        if result2 != expected_val_2:
            print(f"Test failed: {result2}")
        else:
            print("Test passed")

    # Test 3 fails as the input have no delimeter, 
    # as Test 1 contains the "-" as the delimeter.
    @staticmethod
    def test_cc_format_3():
        input_val_3 = "1234567812345678"
        expected_val_3 = "123456781234"
        result3 = CreditCardStr.cc_format_string(input_val_3)
        assert result3 != expected_val_3

        if result3 != expected_val_3:
            print(f"Test failed: {result3}")
        else:
            print("Test passed")

if __name__ == "__main__":
    TestCreditCardStr.test_cc_format_1()
    TestCreditCardStr.test_cc_format_2()
    TestCreditCardStr.test_cc_format_3()
