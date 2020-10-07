# --------------------------------------
# Calculate how many vowels are in a   |
# sentence using three techniques.     |
# --------------------------------------


def count_built_in(sentence):
    NumVowels = 0
    sentence.lower()
    NumVowels = sentence.count('a')
    NumVowels += sentence.count('e')
    NumVowels += sentence.count('i')
    NumVowels += sentence.count('o')
    NumVowels += sentence.count('u')
    return NumVowels


def count_iterative(sentence):
    NumVowels = 0
    sentence.lower()
    for i in sentence:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            NumVowels = NumVowels + 1
    return NumVowels


def count_recursive(sentence):
    sentence.lower()
    if not sentence:
        return 0
    return (1 if sentence[0] in 'aeiou' else 0) + count_recursive(sentence[1:])


# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Calculating the number of vowels  using ...")
        print("-------------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print("Recursion =", count_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()


# --------------------------------------

main()
