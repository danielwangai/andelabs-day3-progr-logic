class BinarySearch(list):
	def __init__(self, a, b):
		# len(list)
		self.a = a
		self.b = b

	def search(self, value_to_search):#recursive function
		# initialize counter
		counter = 0
		# index of first element in the current search list
		lower_index = 0# initialized ot  0
		# index of last element in the current search list
		higher_index = self.a - 1
		# index of midpoint element
		midpoint = lower_index + (higher_index - lower_index)//2

		if value_to_search == midpoint:
			# update counter and return dictionary of counter(key) and index of element(value)
			counter = counter + 1
			return {counter: midpoint}
		elif value_to_search > midpoint:
			# element is in upper bound of list
			lower_index = midpoint + 1
			midpoint = lower_index + (higher_index - lower_index)//2
			self.search(value_to_search)
		elif value_to_search < midpoint:
			# element is in upper bound of list
			higher_index = midpoint - 1
			midpoint = lower_index + (higher_index - lower_index)//2
			self.search(value_to_search)


# x = BinarySearch(5, 1)
# print(x.search(2))
