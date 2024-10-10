#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;

	int so_l[n];
	for (int i = 0; i < n-1; i++) {
		cin >> so_l[i];
		cin.ignore();
	}
	cin >> so_l[n-1];

	int lar_l[n];
	for (int i = 0; i < n-1; i++) {
		cin >> lar_l[i];
		cin.ignore();
	}
	cin >> lar_l[n-1];

	int is_l[n];
	for (int i = 0; i < n; i++) {
		cin >> is_l[i];
		cin.ignore();
	}

	int so, lar, is;
	so = lar = is = 0;
	for (int i = 0; i < n; i++) {
		if ((so_l[i] + lar_l[i] + is_l[i]) % 2 == 0) {
			if (so_l[i] % 2 == 0) {
				so += 1;
			}
			if (lar_l[i] % 2 == 0) {
				lar += 1;
			}
			if (is_l[i] % 2 == 0) {
				is += 1;
			}
		} else {
			if (so_l[i] % 2 != 0) {
				so += 1;
			}
			if (lar_l[i] % 2 != 0) {
				lar += 1;
			}
			if (is_l[i] % 2 != 0) {
				is += 1;
			}
		}
	}

	cout << "SO:" << so << ", LAR:" << lar << ", IS:" << is;

	return 0;
}
