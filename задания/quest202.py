"""
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

Examples:
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False
"""

import  datetime 

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    form = "%B %d %Y"
    current_date= datetime.datetime.strptime(current_date.replace(',',''),form)
    expiration_date= datetime.datetime.strptime(expiration_date.replace(',',''),form)
    return  entered_code is correct_code and current_date <=expiration_date
