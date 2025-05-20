#include <iostream>
#include <vector>


int main() {
    int n;
    std::cout << "Enter number of rows: ";
    std::cin >> n;

    std::vector<std::vector<int>> pascal(n);

    for (int i = 0; i < n; ++i) {
        pascal[i].resize(i + 1);
        pascal[i][0] = pascal[i][i] = 1;
        for (int j = 1; j < i; ++j)
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j];

        for (int j = 0; j <= i; ++j)
            std::cout << pascal[i][j] << " ";
        std::cout << std::endl;
    }

    return 0; 
}