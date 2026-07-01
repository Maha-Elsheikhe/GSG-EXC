# Exercise 1
def get_first_and_last(array: list) -> tuple:
    return (array[0], array[-1])


names = ["Maha", "Lama", "Sama"]
res = get_first_and_last(names)
print(res)


# Exercise 2
def get_passed_grades(array: list) -> list:
    passed = []
    for grade in array:
        if grade >= 60:
            passed.append(grade)

    return passed


grades = [50, 60, 65, 90, 44, 43]
print(get_passed_grades(grades))


# Exercise 3
def get_reversed_sentence() -> str:
    text = input("Enter your sentence: ")
    words = text.split()
    words.reverse()
    reversed_sentence = " ".join(words)
    return reversed_sentence


print(get_reversed_sentence)


# Exercise 4
def get_passed_grades(array: list) -> list:
    array.sort()
    array.reverse()
    top_score = array[:3]
    return top_score


print("Top three scores: ", get_passed_grades(grades))

# Exercise 5
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

total = 0   

for item in nested_list:
    for subitem in item:
        total += subitem

print("Total: ", total)
