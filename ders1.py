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

#Anagram çiftleri bulup en uzun olani ekrana yazdirmak

def find_longest_anagram_pair(words):
  words.sort()
  anagram_groups = {}
  for word in words:
    sorted_word = "".join(sorted(word))
    if sorted_word not in anagram_groups:
        anagram_groups[sorted_word] = []
    anagram_groups[sorted_word].append(word)

  longest_anagram_pair = []
  max_length = 0

  for group in anagram_groups.values():
    if len(group) >= 2 and len(group[0]) > max_length:
        max_length = len(group[0])
        longest_anagram_pair = group[:2]

  return longest_anagram_pair

words = input("kelime listesi giriniz.").split()
result = find_longest_anagram_pair(words)
print("En uzun anagram çifti:", result)

#ders1

#Temel veri tipleri
unitPrice = 2500
productName = "Hava temizleyici"
isLoggedIn = False
interestRate = 4.5

#Şartlı Yönlendirme

if isLoggedIn == True:
  print("Kullanıcı bilgileri doğru")
else: 
  print("Kullanıcı bilgileri hatalı")
  
grade = 75
if grade >=90:
  print("AA")
elif grade >= 80:
  print("BA")
elif grade >= 70:
  print("CB")
else:
  print("FF")
  
 #Döngüler
for i in range(10):
  print(i)

#2'den başla 10'a kadar 3erli
for i in range(2,10,3):
  print(i)
  
cities = ["Ankara", "İstanbul", "İzmir"] #Listedir, köşeli parantezle olur.

for city in cities: 
    print(city)
    
#Kural: Asla isimlendirmeleri uyduruk yapma, kısaltma kullanma. Okunaklı kod yazmak çok önemli.

city = "Ankara" #Bu aslında arkaplanda {"A","n","k","a","r","a" şeklinde gözükür


sayi1 = int(input("Sayı1'i giriniz: "))
sayi2 = int(input("Sayı2'yi giriniz: "))

def total(n):
  toplam = 0
  for i in range(1,n):
    if n%i == 0:
      toplam += i
  return toplam

sayi1top = total(sayi1)
sayi2top = total(sayi2)