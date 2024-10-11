input_month = input()
input_day = int(input())

# Check if the input day is valid
if input_day < 1 or input_day > 31:
    print('Invalid')
else:
    if (input_month == 'December' and input_day >= 21) or input_month in ['January', 'February'] or (input_month == 'March' and input_day < 20):
        print('Winter')
    elif (input_month == 'March' and input_day >= 20) or input_month in ['April', 'May'] or (input_month == 'June' and input_day < 21):
        print('Spring')
    elif (input_month == 'June' and input_day >= 21) or input_month in ['July', 'August'] or (input_month == 'September' and input_day < 22):
        print('Summer')
    elif (input_month == 'September' and input_day >= 22 and input_day != 31) or input_month in ['October', 'November'] or (input_month == 'December' and input_day < 21):
        print('Autumn')
    else:
        print('Invalid')