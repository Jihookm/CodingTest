while 1:
    try:
        print(input())
    except EOFError: #읽을게 없을 때
        break