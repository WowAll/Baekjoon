#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main(void) {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, k;
        cin >> n >> k;
        vector<int> cost(n + 1), dp(n + 1, 0), indegree(n + 1, 0);
        vector<vector<int>> edges(n + 1);

        for (int i = 1; i <= n; i++) cin >> cost[i];
        for (int i = 0; i < k; i++) {
            int src, dest;
            cin >> src >> dest;
            edges[src].push_back(dest);
            indegree[dest]++;
        }

        int target;
        cin >> target;

        queue<int> q;
        for (int i = 1; i <= n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
                dp[i] = cost[i];
            }
        }

        while (!q.empty()) {
            int cur = q.front(); q.pop();
            for (int next : edges[cur]) {
                dp[next] = max(dp[next], dp[cur] + cost[next]);
                if (--indegree[next] == 0)
                    q.push(next);
            }
        }

        cout << dp[target] << "\n";
    }
}