def GroupAnagram(strs):
    sts_table = {}
    for str1 in strs:
        sorted_str = ''.join(sorted(str1))
        if sorted_str not in sts_table:
            sts_table[sorted_str] = []
        sts_table[sorted_str].append(str1)
    return list(sts_table.values())