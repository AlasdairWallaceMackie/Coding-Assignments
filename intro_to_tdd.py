import unittest

class Testers(unittest.TestCase):

    def test_reverse1(self):
        self.assertEqual( reverse_list([1,2,3]), [3,2,1] )
    def test_reverse2(self):
        self.assertEqual( reverse_list([3,2,1]), [1,2,3] )
    def test_reverse3(self):
        self.assertEqual( reverse_list([1,4,7,4,3,6,7]), [7,6,3,4,7,4,1] )

    def test_palindrome1(self):
        self.assertEqual( is_palindrome("racecar"), True )
    def test_palindrome2(self):
        self.assertEqual( is_palindrome("buttz"), False )
    def test_palindrome3(self):
        self.assertEqual( is_palindrome("tacocat"), True )
    def test_palindrome4(self):
        self.assertEqual( is_palindrome("palindrome"), False )
    def test_palindrome5(self):
        self.assertEqual( is_palindrome("a man a plan a canal panama"), True )

    def test_Coin1(self):
        self.assertEqual( coins(1.00), "4 Quarters, 0 Dimes, 0 Nickels, 0 Pennies")
    def test_Coin2(self):
        self.assertEqual( coins(420.69), "1682 Quarters, 1 Dimes, 1 Nickels, 4 Pennies")
    def test_Coin3(self):
        self.assertEqual( coins(1.10), "4 Quarters, 1 Dimes, 0 Nickels, 0 Pennies")
    def test_Coin4(self):
        self.assertEqual( coins(1.01), "4 Quarters, 0 Dimes, 0 Nickels, 1 Pennies")
    def test_Coin5(self):
        self.assertEqual( coins(2.00), "8 Quarters, 0 Dimes, 0 Nickels, 0 Pennies")
    
    def test_factorial1(self):
        self.assertEqual( factorial(5), 120 )
    def test_factorial2(self):
        self.assertEqual( factorial(8), 40320 )
    def test_factorial3(self):
        self.assertEqual( factorial(3), 6 )

    def test_fibonacci1(self):
            self.assertEqual( fibonacci(5), 3 )
    def test_fibonacci2(self):
            self.assertEqual( fibonacci(9), 21 )
    def test_fibonacci3(self):
            self.assertEqual( fibonacci(1), 1 )
    def test_fibonacci4(self):
            self.assertEqual( fibonacci(0), 0 )

def reverse_list(list):
    for i in range( round(len(list)/2) ):
        swap_index = (len(list)-1) - i
        hold = list[swap_index]
        list[swap_index] = list[i]
        list[i] = hold
    return list

def is_palindrome(str):
    str = str.replace(" ", "") #Remove all spaces
    test_str = ""
    for i in range( len(str)-1, 0-1, -1 ):
        test_str += str[i]

    if test_str == str:
        return True
    else:
        return False

def coins(dollars_and_cents):
    
    dollars_and_cents = round(dollars_and_cents, 2)

    def test_coin_value(coin):
        nonlocal dollars_and_cents
        if dollars_and_cents >= coin.value:
            coin.amount += 1
            dollars_and_cents -= coin.value
            dollars_and_cents = round(dollars_and_cents, 2) #Have to round to 2 decimal places else it returns 0.000000000001
            return True
        return False

    class Coin:
        def __init__(self, name, value, amount=0):
            self.name = name
            self.value = value
            self.amount = amount

    quarters = Coin('Quarters', 0.25)
    dimes = Coin('Dimes', 0.10)
    nickels = Coin('Nickels', 0.05)
    pennies = Coin('Pennies', 0.01)

    while dollars_and_cents > 0:
        if test_coin_value(quarters) == True:
            pass
        elif test_coin_value(dimes) == True:
            pass
        elif test_coin_value(nickels) == True:
            pass
        elif test_coin_value(pennies) == True:
            pass
        # print(f"Remaining: {dollars_and_cents}")
    
    # print(f"{quarters.amount} Quarters, {dimes.amount} Dimes, {nickels.amount} Nickels, {pennies.amount} Pennies")
    return (f"{quarters.amount} {quarters.name}, {dimes.amount} {dimes.name}, {nickels.amount} {nickels.name}, {pennies.amount} {pennies.name}")

def factorial(num):
    if(num>1):
        num *= factorial(num-1)
    return num

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1

    f1 = 0
    f2 = 1
    for i in range(2, num):
        output = f1 + f2
        f1 = f2
        f2 = output
    return output


if __name__ == '__main__':
    unittest.main()