# Ruby cheatsheet number 10
# Arrays | 2

# Create test array
test = Array.new(20)

# Get length and size
puts test.length # 20
puts test.size # 20

# Create array with length and item
test2 = Array.new(10, "Amir")
puts test2

# Create array like a loop
test3 = Array.new(0..10)
puts test3

# Create array with []
test4 = Array.[](1, 2, 3, 4, 5)
test5 = Array[1, 2, 3, 4, 5]