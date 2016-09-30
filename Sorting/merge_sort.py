
##############################################################
# Title; Sorting
# Algorithm: Merge Sort
# Solution approach: Divide & Conquer
#
# Description:
##############################################################

def merge_sort(list):
	#print len(list)
	_merge_sort(list,0,len(list)-1)


def _merge_sort(list,p,q):
	if(p<q):
		_merge_sort(list,p,(p+q)/2)
		_merge_sort(list,(p+q)/2+1,q)
		merge(list,p,q)

def merge(list,p,q):
	temp = []
	i = p
	j = (p+q)/2+1
	while((i<=(p+q)/2) and j <= q ):
		if(list[i]<=list[j]):
			temp.append(list[i])
			i=i+1
		else:
			temp.append(list[j])
			j=j+1

	if(i > (p+q)/2):
		while(j<=q):
			temp.append(list[j])
			j=j+1
	else:
		while(i<=(p+q)/2):
			temp.append(list[i])
			i=i+1
	for k in range(p,q+1):
		list[k]=temp[k-p]
	

s = [8,46,23,90,-20,25,120,240,-4,8]
merge_sort(s)
print s
