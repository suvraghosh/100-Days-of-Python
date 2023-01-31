'''Read this the code in main.py
Spot the problems 🐞.
Modify the code to fix the program.'''

# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

logo='''
  _____         _                           _                 ______  _            _                      
 |  __ \       | |                         (_)               |  ____|(_)          | |                     
 | |  | |  ___ | |__   _   _   __ _   __ _  _  _ __    __ _  | |__    _  ____ ____| |__   _   _  ____ ____
 | |  | | / _ \| '_ \ | | | | / _` | / _` || || '_ \  / _` | |  __|  | ||_  /|_  /| '_ \ | | | ||_  /|_  /
 | |__| ||  __/| |_) || |_| || (_| || (_| || || | | || (_| | | |     | | / /  / / | |_) || |_| | / /  / / 
 |_____/  \___||_.__/  \__,_| \__, | \__, ||_||_| |_| \__, | |_|     |_|/___|/___||_.__/  \__,_|/___|/___|
                               __/ |  __/ |            __/ |                                              
                              |___/  |___/            |___/                                               
'''

print(logo)

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)