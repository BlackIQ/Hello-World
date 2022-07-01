// Variables | Dynamic

void main() {
  var x = "Amir";
  // x = true; // We can not change a var, const, final and other data types

  // We use dynamic to be able to change data type
  dynamic y = 10; // Now is int
  y = true; // Now is boolean
  y = "Amir"; // Now is string
}
