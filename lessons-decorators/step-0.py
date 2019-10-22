from urllib.request import urlopen

def page(url):
    def get():
        return urlopen(url).read()
    return get

python = page('https://python.org')
print(python, type(python))
#print(python())

def f(*args, **kwargs):
    print(args, kwargs)

f(1, 2, 3, a=4, b=5)
args=(10, 20, 30)
d = {
    'aa': 40,
    'bb': 50
}

f(*args, **d)
