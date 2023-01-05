#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

#defining values to variable
    a = 10
    b = 5

#printing result for the addition
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    
    #printing result for subtraction
    print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))

    #printing result for multiplication
    print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))

    #printing result for division
    print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
