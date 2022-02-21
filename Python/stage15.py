stix = '''

She walks in beauty

She walks in beauty , like the night
Of cloudless climes and starry skies ;
And all that's best of dark and bright
Meet in her aspect and her eyes ;
Thus mellowed to that tender light
Which heaven to gaudy day denies ...

Lord Byron
'''
max=0
max_povtoreniya=[]

avg_len=0

#Exercise 1
print(stix)
#нормализирую строчку
vse = stix.split()
vse_length=len(vse)
for i in range(vse_length):
    vse[i]=vse[i].lower()

#Exercise 2
#перевела лист всех слов в сет чтобы избавиться от дупликатов
unikalnie=set(vse)
print(unikalnie)


#Exercise 3
#перевела сет обратно в лист чтобы можно было работать с индексом
unikalnie_list=list(unikalnie)
length=len(unikalnie_list)
for i in range(length):
    word_count=vse.count(unikalnie_list[i])
    print(i+1, ". ",unikalnie_list[i], "(", vse.count(unikalnie_list[i]), ")")
    avg_len=avg_len+len(unikalnie_list[i])
    #макс=0 по дефолту, если значение больше то оно заменяется и становится новым максом
    if word_count>max:
        max_povtoreniya.clear()
        max=word_count
    if word_count==max:
     max_povtoreniya.append(unikalnie_list[i])

#Exercise 4
print("Maximum povtoreniy: ", max)
print("Slovo kotoroe povtorilos ", max ," raz: ", max_povtoreniya)

#Exercise 5
print("Srednyaa dlina unikalnix slov: ",avg_len/(i+1))

#Exercise 6
print("Kolichestvo unikal'nix slov: ",i+1)
print("Kolichestvo vsex slov: ",len(vse))