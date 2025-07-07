#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    string s;
    cout << "Enter string length: ";
    cin >> n;
    cout << "Enter the string: ";
    cin >> s;

    unordered_map<string, int> freq;
    string max_pair;
    int max_count = 0;

    for (int i = 0; i < n - 1; ++i) {
        string pair = s.substr(i, 2);
        freq[pair]++;
        if (freq[pair] > max_count) {
            max_count = freq[pair];
            max_pair = pair;
        }
    }

    // Print all two-grams and their frequencies
    cout << "\n🔎 Frequency of all two-grams:\n";
    vector<string> keys;
    for (auto& p : freq)
        keys.push_back(p.first);
    sort(keys.begin(), keys.end());

    for (const auto& k : keys)
        cout << k << ": " << freq[k] << "\n";

    // Most frequent two-gram
    cout << "\n🏆 Most Frequent Two-Gram: " << max_pair << endl;

    return 0;
}

