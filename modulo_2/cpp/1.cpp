#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	
	int nums[n];
	for (int i = 0; i < n; i++) {
		cin >> nums[i];
	}

	int aux = nums[n-1];
	for (int i = n-2; i >= 0; i--) {
		aux += nums[i];
		cout << aux << '\n';
	}
	
	return 0;
}
