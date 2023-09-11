def GroupAnagram(strs,defaultdict):
    res = defaultdict(list)
    for s in strs:
      count = [0]*26
      for c in s:
          count[ord(c)-ord('a')]+=1
          res[tuple(count)].append(s)
    return res.values()


print(GroupAnagram(['eat','rat','bat','ate']))