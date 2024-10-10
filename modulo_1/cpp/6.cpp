#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    cout << n << '\n';
    while (n != 1) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3*n + 1;
        }
        cout << n << '\n';
    }

    return 0;
}
