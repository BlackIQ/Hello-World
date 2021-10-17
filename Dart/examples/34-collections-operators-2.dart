// Collections | For

void main() {
  // Set a extra list
  var exCities = ['London', 'Texas'];

  // Add exCities to cities | Way 1
  var cities1 = [
    'Dubay',
    'Berlin',
    'Tokyo',
  ];

  cities1.addAll(exCities);

  // Add exCities to cities | Collection-for
  var cities2 = [
    'Dubay',
    'Berlin',
    'Tokyo',
    for (var city in exCities) city,
  ];
}
