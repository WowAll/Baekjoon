#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int short_max = 0;
    int long_max = 0;
    for (auto iter = sizes.begin(); iter != sizes.end(); iter++)
    {
        int num1 = iter->at(0);
        int num2 = iter->at(1);
        if (num1 > num2)
        {
            if (num1 > long_max)
                long_max = num1;
            if (num2 > short_max)
                short_max = num2;
        }
        else
        {
            if (num2 > long_max)
                long_max = num2;
            if (num1 > short_max)
                short_max = num1;
        }
    }
    return long_max * short_max;
}