// Math | Random

import 'dart:math';

void main() {
  // Define a random
  final rng = Random();

  // Select an int in range 0 to 3
  final x = rng.nextInt(3);

  print(x);
}
