def SortdNames(names,heights):
    sort_h = list(sorted(zip(names,heights)),reverse = True)
    answer = []
    for i in range(len(sort_h)):
        answer.append(sort_h[i][1])
    return answer

print(SortdNames(['Namiq','Ayxan','Johny'], [185,183,179]))
