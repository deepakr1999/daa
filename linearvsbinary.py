import timeit

max_elem=[100,1000,2000,5000,7000,15000,30000,50000]

def linear(max):
	arr=[]
	key=max
	for i in range(0,max-1):
		arr.append(i)
	for i in range(0,max-1):
		if key==arr[i]:
			return



def binary(arr,l,h,k):
	if(l<=h):
		mid=(l+h)/2
		if k>arr[ord(mid)]:
			return binary(arr,mid+1,h,k)
		if k==arr[ord(mid)]:
			return
		return binary(arr,l,mid-1,k)

for i in range(0,len(max_elem)):
	start=timeit.default_timer()
	linear(max_elem[i])
	end=timeit.default_timer()
	print("The time taken for ",max_elem[i]," elements is {:.20f}".format(end-start))


for i in range(0,len(max_elem)-1):
	start=timeit.default_timer()
	arr=[]
	for j in range(0,max_elem[i]):
		arr.append(j)
	binary(arr,0,100,10)
	end=timeit.default_timet()
