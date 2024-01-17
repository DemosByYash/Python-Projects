# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:23:41 2023

@author: yash
"""

# Calculator - Table/Exponent/Odd-Even

loop_x = 'y'
while loop_x == 'y':
    #edit name
    pass
    print('Welcome To Calculator')
    print('Instructions:\n1 for Table\n2 for Exponent\n3 for Odd-Even\n4 for Exit')
    calc_select = int(input('Type the number here: '))
    if calc_select == 1:
        print('You have chosen Table Calculator')
        num_t1 = int(input('Type a digit to get it\'s table: '))
        for digits_t in range(1,11):
            print(f'{num_t1} x {digits_t} =', num_t1 * digits_t)
        loop_x = input('Type y to restart or n to exit: ')
    
        pass
    # Exponent Calculator
    elif calc_select == 2:
        print('You have chosen Exponent Calculator')
        num_e1 = int(input('Type a digit(base): '))
        num_e2 = int(input('Type it\'s power: '))
        print('answer: ',num_e1 ** num_e2)
        loop_x = input('Type y to restart or n to exit: ')
    
        pass
    #Odd-Even Calculator
    elif calc_select == 3:
        num_o1 = int(input('type a digit: '))
        if num_o1 % 2 == 0:
            print(f'{num_o1} is an even number') 
        else:
            print(f'{num_o1} is an odd number')
        loop_x = input('Type y to restart or n to exit: ')
    else:
        print('exited successfully')
        break 
else:
    print('thankyou for using, exited successfully')