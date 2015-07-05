#import re
#card_number='5263-3065-0122-0017'


def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10


if len(card_number)==19:
### 16 digits
#check the format
    pattern16=re.compile(r'^\d{4}-\d{4}-\d{4}-\d{4}')
    match16=pattern16.search(card_number)
    if match16!=None:
        print "correctly formatted 16 digits (Visa or Mastercard)"
    else:
        print "uncorrectly formatted 16 digits"
 # to remove the hyphens
    b16=bytearray(card_number)
    for n in range(1,4):
        del b16[n*4]
    card_number=str(b16)
elif len(card_number)==17:
    ###15 digits
    pattern15=re.compile(r'^\d{4}-\d{6}-\d{5}')
    match16=pattern15.search(card_number)
    if match15!=None:
        print "correctly formatted 15 digits (Amex)"
    else:
        print "uncorrectly formatted 15 digits"
    #remove hyphens
    b15=bytearray(card_number)
    del b15[4]
    del b15[11]
    card_number=str(b15)
else:
    "Not a credit card number"
#check the luhn algorithm
if luhn_checksum(card_number) == 0:
    print "valid number"    
else:
    print "not valid number"

