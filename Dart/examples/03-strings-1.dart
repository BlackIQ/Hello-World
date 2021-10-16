// Strings

void main() {
  // print('Now I'm feeling great!'); This is wrong. We use same qoute in a center of it
  print('Now I\'m feeling good!'); // Now it is solved. Use \ before qoute.
  print("Now I'm feeling good!"); // This is way no. 2.

  // Special charectors
  print("\\"); // Output is \
  print("\$"); // Output is $

  // print("Dir is: \home\user\Downloads"); This is wrong.
  print("Dir is: \\home\\user\\Downloads"); // Now it prints \

  // Print with out details of special chars
  print(r"The home worth $1500000."); // Now, $ is not as a variable
}
