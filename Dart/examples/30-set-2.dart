// Set | Part 2

void main() {
  // Create an euCountries set
  var euCounties = {'Italy', 'Russa', 'UK'};

  // Create an asCountries set
  var asCounties = {'Indea', 'Russa', 'UEA'};

  // Get non repeted items
  print(euCounties.union(asCounties));

  // Get same items
  print(euCounties.intersection(asCounties));

  // Get differences
  print(euCounties.difference(asCounties));
}
