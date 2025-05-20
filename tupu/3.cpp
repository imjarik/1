#include <iostream>
#include <iomanip>


int main() {
    int number;
    std::cout << "Enter an integer: ";
    std::cin >> number;

    std::cout << "Even? " << (number % 2 == 0 ? "YES" : "NO") << std::endl;
    std::cout << "Divisible by 8? " << (number % 8 == 0 ? "YES" : "NO") << std::endl;
    std::cout << "Divisible by 16? " << (number % 16 == 0 ? "YES" : "NO") << std::endl;

    std::cout << "Octal: " << std::oct << number << std::endl;
    std::cout << "Hexadecimal: " << std::hex << number << std::endl;

    return 0;
} 