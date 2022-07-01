import 'dart:io';
import 'dart:math';

enum Move { rock, paper, scissors }

void main() {
  final rang = Random();
  while (true) {
    stdout.write("What is your move? [r, p, s] ");
    final input = stdin.readLineSync();

    if (input == 'r' || input == 'p' || input == 's') {
      var playerMove;
      if (input == 'r') {
        playerMove = Move.rock;
      } else if (input == 'p') {
        playerMove = Move.paper;
      } else {
        playerMove = Move.scissors;
      }

      final random = rang.nextInt(3);
      final aiMove = Move.values[random];

      print("You select: $playerMove");
      print("Ai selects: $aiMove");

      if (playerMove == aiMove) {
        print("Draw");
      } else if (playerMove == Move.rock && aiMove == Move.scissors ||
          playerMove == Move.paper && aiMove == Move.rock ||
          playerMove == Move.scissors && aiMove == Move.paper) {
        print("You win");
      } else {
        print("You lose");
      }
    } else if (input == 'q') {
      break;
    } else {
      print("Invalid input");
    }
  }
}
