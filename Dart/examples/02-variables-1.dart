// Variables & print variables

void main() {
  // Variables
  String name = "Amirhossein"; // String
  int age = 18; // Int
  double height = 1.60; // Double
  bool male = true; // Boolean

  // Append
  print("Name is " + name); // First way
  print("Name is $name"); // Second way

  // Example
  print(
      "Name is $name and is $age. Also has $height height. Male status is $male.");

  // Operators in $
  print("One plus the age is ${age + 1}"); // We use ${} to do something

  // Mixed appends
  double temp = 27.5;
  // print("Tempture is $tempC"); In this type, C mixs with variable
  print("Tempture is ${temp}C"); // In this way, boot are mixed with no errors
}
