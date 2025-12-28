def string_freq(string):
    hash_map = {}

    for i in string:
        hash_map[i] = hash_map.get(i, 0) + 1

    return hash_map

if __name__ == "__main__":
    string = "aeroplllanneee"
    ans = string_freq(string)
    print(ans)

    char = input("Enter character to count = ")
    print(ans.get(char, 0))

