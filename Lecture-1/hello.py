def abcd(f):
    def w():
        print("before")
        f()
        print("after")
    return w

@abcd
def hello():
    print("hello function")

hello()