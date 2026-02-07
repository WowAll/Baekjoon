#include <iostream>
#include <vector>
#include <cstring>
#include <queue>

using namespace std;

int main(void) {
    string str;
    cin >> str;

    if (str[0] == '0') {
        cout << 0 << endl;
        return 0;
    }

    int n = str.length();
    vector<int> dp(n + 1, 0);

    dp[0] = 1;
    dp[1] = 1;

    for (int i = 2; i <= n; i++) {
        int oneDigit = str[i - 1] - '0';
        if (oneDigit >= 1 && oneDigit <= 9) {
            dp[i] = (dp[i] + dp[i - 1]) % 1000000;
        }

        int twoDigits = (str[i - 2] - '0') * 10 + (str[i - 1] - '0');
        if (twoDigits >= 10 && twoDigits <= 26) {
            dp[i] = (dp[i] + dp[i - 2]) % 1000000;
        }
    }

    cout << dp[n] << endl;

    return 0;
}