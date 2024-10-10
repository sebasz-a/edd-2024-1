#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();

    string s;
    getline(cin, s);
    s.erase(remove(s.begin(), s.end(), ','), s.end());
    s.erase(remove(s.begin(), s.end(), ' '), s.end());

    string out;
    for (int i = 0; i < n/2; i++) {
        out += s[i];
        out += s[n-i-1];
    }
    if (n % 2 != 0) {
        out += s[n/2];
    }
    cout << out;

    return 0;
}
