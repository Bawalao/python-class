with open('panera.txt') as f:
    print(f.readline().strip())
    f.seek(0)
    print(f.readline().strip())
