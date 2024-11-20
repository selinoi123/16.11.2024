from random import randint


array_city: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]

#START Question A1
print(sorted(array_city, key=lambda array:len(array)))
#END

#START Question A2
print(sorted(array_city, key=lambda array: array.count(' '), reverse=True))
#END

#START Question A3
print(sorted(array_city, key=lambda array: array[-1]))
#END

#START Question A4
print(sorted(array_city, key=lambda city: city[::-1]))
#END

#START Question A5
print(sorted(array_city, key=lambda array: array.count('a'), reverse=True))
#END

#START Question A6
cities: list[str:int:str] = [
    ["Tokyo", 5760, "Asia"],
    ["New York", 5690, "North America"],
    ["Paris", 2050, "Europe"],
    ["London", 2240, "Europe"],
    ["Sydney", 8780, "Australia"],
    ["Dubai", 1300, "Asia"],
    ["Shanghai", 4920, "Asia"]
]

#START Question a
print(sorted(cities, key=lambda city: city[1]))
#END

#START Question b
print(sorted(cities, key=lambda city: city[1], reverse=True))
#END

#START Question c
print(sorted(cities, key=lambda city: city[2]))
#END

#START Question d
print(sorted(cities, key=lambda city: (city[2], city[1])))
#END

number: list[int] = [randint(1, 100) for _ in range(50)]

#START Question b1
print(sorted(number, key=lambda num: num))
#END

#START Question b2
average = sum(number) / len(number)
print(average)
print(sorted(number, key=lambda num: (num - average) ** 2))
#END

texts: str = """
This chocolate cake is rich, moist, and full of delicious chocolate flavor.
To make the cake, you will need chocolate, flour, sugar, eggs, and butter.
After baking the chocolate cake, let the cake cool before adding the chocolate frosting.
"""

#START Question 2a
words: list[str] = texts.lower().replace(",", " ").split()
print(words)

dict_count_word: dict[str:int] = dict()
for word in words:
    if word in dict_count_word:
        dict_count_word[word] += 1
    else:
        dict_count_word[word] = 1

print(dict_count_word)
most_frequent_word = max(dict_count_word, key=dict_count_word.get)
print(most_frequent_word)
#END

#START Question 2b
dict_count_letters: dict[str:int] = dict()
for let in texts.lower().replace(" ", ""):
    if let in dict_count_letters:
        dict_count_letters[let] += 1
    else:
        dict_count_letters[let] = 1

print(dict_count_letters)
print(list(sorted(dict_count_letters.items(), key = lambda item: item[1], reverse = True)))
print(max(dict_count_letters))
max_letter = max(dict_count_letters, key=lambda key_item: dict_count_letters[key_item])
print("max :", max_letter,dict_count_letters[max_letter])

min_letter = min(dict_count_letters, key=lambda key_item: dict_count_letters[key_item])
print("min :", min_letter ,dict_count_letters[min_letter])
#END


#START Question C
power_three: dict[int: int] = dict()
for i in range(1, 20 + 1):
    power_three[i] = i ** 3
print(power_three)
num: int = int(input("Enter a number: "))
if 1 <= num <= 20:
    print(power_three[num])
else:
    print("no exist")
#END

