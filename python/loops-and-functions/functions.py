# def hello():
#     print(f'Hello {name}')

# def goodbye():
#     global name
#     print('Goodbye')
#     name = 'Mark'
    
# # Main
# name = 'John'
# goodbye()
# hello()

#############################
# def hello(name):
#     print(f'Hello {name}')

# def goodbye():
#     global name
#     print('Goodbye')
#     name = 'Mark'
    
# # Main
# goodbye()
# hello('John')

#############################
# def hello(name, age): # one or more parameters (positional parameters)
#     x = 5
#     print(f'Hello {name}, you are {age} years old!')

# def goodbye():
#     global name
#     print('Goodbye')
#     name = 'Mark'
    
# # Main
# goodbye()
# hello('John', 36)

#############################
# def hello(name, age):
#     x = 5
#     print(f'Hello {name}, you are {age} years old!')

# def goodbye():
#     global name
#     print('Goodbye')
#     name = 'Mark'
    
# # Main
# goodbye()
# hello(age=36, name='John') # keyword arguments

#############################
# subtotal = float(input('Subtotal: $'))
# total = round(subtotal * 1.1, 3) # a float has a precision decimal places. Meaning 3 is the maximum number of decimal places.
# print(f'Total: ${total}')
# the example in class was 100 for subtotal

#############################
# subtotal = float(input('Subtotal: $'))
# total = subtotal * 1.1 # a float has a precision decimal places. Meaning 3 is the maximum number of decimal places.
# print(f'Total: ${total: .2f}') # ': .2f' means format total variable with float with 2 decimal places
# the example in class was 100 for subtotal

#############################
# def add_gst(amount):
#     total = amount * 1.1
#     return total

# subtotal = float(input('Subtotal: $'))
# grand_total = add_gst(subtotal) # this is more readable in comparison to below code
# print(f'Total: ${grand_total: .2f}')

#############################
# def add_gst(amount):
#     total = amount * 1.1
#     return total

# subtotal = float(input('Subtotal: $'))
# print(f'Total: ${add_gst(subtotal): .2f}') # above code is more readable

#############################
def add_tax(amount, tax_rate=0.1): # 0.1 is default value since most of the time it is gst tax that is being computed, the rest are other kind of tax
    total = amount * (1 + tax_rate)
    return total

subtotal = float(input('Subtotal: $'))
grand_total = add_tax(subtotal)
print(f'Total (inc company tax): ${grand_total: .2f}')