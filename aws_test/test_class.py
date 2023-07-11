class hoge:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def test_vars(self):
        print(vars(self))

hoge_instance = hoge("aaa", "bbb")
print(hoge_instance.test_vars())
