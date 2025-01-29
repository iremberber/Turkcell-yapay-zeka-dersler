#bir cümle alın ve bu cümlede geçen her bir kelimenin kaç kez tekrarlandığını bulun. 
#Ardından, kelimeleri frekanslarına göre azalan sırada sıralayarak ekrana yazdırın.

#"bu bir test, bu sadece bir test"

from collections import Counter

sentence = input("Bir cümle yazınız : ")

listSentences = sentence.split()
print(listSentences)

sentenceCount = Counter(listSentences)
print(sentenceCount)

sorted(sentenceCount)
print(sorted(sentenceCount)) 


