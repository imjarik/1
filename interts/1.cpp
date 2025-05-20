#include <iostream>


int main() {
    int n;
    std::cout << "Enter n: ";
    std::cin >> n;

    for (int a = 1; a <= n; a++) {
        for (int b = a; b <= n; b++) {
            for (int c = b; c <= n; c++) {
                if (a * a + b * b == c * c)
                    std::cout << a << "^2 + " << b << "^2 = " << c << "^2" << std::endl;
            }
        }
    }
    return 0; 
}