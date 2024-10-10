#include <iostream>

using namespace std;

int main() {
    int c;
    cin >> c;

    while (c--) {
        int n;
        cin >> n;

        int board[n];
        for (int i = 0; i < n; i++) {
            cin >> board[i];
        }

        int count = 0;
        int move = 0;
        while (true) {
            count += 1;
            int aux = move;
            move += board[move];

            if (move < 0 || move >= n) {
                cout << count << '\n';
                break;
            } else if (board[move] == 0){
                cout << count << '\n';
                break;
            }
            board[aux] = 0;
        }
    }

    return 0;
}
