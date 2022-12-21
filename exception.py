'''a=10
try:
    a=a/0

except:ZeroDivisionError
print("its not an error")'''

def div(a):
    if a < 4:
        b= a/(a-a)

    print("the value of b",b)


try:
    div(1)

except ZeroDivisionError:
    print("not defined")

except UnboundLocalError:
    print("value is greater than 4")

