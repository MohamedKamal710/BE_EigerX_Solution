#1 
def priceCheck( products ,  productPrices ,  productSold , soldPrice):
    prices = {}
    for i ,pro in enumerate(products):
        prices[pro] = float(productPrices[i])
    errors = 0
    for i , pro in enumerate(productSold):
        if(soldPrice[i] != prices[pro]):
            errors+=1
    return errors


def test_PriceCheck():
    assert priceCheck(['eggs', 'milk', 'cheese'] , [2.89, 3.29, 5.79],['eggs', 'eggs', 'cheese', 'milk'],[2.89, 2.99, 5.97, 3.29]) == 2 , 'should be 2'
    assert priceCheck(['rice', 'sugar', 'wheat', 'cheese'] , [16.89, 56.92, 20.89, 345.99],['rice', 'cheese'],[18.99, 400.89]) == 2 , 'should be 2'


test_PriceCheck()


#2

"Select Name as 'Department_Name' , COUNT(*) as 'Number_Of_Employees' from Department as D inner join Employee as E on E.Dept_ID = D.ID group by Deparment_Name order by Number_Of_Employees , Department_Name Asc"


#3
def recursiveDigitSummer(number):
    if(number < 10): return number
    x = number % 10
    return recursiveDigitSummer(int(number / 10)) + x

def test_RecursiveDigitSummer():
    assert recursiveDigitSummer(2347623) == 27 , "should be 27"

test_RecursiveDigitSummer()


#4

def recursive_sequence(inputs , i , max , counter):
    x = int(inputs[i])
    if x == 0 : return (max , counter)
    if x > max:
        max = x
        counter = 1
    elif x == max:
        counter+=1 
    return recursive_sequence(inputs , i + 1, max , counter)


def rec_num_seq(sequence):
    inputs = sequence.split(" ")
    return recursive_sequence(inputs , 0 , float('-inf'), 0)


def test_sequence():
    assert rec_num_seq('1 5 42 -376 5 19 5 3 42 2 0') == (42,2) , "should be (42,2)"

test_sequence()