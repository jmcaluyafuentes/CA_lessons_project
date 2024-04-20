def card_validation(card_num):
    # remove spaces and dashes
    card_num = card_num.replace(" ","").replace("-","")

    # validate visa card number
    if (card_num[0] == '4') and (len(card_num) in [13, 16]):
        card_type = 'Visa Card'
        valid_card = True

    # validate mastercard number
    elif (51 <= int(card_num[:2]) <= 55 or 2221 <= int(card_num[:4]) <= 2720) and (len(card_num) == 16):
        card_type = 'Mastercard'
        valid_card = True

    else:
        card_type = 'Invalid'
        valid_card = False

    print(f'Card type: {card_type}')
    return valid_card

# Main
cc_num = input('Please enter your Credit Card Number: ')

validated_card = card_validation(cc_num)

if validated_card:
    bank_num = cc_num[1:6]
    account_num = cc_num[6:-1]
    print(f'Bank number: {bank_num}')
    print(f'Account number: {account_num}')
else:
    print('Please enter the correct card number.')
