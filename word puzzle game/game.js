const wordList = ["apple", "banana", "cherry", "date"]; // Replace with your own word list

const stages = [
  `
    +---+
        |
        |
        |
       ===
  `,
  `
    +---+
    O   |
        |
        |
       ===
  `,
  `
    +---+
    O   |
    |   |
        |
       ===
  `,
  `
    +---+
    O   |
   /|   |
        |
       ===
  `,
  `
    +---+
    O   |
   /|\\  |
        |
       ===
  `,
  `
    +---+
    O   |
   /|\\  |
   /    |
       ===
  `,
  `
    +---+
    O   |
   /|\\  |
   / \\  |
       ===
  `
];

const clear = () => {
  // Replace this with the code to clear the output between guesses in your specific HTML implementation
};

const getRandomWord = () => {
  return wordList[Math.floor(Math.random() * wordList.length)];
};

const displayWord = (word, guessedLetters) => {
  const displayedWord = word
    .split("")
    .map((letter) => (guessedLetters.includes(letter) ? letter : "_"))
    .join(" ");
  return displayedWord;
};

const hangman = () => {
  console.log("Welcome to Hangman!");

  const chosenWord = getRandomWord();
  const wordLength = chosenWord.length;
  let display = "_".repeat(wordLength).split("");

  let lives = stages.length - 1;
  let gameIsFinished = false;
  let guessedLetters = [];

  while (!gameIsFinished) {
    const guess = prompt("Guess a letter:").toLowerCase();
    clear();

    if (guessedLetters.includes(guess)) {
      console.log(`You've already guessed ${guess}`);
    } else {
      guessedLetters.push(guess);

      if (chosenWord.includes(guess)) {
        for (let position = 0; position < wordLength; position++) {
          if (chosenWord[position] === guess) {
            display[position] = guess;
          }
        }
        console.log(displayWord(chosenWord, guessedLetters));

        if (!display.includes("_")) {
          gameIsFinished = true;
          console.log("You win.");
        }
      } else {
        lives--;
        console.log(`You guessed ${guess}\nThat's not in the word.\nYou lose a life. ${lives} lives left`);
        console.log(stages[lives]);

        if (lives === 0) {
          gameIsFinished = true;
          console.log(`You lose.\nThe word was ${chosenWord}`);
        }
      }
    }
  }
};

hangman();
