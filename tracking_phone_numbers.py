import phonenumbers
from phonenumbers import geocoder, carrier, timezone

print("*" * 50)
entered_num = input("Enter a phone number with its country code : ")
try:
    # global phone_num
    phone_num = phonenumbers.parse(entered_num, None)  # An Object
except:
    print("Your entered number is not a real phone number")
    quit()

print()
print("The Information Of This Phone Number Is ........ ")
country_code = phone_num.country_code
national_num = phone_num.national_number
city_of_num = geocoder.description_for_number(phone_num, "en")
country_of_num = geocoder.country_name_for_number(phone_num, "en")
company_name = carrier.name_for_number(phone_num, "en")
time_zone = timezone.time_zones_for_number(phone_num)

# The Info
print()
print(f"- The Country Code Of This Phone Number = {country_code}")
print(f"- The National Phone Number = {national_num}")
print(f"- The Region Which This Number Belongs To = {city_of_num}")
print(f"- The Country Which This Number Belongs To = {country_of_num}")
print(f"- The Company Which This Number Belongs To = {company_name}")
print(f"- The Timezone Of This Number = {time_zone}")
print("*" * 50)