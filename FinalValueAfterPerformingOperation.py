def FinalValue(operation):
    return sum(op[1]==1 or -1 for op in operation)

