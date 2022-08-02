# Ruby cheatsheet number 8
# Methods

# Create a sample method
def method1
  puts "Method 1 is run"
end

# Create a method with value
def method2(name, age)
  puts "#{name} is #{age} years old!"
end

# Return value
def method3(a, b)
  a + b
end

# Run methods
method1

puts "- - - - -"

method2("Amir", 19)

puts "- - - - -"

puts method3(10, 20)