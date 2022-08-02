# Ruby cheatsheet number 13
# Iterators

# Collect an array
a = ["amir", "ali", "mamad"]
b = Array.new
b = a.collect{|item| item}

puts b

# Collect and do an action
aa = [1, 2, 3]
bb = Array.new
bb = aa.collect{|item| item * 2}

puts bb