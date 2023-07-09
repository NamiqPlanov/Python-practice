def MatchingRule(items,ruleKey,ruleValue):
    type1 = []
    color = []
    name = []
    n = len(items)
    for i in range(n):
        type1.append(items[i][0])
        color.append(items[i][1])
        name.append(items[i][2])
    if ruleKey =="type":
        return type1.count(ruleValue)
    elif ruleKey =="color":
        return color.count(ruleValue)
    elif ruleKey == "name":
        return name.count(ruleValue)

print(MatchingRule([["car","grey","BMW"],["car","green","BMW"]], "type", "car"))
