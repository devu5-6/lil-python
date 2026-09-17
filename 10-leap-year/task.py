def is_leap_year(x):
    # Write your code here. 
    # Don't change the function name.
    if (x%4==0):
        if (x%100==0):
            if (x%400==0):
                print('True')
            else:
                print('False')
        else:
            print('True')
    else:
        print('False')

is_leap_year(1989)