#  this program that asks how many tickets for
#  each class of seats were sold, then displays the
#  amount of income generated from ticket sales
def main():
    class_a = get_class_a()
    class_b = get_class_b()
    class_c = get_class_c()
    total = class_c + class_b + class_a
    print('The total income generated from tickets sale'
          ' is $', format(total, ',.2f'), sep='')


#  the get_class_a function gets the number of tickets from user and
#  calculates the generated income from class A tickets
def get_class_a():
    seats_a = int(input('PLease enter the number of Class A seats tickets sold: '))
    selling_price_a = float(input('Please enter the selling price of each Class A ticket.'))
    price_a = seats_a * selling_price_a
    return price_a


#  the get_class_a function gets the number of tickets from user and
#  calculates the generated income from class B tickets
def get_class_b():
    seats_b = int(input('PLease enter the number of Class B seats tickets sold: '))
    selling_price_b = float(input('Please enter the selling price of each Class B tickets.'))
    price_b = seats_b * selling_price_b
    return price_b


#  the get_class_a function gets the number of tickets from user and
#  calculates the generated income from class C tickets
def get_class_c():
    seats_c = int(input('PLease enter the number of Class C seats tickets sold: '))
    selling_price_b = float(input('Please enter the selling price of each Class C tickets.'))
    price_c = seats_c * selling_price_b
    return price_c


main()
