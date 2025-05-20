#include <iostream>

int main() {
    double A, B, C;
    std::cout << "A: ";
    std::cin >> A;
    std::cout << "B: ";
    std::cin >> B;
    std::cout << "C: ";
    std::cin >> C;

    double p = 2 * (A*B + B*C + A*C);
    double v = A * B * C;

    std::cout << "Surface Area: " << p << std::endl;
    std::cout << "Volume: " << v << std::endl;

    return 0;
}