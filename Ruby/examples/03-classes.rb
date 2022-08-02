# Ruby cheatsheet number 3
# Classes

# Define a global variable
$year = 2022

# Define a class
class Person
  # Add initial method
  def initialize(name, born)
    # Add variables
    @name = name
    @age = born
  end

  # Add a sample method
  def age
    # Return something and using global variable
    $year - @age
  end

  # Create a function with params
  def friend(friend)
    # Define friend
    @friend = friend

    # Print with variables
    puts "#{@name} is friend with #{@friend}."
  end
end

# initial a class with values
amir = Person. new("Amir", 2003)

# using class method and add it to a value
age = amir.age

# Print age
puts age

# Use a class method with params
amir.friend("Fatemeh")