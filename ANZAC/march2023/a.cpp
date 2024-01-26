#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<bool> isFib(200,false);

    isFib[0] = true;
    int i = 0, j = 1;
    for (int i = 1; i < 10; i++) {
        isFib[j]= true;
        int temp = i + j;
        i = j;
        j = temp;
    }

    for (int i = 0; i < n; i++) {
        if (isFib[i] == true) {
            std::cout << "fizz";
        } else {
            std::cout << "buzz";
        }
    }
    std::cout << std::endl;

    return 0;
}