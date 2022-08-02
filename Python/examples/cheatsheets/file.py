with open("my_file.txt", 'a') as file: # if file not made, make it and then open:
  file.read() # read the file
  for i in file.readline():
    print(i) # read line by line
    
  file.write("Hello, World!") # write some text in file
  
  # with close file automaticly
