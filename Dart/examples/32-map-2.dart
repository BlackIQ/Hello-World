// Map | Part 2

void main() {
  // Create a map
  var amir = {
    'name': 'Amirhossein',
    'age': 18,
    'height': 1.6,
  };

  // Create a map with specefic data type | Way 1
  Map<String, dynamic> you = {
    'name': 'Ali',
    'age': 6,
    'height': 1.1,
  };

  // Create a map with specefic data type | Way 2
  var he = <String, dynamic>{
    'name': 'Erfan',
    'age': 19,
    'height': 1.7,
  };

  // Get data as String | Way 1
  var name = he['name'] as String;

  // Get data as String | Way 2
  String ali = you['name'];

  // Get all keys with for
  for (var key in he.keys) {
    print(key);
  }

  // Get value of the key with for | Way 1
  for (var value in he.values) {
    print(value);
  }

  // Get value of the key with for | Way 2
  for (var key in he.keys) {
    print(he[key]);
  }

  // Using enties
  for (var entry in amir.entries) {
    print('${entry.key}: ${entry.value}');
  }
}
