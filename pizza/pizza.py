import datetime
import itertools
import random
import sys

print datetime.datetime.now()

#import the data input
finput = '%s' %str(sys.argv[1]) 
infile = open(finput, 'rb')
fi_line = infile.readline()
print fi_line
ln = fi_line.split(' ')
R = int(ln[0]) #nb of rows
C = int(ln[1]) #nb of cols
L = int(ln[2]) #minimum number of each ingredient cells in a slice
H = int(ln[3]) #maximum total number of cells of a slice
input_matrix = [[0 for x in range(C)] for y in range(R)]

line_index = 0
for line in infile:
	for i in range(C):
		if line[i] == 'T':		
			input_matrix[line_index][i] = 0;
		elif line[i] == 'M':		
			input_matrix[line_index][i] = 1;
		else:
			print 'Error. File .in corrupted'
	line_index += 1

print 'Transform successfully. R = %d, C = %d, L = %d, H = %d' %(R, C, L, H)
infile.close()

############################
#Output file format:######## 
#nb_slices##################
#rb0 cb0 re0 ce0############
#rb1 cb1 re1 ce1############ 
#rb2 cb2 re2 ce2############
#...............############
############################


#####################################################
#function to check if a slice is ok##################
def slice_check(_slice): #r: row, c: column, b: beginning, e: ending
	if len(_slice) != 4:
		print "Error. Variable input incorrect"
		return None
	rb = _slice[0]
	cb = _slice[1]
	re = _slice[2]
	ce = _slice[3]
	rmax = max(rb, re) #they accept both orders
	rmin = min(rb, re)
	cmax = max(cb, ce)
	cmin = min(cb, ce)
	if (rmax - rmin +1)*(cmax - cmin +1) > H:
		return False
	sumary = 0
	for i in xrange(rmin, rmax+1):
		for j in xrange(cmin, cmax+1):
			sumary += input_matrix[i][j]
	if (sumary < L) | (sumary > ((rmax - rmin +1)*(cmax - cmin +1) - L)):
		return False
	return (rmax - rmin +1)*(cmax - cmin +1) #score for this slice
#print slice_check(0, 0, 0, 7)
##################################################### 	

#####################################################
def slice_score(_slice): #r: row, c: column, b: beginning, e: ending
	if len(_slice) != 4:
		print "Error. Variable input incorrect"
		return None
	rb = _slice[0]
	cb = _slice[1]
	re = _slice[2]
	ce = _slice[3]
	rmax = max(rb, re) #they accept both orders
	rmin = min(rb, re)
	cmax = max(cb, ce)
	cmin = min(cb, ce)
	return (rmax - rmin +1)*(cmax - cmin +1) #score for this slice

#####################################################
#function to check if two slices overlap or not 
def slices_not_overlap(slice_list):
	if len(slice_list) == 0:
		print "Error. No variable input"
		return None
	for _slice in slice_list:
		if len(_slice) != 4:
			print "Error. Variable input incorrect"
			return None
	if len(slice_list) == 1:
		return True
	
	if len(slice_list) == 2:
		rb1 = slice_list[0][0]
		cb1 = slice_list[0][1]
		re1 = slice_list[0][2]
		ce1 = slice_list[0][3]
		rb2 = slice_list[1][0]
		cb2 = slice_list[1][1]
		re2 = slice_list[1][2]
		ce2 = slice_list[1][3]
		if (min(rb1, re1) > max(rb2, re2)) | (min(rb2, re2) > max(rb1, re1)): 
			return True
		if (min(cb1, ce1) > max(cb2, ce2)) | (min(cb2, ce2) > max(cb1, ce1)): 
			return True 
		return False
	for i in xrange(len(slice_list)-1):
		for j in xrange(i+1, len(slice_list)):
			if not slices_not_overlap([slice_list[i], slice_list[j]]):
				return False
	return True
#print "Test slices_not_overlap"
#print slices_not_overlap([[1, 1, 1, 4], [1, 0, 2, 1]])
#print slices_not_overlap([[0, 0, 3, 3], [4, 6, 7, 8]])
#print slices_not_overlap([[0, 0, 3, 3], [0, 4, 4, 5], [4, 6, 7, 8]])
#print slices_not_overlap([[0, 0, 3, 3], [0, 4, 4, 5], [4, 6, 7, 8], [0, 2, 7, 8]])
#print slices_not_overlap([[1, 3, 1, 6], [3, 2, 3, 4], [1, 5, 5, 5], [1, 1, 2, 2], [3, 1, 3, 4], [1, 3, 2, 4], [2, 0, 2, 3], [3, 1, 5, 1], [2, 4, 3, 4], [5, 2, 5, 6], [1, 6, 2, 6], [1, 4, 3, 4], [2, 0, 3, 1], [3, 1, 4, 2], [0, 3, 1, 4], [3, 3, 3, 4], [0, 6, 3, 6], [1, 0, 5, 0], [3, 3, 3, 5], [3, 1, 4, 1], [2, 2, 3, 3], [3, 2, 5, 2], [1, 6, 5, 6], [1, 4, 2, 5], [2, 2, 2, 3], [2, 2, 2, 4], [1, 4, 1, 5], [1, 0, 3, 0], [3, 2, 3, 3], [2, 6, 4, 6], [0, 1, 0, 4], [2, 5, 2, 6], [2, 6, 3, 6], [5, 4, 5, 6], [0, 0, 0, 1], [3, 0, 3, 3], [0, 0, 3, 0], [0, 1, 0, 5], [2, 0, 2, 4], [0, 0, 4, 0], [4, 5, 5, 6], [1, 4, 1, 6], [0, 6, 2, 6], [0, 2, 0, 5], [2, 4, 3, 5], [0, 1, 2, 1], [3, 0, 3, 2], [0, 5, 1, 6], [1, 6, 3, 6], [0, 4, 1, 5], [3, 0, 4, 1], [3, 5, 4, 6], [3, 2, 4, 3], [3, 4, 5, 4], [4, 5, 4, 6], [1, 2, 1, 5], [5, 3, 5, 6], [2, 1, 2, 4], [1, 0, 2, 1], [1, 1, 1, 5], [0, 0, 1, 1], [1, 3, 1, 4], [2, 5, 4, 5], [3, 0, 3, 1], [0, 3, 0, 5], [0, 3, 0, 6], [3, 4, 4, 5], [1, 0, 2, 0], [1, 5, 4, 5], [2, 4, 2, 5], [0, 2, 0, 6], [0, 0, 1, 0], [3, 2, 3, 5], [1, 2, 1, 4], [0, 0, 0, 3], [1, 1, 1, 4], [3, 5, 5, 5], [5, 5, 5, 6], [2, 5, 3, 6], [0, 6, 1, 6], [2, 1, 2, 2], [3, 5, 4, 5], [3, 1, 3, 3], [0, 0, 2, 0], [2, 5, 5, 5], [0, 3, 0, 4], [0, 5, 1, 5], [3, 2, 4, 2], [1, 6, 4, 6], [1, 1, 2, 1], [2, 0, 2, 2], [0, 0, 0, 2], [1, 5, 2, 6], [3, 1, 3, 5], [0, 0, 0, 4], [3, 4, 4, 4], [2, 1, 2, 3], [1, 0, 4, 0], [3, 3, 4, 4], [2, 3, 3, 4], [0, 6, 4, 6], [2, 1, 3, 2], [3, 0, 3, 4], [0, 2, 0, 4], [1, 2, 1, 6], [1, 3, 2, 3], [1, 2, 2, 3], [2, 1, 3, 1], [2, 6, 5, 6], [1, 3, 1, 5]])
#####################################################

slice_list = [] 
for rb in xrange(R):
	for cb in xrange(C):
		for re in xrange(rb, R):
			for ce in xrange(cb, C):
				_slice = [rb, cb, re, ce]
				if not slice_check(_slice): 
					continue
				else:
					if not _slice in slice_list: 
						slice_list.append(_slice)
					
print 'Slice list built of %d slices' %(len(slice_list))					
#print slice_list[0], slice_list[len(slice_list)-1]



nb_slices_min = int(R*C/H) + 1 		
#print nb_slices_min
nb_slices_max = int((R*C)/(2*L))
#print nb_slices_max 
max_score = 0
best_solution = []
solution = []

#########Solution 1: Randomly select###################
#for i in xrange(10000):
while(max_score < R*C):
	solution[:] = []
	new_slice_list = slice_list[:]
	#print "Len new_slice_list: %d. Len slice_list: %d" %(len(new_slice_list), len(slice_list)) 
	score = 0
	slice0 = random.choice(new_slice_list)
	#print slice0
	solution.append(slice0)
	score += slice_score(slice0)
	#print score
	new_slice_list.remove(slice0)
	while(len(new_slice_list)>0):
		#print len(new_slice_list)
		_slice = random.choice(new_slice_list)
		new_slice_list.remove(_slice) 
		solution.append(_slice)
		if not slices_not_overlap(solution):
			solution.remove(_slice)
			#print "Continue"
			continue
		else:
			#print "Add score" 
			score += slice_score(_slice)
			#print slice_score(_slice)
	if score > max_score:
		max_score = score
		best_solution[:] = []
		best_solution = solution[:]
		print "Max score: %d"  %(max_score)
		print len(best_solution)
		print best_solution	
		outfile = open('small.out', 'wb')
		outfile.write("%d\n" %len(best_solution))
		for _slice in best_solution:
			outfile.write("%d %d %d %d\n" %(_slice[0], _slice[1], _slice[2], _slice[3]))
		outfile.close()	
		if max_score == R*C:
			print "Perfect solution found"
			break

print datetime.datetime.now()		


#################################
#function return a set of all possible subsets of m elements from a set S
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

def common_element(some_list):
	if len(some_list) == 0:
		return None
	if len(some_list) == 1:
		return some_list[0]
	if len(some_list) == 2:
		_list = []
		for i in some_list[0]:
			for j in some_list[1]:
				if i == j:
					_list.append(i)
		return _list
	if len(some_list) > 2:
		list1 = common_element(some_list[:len(some_list)/2])
		list2 = common_element(some_list[len(some_list)/2:])
		return common_element([list1, list2])
#test common_element: 
#A = [0,1,2,3,[4,5]]
#B = [0,1,3,4,6,7,8]
#C = [0,1]
#D = []

#print common_element([D])
#print common_element([A])
#print common_element([A,B])
#print common_element([A,B,C])
#print common_element([A,B,C,D])
#################################
	 
		

	
	
