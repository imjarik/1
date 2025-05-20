#include <iostream>
#include <iomanip>


int main() {
    double a, b;
    std::cout << "Enter two numbers: ";
    std::cin >> a >> b;

    std::cout << std::fixed << std::setprecision(12);
    std::cout << "Sum: " << a + b << std::endl;
    std::cout << "Dif: " << a - b << std::endl;
    std::cout << "Pro: " << a * b << std::endl;
    if (b != 0)
        std::cout << "Quotient: " << a / b << std::endl;
    else
        std::cout << "Cannot divide by zero!" << std::endl;

    return 0;
} 