# 1 დავალება
sentence = input("შეიყვანეთ წინადადება:")
word1 = input("შეიყვანეთ სიტყვა რომელიც უნდა შეიცვალოს:")
word2 = input("შეიყვანეთ სიტყვა რომლითაც უნდა შეიცვალოს:")

new_sentence = sentence.replace(word1, word2)

print("შედეგი:", new_sentence)


# 2 დავალება
sentence = input("შეიყვანეთ წინადადება: ")

words = sentence.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("ყველაზე გრძელი სიტყვა არის:", longest)


# 3 დავალება
word1 = input("შეიყვანე პირველი სიტყვა: ").lower()
word2 = input("შეიყვანე მეორე სიტყვა: ").lower()

if len(word1) != len(word2):
    print("ეს სიტყვა არ არის ანაგრამი.")
else:
    def count_letters(word):
        letter_count = {}
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        return letter_count

    if count_letters(word1) == count_letters(word2):
        print("ეს სიტყვა ანაგრამია.")
    else:
        print("ეს სიტყვა არ არის ანაგრამი.")
