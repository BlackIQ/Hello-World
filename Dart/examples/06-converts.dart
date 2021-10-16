// Convert variables

void main() {
  // Int to String and Dobule
  int a = 50;

  // Int to String
  String a_string = a.toString(); // Convert Int to String
  double a_double = a.toDouble(); // Convert Int to Double

  // Double to Int and String
  double b = 3.14;

  int b_int = b.toInt();
  String b_string = b.toString();

  // String to Int and Double
  String c = "10";

  int c_int = int.parse(c); // Convert String to Int
  double c_double = double.parse(c); // Convert String to Int
}
