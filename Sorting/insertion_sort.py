
#######################################################################
# Title: Sorting
# Algorithm: Insertion sort
#
# Description:
# Insertion sort is an efficient algorithm for sorting a small number
# of elements. Insertion sort works the way many people sort a hand of
# playing cards. We start with an empty left hand and the cards face
# down on the table. We then remove one card at a time from the table
# and insert it into the correct position in the left hand. To find 
# the correct position for a card, we compare it with each of the cards
# already in the hand, from right to left. At all times, the cards held
# in the left hand are sorted, and these cards were originally the top
# cards of the pile on the table.
#
#######################################################################
def insertion_sort(list):
	for i in range(1,len(list)):
		key = list[i]
		j = i-1
		while (j>=0 and list[j]>key):
			list[j+1] = list[j]
			j = j-1
		list[j+1] = key

A = [5,2,4,6,2,1,3,-5,-9,0,56,45]
insertion_sort(A)
print A
