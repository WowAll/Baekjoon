#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main(void) {
    vector<pair<int, int>> v;
    int day;
    cin >> day;
    int dp[1500001];
    dp[day] = 0;

    for (int i = 0; i < day; i++) {
        int t, p;
        cin >> t >> p;
        v.push_back(make_pair(t, p));
    }

    for (int i = day - 1; i >= 0; i--) {
        int t = v[i].first;
        int p = v[i].second;
        if (i + t <= day)
            dp[i] = max(dp[i + 1], dp[i + t] + p);
        else
            dp[i] = dp[i + 1];
    }
    cout << dp[0];
}