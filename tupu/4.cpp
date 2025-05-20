#include <iostream>
#include <iomanip>


int main() {
    int mode;
    double temp;
    std::cout << "Enter conversion mode (1 = C→F, 2 = F→C): ";
    std::cin >> mode;
    std::cout << "Enter temperature: ";
    std::cin >> temp;

    const double absoluteZeroC = -273.15;
    const double absoluteZeroF = -459.67;

    bool tooCold = (mode == 1 && temp < absoluteZeroC) || (mode == 2 && temp < absoluteZeroF);

    if (tooCold) {
        std::cout << "Too cold to calculate!" << std::endl;
    } else {
        double result;
        if (mode == 1)
            result = temp * 9.0 / 5.0 + 32; // C → F
        else if (mode == 2)
            result = (temp - 32) * 5.0 / 9.0; // F → C
        else {
            std::cout << "Invalid mode!" << std::endl;
            return 1;
        }

        std::cout << std::fixed << std::setprecision(2);
        std::cout << "Converted temperature: " << result << std::endl;
    }

    return 0;
} 