#include <cstdlib>
#include <iostream>
#include <math.h>
#include <complex>

using namespace std;

bool isPrime(unsigned long int n) {
    
    int j = sqrt(n) + 1;
    
    if(n == 2) {
        return true;
    }

    if (n % 2 == 0 || n == 1) {
        return false;
    }

    for (int i = 3; i < j; i += 2) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {

    int cases;
    cin >> cases;

    for (int i = 0; i < cases; i++) {

        unsigned long int n;
        cin >> n;
        
        if(isPrime(n)) {
            cout << "Prime" << endl;
        } else {
            cout << "Not Prime" << endl;
        }

    }

    return 0;
}