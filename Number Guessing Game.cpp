#include <iostream>
#include <cstdlib>  // For rand() and srand()
#include <ctime>    // For time()
using namespace std;

void playGame() {
    srand(time(0));  // Seed the random number generator
    int secret = rand() % 100 + 1;  // Random number between 1 and 100
    int guess;
    int attempts = 0;

    cout << "🎯 Guess the number (1 to 100):\n";

    do {
        cout << "Enter your guess: ";
        cin >> guess;
        attempts++;

        if (guess < secret)
            cout << "Too low! Try again.\n";
        else if (guess > secret)
            cout << "Too high! Try again.\n";
        else
            cout << "🎉 Correct! You guessed the number in " << attempts << " attempts.\n";

    } while (guess != secret);
}

int main() {
    char choice;

    do {
        playGame();
        cout << "Do you want to play again? (y/n): ";
        cin >> choice;
    } while (choice == 'y' || choice == 'Y');

    cout << "Thanks for playing!\n";
    return 0;
}
