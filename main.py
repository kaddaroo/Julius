class Print:
     def __call__(self, *args, **kwargs):
             print(*args, **kwargs)

a = Print()
a.a = 5
a(a.a)
