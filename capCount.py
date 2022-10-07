import sys
def main(text):
    b=0
    for i in text:
        if i.isupper():
            b += 1
    return(b)
    
z = [y for y in range(len(sys.argv[1])) if sys.argv[1][y].isupper()]

print(main(sys.argv[1]))
print(sum(z))