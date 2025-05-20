#include <iostream>
#include <vector>


bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; ++i)
        if (n % i == 0) return false;
    return true;
}

int main() {
    int n;
    std::cout << "Enter n: ";
    std::cin >> n;

    for (int i = n; i <= 2 * n - 2; ++i) {
        if (isPrime(i) && isPrime(i + 2))
            std::cout << "(" << i << ", " << i + 2 << ")" << std::endl;
    }
    return 0;
} 