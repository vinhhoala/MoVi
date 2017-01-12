import datetime
import itertools

print datetime.datetime.now()


#import the data input
infile = open('small.in', 'rb')
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



#function to check if a slice is ok
def slice_check(rb, cb, re, ce): #r: row, c: column, b: beginning, e: ending
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

def slice_score(rb, cb, re, ce): #r: row, c: column, b: beginning, e: ending
	rmax = max(rb, re) #they accept both orders
	rmin = min(rb, re)
	cmax = max(cb, ce)
	cmin = min(cb, ce)
	return (rmax - rmin +1)*(cmax - cmin +1) #score for this slice

#function to check if two slices overlap or not 
def slices_not_overlap(rb1, cb1, re1, ce1, rb2, cb2, re2, ce2): 
	if (min(rb1, re1) >= max(rb2, re2)) | (min(rb2, re2) >= max(rb1, re1)): 
		return True
	if (min(cb1, ce1) >= max(cb2, ce2)) | (min(cb2, ce2) >= max(cb1, ce1)): 
		return True 
	return False
#print slices_not_overlap(0, 0, 3, 3, 2, 2, 4, 5)

slice_list = [] 
for rb in xrange(R):
	for cb in xrange(C):
		for re in xrange(rb, R):
			for ce in xrange(cb, C):
				if not slice_check(rb, cb, re, ce): 
					continue
				else:
					a_slice = [rb, cb, re, ce] 
					slice_list.append(a_slice)
					
print 'Slice list built of %d slices' %(len(slice_list))					
print slice_list[0], slice_list[len(slice_list)-1]


nb_slices_min = int(R*C/H) + 1 		
print nb_slices_min
nb_slices_max = int((R*C)/(2*L))
print nb_slices_max 
max_score = 0
best_solution = []
solution_set = []
#function return a set of all possible subsets of m elements from a set S

def findsubsets(S,m):
    return set(itertools.combinations(S, m))
    
#def solution_check
slice_list_index = range(11)
nb_slice = 10
index = findsubsets(slice_list_index, nb_slice)
print index

#for nb_slice in xrange(nb_slices_min, nb_slices_max+1):
#	for _index in findsubsets(slice_list_index, nb_slice):
#		print _index
#		a_solution = []
#		for i in _index:
#			a_solution.append(slice_list[i])
#		solution_set.append(a_solution)
#	print 'Solution set built of %d elements' %(len(solution_set))
#	for solution in solution_set:
#		score = 0
#		not_overlap = True
#		for i in xrange(len(solution)):
#			for j in xrange(j, len(solution)):
#				if not slices_not_overlap(solution[i][0], solution[i][1], solution[i][2], solution[i][3], solution[j][0], solution[j][1], solution[j][2], solution[j][3]):
#					not_overlap = False
#					break
#			if not not_overlap:
#				score = 0
#				break
#			score += slice_score(solution[i][0], solution[i][1], solution[i][2], solution[i][3])
#		if score > max_score:
#			max_score = score
#			best_solution = solution
#	print "Best solution so far in case nb_slice = %d with max_score = %d" %(nb_slice, max_score)
#	print best_solution

		

		 
		

	
	
