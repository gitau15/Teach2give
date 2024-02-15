//Reverse Integer
#include <iostream>

int reverseInteger(int num) {
    int reversed = 0;
    while (num != 0) {
        int digit = num % 10;
        reversed = reversed * 10 + digit;
        num /= 10;
    }
    return reversed;
}

int main() {
    int num;
    std::cout << "Enter an integer: ";
    std::cin >> num;
    
    int reversedNum = reverseInteger(num);
    
    std::cout << "Reversed integer: " << reversedNum << std::endl;
    
    return 0;
}