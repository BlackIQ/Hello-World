// Lists | Part 2

void main() {
  // Create a list
  var names = ["Amir", "Ana", "Ali", "Nilo"];

  // Get lenght of the list
  print(names.length);

  // Get first of the list
  print(names.first);

  // Get last of the list
  print(names.last);

  // Is empty
  print(names.isEmpty);

  // Is not empty
  print(names.isNotEmpty);

  // Add a new item
  names.add("Meysam");

  // Add with index
  names.insert(1, "Arsham");

  // Remove with index
  names.removeAt(3);

  // Clear the list
  names.clear();

  // Check an item
  print(names.contains("Amir"));

  // Get item data with item
  print(names.indexOf("Ana"));
}
