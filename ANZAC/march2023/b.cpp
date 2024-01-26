#include <iostream>
#include <string>

using namespace std;

int main() {
    char d;
    string F;
    cin >> d >> F;

    bool inserted = false;
    for (int i = 0; i < F.length(); i++) {
        if (d > F[i]) {
            F.insert(F.begin()+i,d);
            inserted = true;
            break;
        }
    }

    if (!inserted) {
        F.insert(F.end(),d);
    }

    cout << F << endl;

    return 0;
}