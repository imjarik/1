#include <iostream>
#include <string>


int main() {
    std::string name;
    std::cout << "name: ";
    std::getline(std::cin, name);
    std::cout << "Hello! " << name << std::endl;
    return 0;
}