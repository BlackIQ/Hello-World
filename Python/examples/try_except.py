# It's good for handling errors
try: # use "try" and "except" keywords
  # your code to be handled
  pass
except Exception as err: # you can see your error as Exception object and we put it in a variable named `err`
  print("You have an error:", err) # print error

# this example for importing a module:
try:
  import os
  import requests
except Exception as err:
  print("You have an error!")
  user_answer = input("Do you want to install \"requests\" library?[Y/n]")
  
  if user_answer == "n" or "N":
    print("so, install that!")
  else:
    print("Installing Library . . .")
    os.system("pip3 install reqests")
