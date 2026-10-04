#include <iostream>
#include <random>

int main() {
    int num;
    int tries = 0;
    int guess;

    std::cout << "Welcome to the number guessing game!\n";
    
    std::random_device rd; 
    std::mt19937 gen(rd()); 
    std::uniform_int_distribution<int> distr(1, 100);
    num = distr(gen);
    
    while (true) {
        std::cout << "What is your guess (1/100)? ";
        std::cin >> guess;
        tries++;

        if (guess != num && 1 <= guess && guess <= 100) {
            if (guess < num) {
                std::cout << "Too low!\n";
                continue;
            }
            if (guess > num) {
                std::cout << "Too high!\n";
                continue;
            }
        }
        else if (guess < 1 || guess > 100) {
            std::cout << "Number out of range.\n";
            continue;
        }
        else {
            std::cout << "YOU WON!!! The number was: " << num << ", and you guessed it in " << tries << " attempts!\n";
            break;
        }
    }

    return 0;
}