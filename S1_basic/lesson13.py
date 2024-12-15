# 实现一个可迭代对象，可以用小数做步长
class myrange():
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.end:
            self.start += self.step
            return self.start
        else:
            raise StopIteration
        
for i in myrange(1, 10, 0.5):
    print(i)