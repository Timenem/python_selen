"""
You are given a (small) check book as a - sometimes - cluttered (by non-alphanumeric characters) string:

"1000.00
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10"

The first line shows the original balance. Each other line (when not blank) gives information: check number, category, check amount. (Input form may change depending on the language).

First you have to clean the lines keeping only letters, digits, dots and spaces.

Then return a report as a string (underscores show spaces -- don't put them in your solution. They are there so you can see them and how many of them you need to have):

"Original_Balance:_1000.00
125_Market_125.45_Balance_874.55
126_Hardware_34.95_Balance_839.60
127_Video_7.45_Balance_832.15
128_Book_14.32_Balance_817.83
129_Gasoline_16.10_Balance_801.73
Total_expense__198.27
Average_expense__39.65"

On each line of the report you have to add the new balance and then in the last two lines the total expense and the average expense. So as not to have a too long result string we don't ask for a properly formatted result.

"""


import re
import statistics


def balance(book: str) -> str:
    header = ''
    sentence = ''
    start_balance = float(format(
        float(str(re.sub(r'[^\w]', ' ', ''.join([i for i in book.split(sep='\n')[0]]))).strip().replace(' ', '.')),
        '.2f'))
    total_expense = 0
    current_balance = start_balance
    outer_list = [i for i in book.split(sep='\n')[1::]]
    check_numbers = [str(i).split(sep=' ')[0] for i in outer_list]
    category = [re.sub(r'[^\w]', ' ', str(i).split(sep=' ')[1]).strip() for i in outer_list]
    price = [format(float(re.sub(r'[^\w]', ' ', str(i).split(sep=' ')[2]).strip().replace(' ', '.')), '.2f') for i in
             outer_list]
    avg_expence = round(statistics.mean(
        [float(re.sub(r'[^\w]', ' ', str(i).split(sep=' ')[2]).strip().replace(' ', '.')) for i in outer_list]), 2)
    for i in range(len(check_numbers)):
        current_balance -= float(price[i])
        total_expense += float(price[i])
        sentence += f"{check_numbers[i]} {category[i]} {price[i]} Balance {format(current_balance, '.2f')}\r\n"
        header = f"{'Original Balance'}: {format(start_balance, '.2f')}\r\n{sentence}"
    total_expense = str(format(total_expense,'.2f'))
    return (header+'Total expense  '+total_expense+'\r\n'+'Average expense  '+str(avg_expence))

