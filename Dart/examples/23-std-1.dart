// Std | Input, Output

import 'dart:io';

void main() {
  stdout.write("What is your name? ");
  final name = stdin.readLineSync();

  print("Welcome $name");
}
