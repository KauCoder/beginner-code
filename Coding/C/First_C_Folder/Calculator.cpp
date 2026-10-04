// ---------- SIMPLE CALCULATOR PROGRAM ----------
#include <iostream>
#include <string>

void calculator() {
    // ---------- CALCULATING ----------
    int firstNum;
    std::string oper;
    int secondNum;


    std::cout << "First number > ";
    std::cin >> firstNum;

    std::cout << "Operation > ";
    std::cin >> oper;

    std::cout << "Second Number > ";
    std::cin >> secondNum;

    if (oper != "") {
        if (oper == "+") {
            int sum = firstNum + secondNum;
            std::cout << sum << std::endl;
        }
        else if (oper == "-") {
            int difference = firstNum - secondNum;
            std::cout << difference << std::endl;
        }
        else if (oper == "*") {
            int product = firstNum * secondNum;
            std::cout << product << std::endl;
        }
        else if (oper == "/") {
            if (secondNum == 0) {
                std::cout << "WARNING: Division by zero is not possible:\n0" << std::endl;
            } else {
                int quotient = firstNum / secondNum;
                std::cout << quotient << std::endl;
            }
        }
        else if (oper != "+" || "-" || "*" || "/") {
            std::cout << "WARNING: Invalid Operation.\n0" << std::endl;
        }
    }

    else {
        std::cout << "ERROR" << std::endl;
    }
}

int main() {
    // ---------- RUNNING UNTIL USER QUITS ----------
    std::string restart;
    do {
        calculator();
        std::cout << "Would you like to perform another calculation (y/n)? ";
        std::cin >> restart;
    } while (restart == "y");

    return 0;
}