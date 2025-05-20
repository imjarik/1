#include <iostream>


int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;

    std::cout << n << " = ";
    for (int i = 2; i * i <= n; ++i) {
        while (n % i == 0) {
            std::cout << i << " ";
            n /= i;
        }
    }
    if (n > 1) std::cout << n;
    return 0;
} 