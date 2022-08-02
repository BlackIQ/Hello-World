# Ruby cheatsheet number 2
# BEGIN and END statements

# This is the code stuff

print <<"Run"
This is running and stuff
Run

# Begin
# In "begin" we add some codes that are going to run at the first

BEGIN {
  puts "Begin part of app!"
  puts "- - - - -"
}

# End
# In "End" we add some codes that are going to run at the end

END {
  puts "- - - - -"
  puts "End part of app!"
}