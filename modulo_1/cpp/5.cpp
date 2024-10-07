#include <iostream>

using namespace std;

int main() {
    int a;
    long long b, aux;
    cin >> a >> b;
    aux = a;

    while (aux <= b) {
        cout << aux << "\n";
        aux *= a;
    }

    return 0;
}
