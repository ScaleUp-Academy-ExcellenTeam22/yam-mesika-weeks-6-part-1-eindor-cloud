
#get a sentence
#return a list of the length of each word in the sentence
#using list comprehension
def words_length(sentence):
    return [len(word) for word in sentence.split(' ')]

#return a list of all the letters between a-z and A-Z
#using list comprehension
def get_letters():
    return [chr(letter) for letter in range(ord('a'), ord('z')+1)] + [chr(letter) for letter in range(ord('A'), ord('Z')+1)]


def count_words(text):
    text = "".join(word for word in text if word.isalpha() or word.isspace())
    return {word: len(word) for word in text.split(' ')}


print(words_length("Toto, I've a feeling we're not in Kansas anymore"))
print(get_letters())
print(count_words("""You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat."""))