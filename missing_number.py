# takes two list arguments
def find_missing(list_of_no_1, list_of_no_2):

	if list_of_no_1 == list_of_no_2:
		# if the two arguments are similar - elements are the same return 0
		return 0
	else:
		# use data type set to get the difference between the two lists and save it to a list
		difference_lst_1_and_2 = list(set(list_of_no_2) - set(list_of_no_1))
		# difference_lst_1_and_2 is list, use indices to get the element
		return difference_lst_1_and_2[0]