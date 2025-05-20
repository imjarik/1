#include <iostream>
#include <iomanip>


int main() {
    double R;
    const double pi = 3.14;

    std::cout << "radius: ";
    std::cin >> R;

    double area = pi * R * R;
    double length = 2 * pi * R;

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Area: " << area << std::endl;
    std::cout << "Circume: " << length << std::endl;

    return 0;
}