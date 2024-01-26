#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    int limit = 5 + pow(10, 6);
    vector<int> sieve(limit, 0);

    for (int i = 2; i <= limit; ++i)
    {
        if (sieve[i] == 0)
        {
            for (int j = i; j <= limit; j += i)
            {
                sieve[j] = i;
            }
        }
    }

    long long x;
    cin >> x;
    int counter = 0;
    while (x >= 3)
    {
        for (long long i = x - 2; i > 0; i--)
        {
            if (sieve[i] == i)
            {
                x = 2 * i - x;
                break;
            }
        }
        counter += 1;
    }

    cout << counter << endl;

    return 0;
}