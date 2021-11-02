# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        S = input()
        string = S[::2] +' '+ S[1::2]
        print(string)

        

