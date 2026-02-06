#include <iostream>
#include <vector>

using namespace std;

int main() {
    int dp[1000001];
    int path[1000001];
    int n;
    cin >> n;

    dp[1] = 0;
    path[1] = 0;

    for(int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + 1;
        path[i] = i - 1;
        if (i % 2 == 0 && dp[i] > dp[i / 2] + 1) {
            dp[i] = dp[i / 2] + 1;
            path[i] = i / 2;
        }
        if (i % 3 == 0 && dp[i] > dp[i / 3] + 1) {
            dp[i] = dp[i / 3] + 1;
            path[i] = i / 3;
        }
    }
    cout << dp[n] << endl;
    vector<int> result;
    while (n != 1) {
        result.push_back(n);
        n = path[n];
    }
    result.push_back(1);
    for(int i = 0; i < result.size(); i++)
        cout << result[i] << " ";
    cout << endl;
}