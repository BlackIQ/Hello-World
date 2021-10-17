// Colloctions | If

void main() {
  // Create a list with 2 ways

  var addAna = true;
  var addNilo = false;

  // Way 1
  var people = ['Amir', 'Ali', 'Erfan', 'Arsham'];

  if (addAna) {
    people.add("Ana");
  }

  if (addNilo) {
    people.add("Nilo");
  }

  // Way 2 | Collection-If
  var names = [
    'Amir',
    'Ali',
    if (addAna) 'Ana',
    'Erfan',
    if (addNilo) 'Nilo',
    'Arsham',
  ];

  print(names);
}
