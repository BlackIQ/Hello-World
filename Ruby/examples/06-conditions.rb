# Ruby cheatsheet number 6
# Conditions

username = "Amir"
password = "hello"

# If, Else
if username == "Amir"
  if password == "hello"
    puts "User is authenticated"
  else
    puts "Password is wrong"
  end
else
  puts "Username is wrong"
end

puts "- - - - -"

age = 19

# Unless
unless age > 20
  puts "Age is less than 20"
else
  puts "Age is greater than 20"
end

puts "- - - - -"

# Case
action = "login"
case action
when "login"
  puts "Login user"
when "logout"
  puts "Logout user"
else
  puts "Action not found"
end