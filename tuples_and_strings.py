
str1 = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"


# Write a function to count how many times any word occurred in a string.
# Each letter case (upper or lower) in a word matters.
# Lines in output can be in any order.
# Your output should be a list of tuples.


#Count all words in a string
def count_all(str1):
	split_str1 = str1.split(" ")
	word_dict = {}
	total = []
	for item in split_str1:
		if item in word_dict:
			word_dict[item] += 1
		else:
			word_dict[item] = 1
	for word, times in word_dict.items():
		total.append(tuple([word, times]))
	return total

count_all(str1)





# Checks the count of word specified
# def count_word(str1, word):
# 	split_str1 = str1.split(" ")
# 	count, total = 0, 0
# 	while count < len(split_str1):
# 		if split_str1[count] == word:
# 			count, total = count + 1, total + 1
# 		else: 
# 			count += 1
# 	return word, total
