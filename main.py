import phonenumbers
from phonenumbers import timezone, geocoder,carrier
number = input("enter your number: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
sim = carrier.name_for_number(phone ,"en")
regis = geocoder.description_for_number(phone , "en")
print(time)
print(sim)
print(regis)