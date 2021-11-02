# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input()) 
    phone_book = dict(input().split() for i in range(n))
    queries = 1
    while(1):
        try:            
            query = input()
            if query in phone_book:
                print(query+'='+phone_book[query])
            else:
                print("Not found")
        except EOFError:
            break
