# Ruby cheatsheet number 1
# Print stuff in cli

# Print single lines
puts "Hello Jupiter!"
puts 1
puts true

puts "- - - - -"

# Print multi lines
print <<"EOF";
Line one
Second line
EOF

puts "- - - - -"

# Execute codes in cli | One
print <<`EOF`
echo "Hello"
echo "Bye"
EOF

puts "- - - - -"

# Execute codes in cli | Two
print <<`EOF`
ls
ruby --version
EOF

puts "- - - - -"

# Print multi-multi line

# Here we add some parts and in each one we add lines
# We can have 3 or 5 items and 3 or 5 lines!
print <<"One", <<"Two"
Text one & Line one
Text one & Line two
One
Text two & Line one
Text two & Line two
Two