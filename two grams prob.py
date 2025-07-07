def most_frequent_twogram(s):
    freq = {}
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        freq[pair] = freq.get(pair, 0) + 1

                    # Print all two-grams and their counts
    print("🔎 Frequency of all two-grams:")
    for k in sorted(freq):
        print(f"{k}: {freq[k]}")

                     # Find the most frequent two-gram
    most_common = max(freq, key=freq.get)
    return most_common

# Input
n = int(input("Enter string length: "))
s = input("Enter the string: ").strip()

# Output
print("Most frequent two-gram: ", most_frequent_twogram(s)) 
