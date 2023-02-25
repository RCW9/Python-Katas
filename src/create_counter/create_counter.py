def create_counter(num):
	count = num
	def incrementUp():
		nonlocal count
		count += 1
		return count
		

	def incrementDown():
		nonlocal count
		count -= 1
		return count
		

	dictionary = {'up': incrementUp, 'down': incrementDown}
	return dictionary




    
	
	
