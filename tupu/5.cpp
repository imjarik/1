#include <iostream>


int main() {
    double points;
    std::cout << "(0.0 to 9.0): ";
    std::cin >> points;

    if (points >= 0.0 && points <= 4.4)
        std::cout << "2.0 " << std::endl;
    else if (points <= 5.2)
        std::cout << "3.0 " << std::endl;
    else if (points <= 6.2)
        std::cout << "3.5 " << std::endl;
    else if (points <= 7.2)
        std::cout << "4.0 " << std::endl;
    else if (points <= 8.2)
        std::cout << "4.5 " << std::endl;
    else if (points <= 9.0)
        std::cout << "5.0" << std::endl;
    else
        std::cout << "Invalid " << std::endl;

    return 0;
} 