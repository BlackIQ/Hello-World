# Ruby cheatsheet number 4
# Arrays | 1

# Create just a list
names = [ "Amir", "Fatemeh", "Mohammad", "Ali" ]

# For loop in a list
names.each do | name |
  # Print name
  puts name
end

puts "- - - - -"

# Create a JSON array
person = {
  "name" => "Amir",
  "age" => 19,
  "born" => "Nov 20 2003",
  "city" => "Tehran",
}

# For loop in person with key and value
person.each do |key, value|
  # Print key and value
  puts "#{key} is #{value}"
end

puts "- - - - -"

(0..10).each do |i|
  puts "Running for #{i} time"
end