#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    int c;
    cin >> c;

    while (c--) {
        int m, n;
        cin >> m;
        cin >> n;

        int money[n];
        for (int i = 0; i < n; i++) {
            cin >> money[i];
        }

        int gains[m];
        fill(gains, gains+m, 0);
        for (int i = 0; i < n; i++) {
            gains[i%m] += money[i];
        }

        cout << *max_element(gains, gains+m) - *min_element(gains, gains+m) << '\n';
    }

    return 0;
}
