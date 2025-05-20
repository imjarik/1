#include <iostream>

int main() {
    int a, b;
    std::cout << "a ";
    std::cin >> a;
    std::cout << "b ";
    std::cin >> b;

    std::cout << "Sum: " << a + b << std::endl;
    std::cout << "Dif: " << a - b << std::endl;
    std::cout << "Pr: " << a * b << std::endl;

    return 0;
}