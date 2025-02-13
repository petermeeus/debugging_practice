def remove_letter(s, letter):
    for i in range(len(s)):
        if s[i] == letter:
            s = s[:i+1] + s[i:]
    return s

print(remove_letter("banana", "a"))  # Expected: "bnn"