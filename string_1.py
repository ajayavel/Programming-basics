first_name="sikkal"
last_name="sanmuga"
print(first_name.capitalize())
print(last_name.find("an"))
print(last_name.find("na"))
print(last_name[3:])

import re

five_digit_zip="85281"
nine_digit_zip="94536-4539"
phone_number="510-770-4744"


print(re.search(r"\d{5}",five_digit_zip))
print(re.search(r"\d{5}",nine_digit_zip))
print(re.search(r"\d{5}",phone_number))

miles=input("Enter distance in miles:")

print(f"The distance in kms is {float(miles)*1.609344}")