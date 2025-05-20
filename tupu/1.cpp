#include <iostream>
#include <iomanip>


int main() {
    char ch;
    std::cout << "Enter a character: ";
    std::cin >> ch;

    std::cout << "Character: " << ch << std::endl;
    std::cout << "ASCII (decimal): " << static_cast<int>(ch) << std::endl;
    std::cout << "ASCII (hex): " << std::hex << static_cast<int>(ch) << std::endl;

    return 0;
} 