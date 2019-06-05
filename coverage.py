import sys

def do_something(a,b,c):
    if a>1 and b==0:
        c=c/a
    if a==2 and c>1:
        c=c+1
    else:
        c=c-1

if __name__=="__main__":
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    c=int(sys.argv[3])
    do_something(a,b,c)
    do_something(a+1,b,c)