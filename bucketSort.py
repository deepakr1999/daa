import math
class BucketSort:
    array=[]
    n=0
    no_of_buckets=10
    buckets=[]
    min=0
    max=0
    divider=0
    def __init__(self,l):
        self.array=l
        self.n=len(l)
        self.min=self.array[0]
        self.max=self.array[0]
        self.buckets=[[] for i in range(self.no_of_buckets)]
        for i in self.array:
            if i>self.max:
                self.max=i
            if i<self.min:
                self.min=i
        self.divider=math.ceil((self.max+1)/self.no_of_buckets)
    def sort(self):
        #inserting to bucket
        for i,item in enumerate(self.array):
            bi=math.floor(item/self.divider)
            self.buckets[bi].append(item)
        #clearing the array
        del self.array
        for j in self.buckets:
            j.sort()
        self.array=[i for j in self.buckets for i in j]
    def display(self):
        print(self.array)


b=BucketSort([10,5,67,89,43,45,48,21,23,43,46,76])
b.display()
b.sort()
b.display()
