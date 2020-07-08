def most_frequent(a):
    b=dict()
    for i in a:
        if i not in b:
            b[i]=1
        else:
            b[i]=b[i]+1
    print(b)
        

most_frequent("mississippi")
