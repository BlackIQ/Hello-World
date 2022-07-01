// Enum

// Define an Enum. First must be capital

enum Medals {
  gold,
  silver,
  bronze,
  noMedal,
}

void main() {
  const stage = Medals.bronze;

  switch (stage) {
    case Medals.gold:
      print("Gold!");
      break;
    case Medals.silver:
      print("Silver!");
      break;
    case Medals.bronze:
      print("Bronze!");
      break;
    case Medals.noMedal:
      print("Sorry, You are not in first 3 :(");
      break;
  }
}
