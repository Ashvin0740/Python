l = 10 #Global
def function1(n):
    # l=5 #local
    m = 12
    global i
    # l = l+1
    print(l,m)
    print(n,"i have printed")
function1(" this is me")