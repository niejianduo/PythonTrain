class closing(object):
    def __init__(self, obj):
        print('init')
        self.ob = obj
        print(type(obj))
        print(type(self.ob))
    def __enter__(self):
        print('enter')
        return self.ob
    def __exit__(self, *args):
        print('close')
        return self.ob.close()
with closing(open('new.txt',"a")) as f:
    print(type(f))
    f.write('the contents\n')