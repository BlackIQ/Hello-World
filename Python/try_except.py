# It's good for handeling error
try: # use "try" and "except" keyword
  # your code to handel
except Exception as err: # you can see your error in Exception but we creat a variabel as "err"
  print("You have an error:", err) # print error
  
# this exampel for installing library:
try:
  import os
  import requests
except Exception as err:
  print("You have an error!")
  user_answer = input("Do you want to install \"requests\" library?[Y/n]")
  
  if user_answer == "n" or "N":
    print("so, install that!")
  else:
    print("Installing Linrary . . .")
    os.system("pip3 install reqests")
