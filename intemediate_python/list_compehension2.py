#task1

prices = [10,20,30,40]
def halved(num):
     return num/2
halve = [halved(price) for price in prices]
print(halve)

#task2

authors = ['Jafar Jabbarli','Samad Vurgun','Zalimkhan Yaqub']
def splitting(string):
    parts = string.split(' ')
    return parts[0]+'.'+parts[1]
splitter = [splitting(author) for author in authors]
print(splitter)

#task3

scores = [23,45,67,84,82]
def bonus(num1):
    scores_bonus = num1+10
    return scores_bonus>91
true_or_false = [bonus(score) for score in scores]
print(true_or_false)


#task4

websites = ['biz.az','news.az','futbol+.ru']
azeri = [website for website in websites if website.count('az')>0]
print(azeri)



