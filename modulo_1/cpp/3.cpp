#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int q = 0, r = 0, aux = 0;
    while (n--) {
        cin >> aux;
        if (aux > 0) {
            q += aux;
        } else {
            r += aux;
        }
    }

    cout << "positivos " << q << ", negativos " << r;

    return 0;
}
