def card_validation(visa_num):
    if visa_num[0] == '4':
        if len(visa_num) == 13 or len(visa_num) == 16:
            return True
        else:
            return False
    else:
        return False

# Main
cc_num = input('Please enter your Visa Card Number: ')
cc_num = cc_num.replace(" ","") # remove spaces
cc_num = cc_num.replace("-","") # remove dashes

valid_card = card_validation(cc_num)

if valid_card:
    bank_num = cc_num[1:6]
    account_num = cc_num[6:-1]
    print('It is a valid visa card number.')
    print(f'Bank number: {bank_num}')
    print(f'Account number: {account_num}')
else:
    print('Sorry the number you entered is invalid.')
