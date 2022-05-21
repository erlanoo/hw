import re
class  ValidCarNumber:

   ValidCarnumber = input("введите номер машины например 01KG777BAD:")
   is_valid = re.search(r"(0[0-9]{1})KG([0-9]{3})([A-Z]{3})", ValidCarnumber)
   re.search(r"([0-9]{2})KG([0-9]{4})([A-Z]{3})", ValidCarnumber)
   re.search(r"(0[0-9]{1})KG([0-9]{3})([A-Z]{2})", ValidCarnumber)
   print(is_valid)

   if not is_valid:
       print("invalid CarNumbers, номер не валидный!")
   elif ValidCarnumber[is_valid.start():is_valid.end()] == ValidCarnumber:
       print("CarNumbers valid!, номер валидный!")