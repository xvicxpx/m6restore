import sys

def perform_luhn_check(number):
    reversed_ints = [int(n) for n in reversed(number)]
    check_digit = reversed_ints[0]
    sum_of_digits = sum((digit if index % 2 else (digit * 2) % 9 if digit != 9 else 9) for index, digit in enumerate(reversed_ints[1:]))
    return (sum_of_digits * 9) % 10 == check_digit

if len(sys.argv) > 1:
    imei_number = sys.argv[1]
    if perform_luhn_check(imei_number):
        print(f"IMEI number is valid: {imei_number}")
        sys.exit(0)
    else:
        print(f"IMEI number failed validation {imei_number}")
        sys.exit(1)
else:
    print("Please pass IMEI number as parameter. \nExample: ./validate_imei <IMEI Here>")
    sys.exit(1)
