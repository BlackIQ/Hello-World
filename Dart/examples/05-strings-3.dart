// Find & Replcae

void main() {
  String you = "I love you";

  // Checking
  print(you.contains("you")); // This is true. $you has you in it

  String langs = "I love Dart. I love Js. I love Python";

  // Replce current words with new words
  String new_langs = langs.replaceAll("love", "hate"); // Replced love to hate.

  print(new_langs);
}
