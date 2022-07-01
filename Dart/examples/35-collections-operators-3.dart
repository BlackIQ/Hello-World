// Collections | Spreads

void main() {
  // Set a extra list
  var exCountries = ['London', 'Texas'];

  // Add exCountries to countries1 | Way 1 - Collections for
  var countries1 = [
    'Dubay',
    'Berlin',
    'Tokyo',
    for (var city in exCountries) city,
  ];

  // Add exCountries to countries2 | Way 2 - Spreads
  var countries2 = [
    'Dubay',
    'Berlin',
    'Tokyo',
    ...exCountries,
  ];
}
