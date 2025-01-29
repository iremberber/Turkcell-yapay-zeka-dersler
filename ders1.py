from collections import Counter

sentence = input("Bir cümle yazınız : ")

listSentences = sentence.split()
print(listSentences)

sentenceCount = Counter(listSentences)
print(sentenceCount)

sorted(sentenceCount)
print(sorted(sentenceCount)) 


