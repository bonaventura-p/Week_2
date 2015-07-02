# the first one does not work but I can't see why

def binary_search(x,target):
	midpoint=int(median(x))
	if x==[]:
		minx=0
	else:
		minx=min(x)
	if x==[]:
		maxx=0
	else:
		maxx=max(x)	
	if target >maxx or target <minx:
		return "Not in the list"
	if target<midpoint:
		x=x[minx:midpoint-1]
		binary_search(x,target)
	elif target > midpoint:
		x=x[midpoint+1:maxx]
		binary_search(x,target)
	elif target==midpoint:
		 position=midpoint
		 print position
# this instead does work
def binary_search1(x,target):
	if x==[]:
		minx=0
	else:
		minx=min(x)
	if x==[]:
		maxx=0
	else:
		maxx=max(x)	
	while True:
    	if maxx < minx:
        	return -1
        midpoint = (minx + maxx) // 2
        if x[midpoint] < target:
            minx = midpoint + 1
        elif x[midpoint] > target:
            maxx = midpoint - 1
        else:
            return midpoint