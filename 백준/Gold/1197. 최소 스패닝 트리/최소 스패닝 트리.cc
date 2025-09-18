#include <iostream>
#include <queue>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	vector<pair<int, int>> graph[10001];
	priority_queue<pair<int, int>> pq;
	bool vis[10001] = { false };
	int ans = 0;

	int v, e;
	cin >> v >> e;
	for (int i = 0; i < e; i++)
	{
		int a, b, c;
		cin >> a >> b >> c;
		graph[a].push_back(make_pair(b, c));
		graph[b].push_back(make_pair(a, c));
	}
	pq.push(make_pair(0, 1));
	while (!pq.empty()) {
		int cost = -pq.top().first;
		int cur = pq.top().second;
		pq.pop();
		if (vis[cur])
			continue;
		vis[cur] = true;
		ans += cost;
		for (auto iter = graph[cur].begin(); iter < graph[cur].end(); iter++)
		{
			int next = iter->first;
			int ncost = iter->second;
			pq.push(make_pair(-ncost, next));
		}
	}
	cout << ans;
}