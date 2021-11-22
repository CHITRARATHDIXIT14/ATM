data = [['chitrarath','ID001',90000],
        ['hetanshi','ID002',10000],
        ['hardik','ID003',1000]]
def checkblnce(rec) :
    print('check in balance')
    for i in data :
        if i[1] == rec :
            print('Your account balance is ' , i[2])
def withdraw(rec) :
    print('withdraw money')
    amount = int(input('Enter the amount you want to  withdraw'))
    for i in data :
        if i[1] == rec :
            balance = i[2] - amount
            print('Your current account balance is ' , balance)
            

def cashDepositer(rec) :
    print('Desposit money')
    amount1 = int(input('Enter the amount you want to deposit'))
    for i in data:
        if i[1] == rec :
            balance1 = i[2] + amount1
            print( str(i[0]) + ' Your current account balance is ' + str(balance1))


print('Welcome to the CHITRARATH ATM')
print('Press 1 for balance enquiry')
print('Press 2 for cash Withdaw ')
print('Press 3 to Deposit Money')

number = int(input('Enter your choice'))
id = input('Enter your bank ID for example : ZZ00* ')

if number==1:
    checkblnce(id)
elif number==2:
    withdraw(id)
else :
    cashDepositer(id)

# mam please repeat what you say ?




