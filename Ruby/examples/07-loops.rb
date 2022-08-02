# Ruby cheatsheet number 7
# Loops

# While
while_i, while_j = 1, 5

while while_i < while_j do
  puts "While is running, i is #{while_i}"
  while_i += 1
end

puts "- - - - -"

# Until
until_i, until_j = 1, 5

until until_i > until_j do
  puts "Until is running, i is #{until_i}"
  until_i += 1
end

puts "- - - - -"

# For
for_n = 5

for n in 0..for_n
  puts "For is running, i is #{n}"
end

puts "- - - - -"

# Each
each_array = [ "name", "age", "born", "sruff" ]

each_array.each do |item|
  puts "Each is running, i is #{item}"
end

puts "- - - - -"

# Next, Break
for i in 0..5
  puts "Number is #{i}"
  if i != 4
    puts "Number is #{i}. Let's next!"
    next
  else
    puts "Number is #{i}. Let's break!"
    break
  end
end