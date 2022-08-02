// Lists | Part 1

void main() {
  // Create a list
  var names = ["Amir", "Ana", "Ali", "Nilo"];

  // Change one
  names[3] = "Hossein";

  // Get lenght of a list
  var len = names.length;

  // Print each of the list | 1
  for (var name in names) {
    print(name);
  }

  // Print each of the list | 2
  for (var i = 0; i < len; i++) {
    print(names[i]);
  }
}
