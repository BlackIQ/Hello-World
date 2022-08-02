// Loop | Break and Continue

void main() {
  for (var i = 0; i < 10; i++) {
    print(i);
    if (i == 5) {
      print("We got 5");
      break;
    }
    if (i % 2 == 0) {
      print("Number can be devied to 2");
      continue;
    }
  }
}
