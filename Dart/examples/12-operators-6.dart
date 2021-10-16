// Operators | Logical

void main() {
  // If one side is true, returns true
  print(5 < 2 || 5 < 7);

  // If both sides are true, returns true
  print(2 < 5 && 'Hi' == 'Hi');

  // Example
  String email = "me@blackiq.ir";
  print(email.isNotEmpty && email.contains("@"));
}
