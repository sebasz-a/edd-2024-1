#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();

    string s;
    while (n--) {
        getline(cin, s);
        s.erase(remove(s.begin(), s.end(), ' '), s.end());

        reverse(s.begin(), s.end());
        for (int i = 0; i < s.length()-1; i += 2) {
            swap(s[i], s[i+1]);
        }
        cout << s << '\n';
    }

    return 0;
}
