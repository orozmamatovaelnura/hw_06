def advanced_search(integer_lst, searched_value): #код для сравнения
	if not isinstance(searched_value, int):
		raise ValueError('Arguments should be integers')

	for i in integer_lst:
		if not isinstance(i, int):
			raise ValueError('Arguments should be integers')

	integer_set = set(integer_lst)
	new_lst = list(integer_set)
	if not searched_value in new_lst:
		result_index = -1
	else:
		result_index = new_lst.index(searched_value)

	return new_lst, result_index


def decorator(func_dec):    
  def wrapper(integer_lst, searched_value):  #оборачиваем функцию
    return func_dec(integer_lst, searched_value)
  return wrapper

@decorator
def search(integer_lst, searched_value):    #копируем тот же код
	if not isinstance(searched_value, int):
		raise ValueError('Arguments should be integers')

	for i in integer_lst:
		if not isinstance(i, int):
			raise ValueError('Arguments should be integers')

	integer_set = set(integer_lst)
	new_lst = list(integer_set)
	if not searched_value in new_lst:
		result_index = -1
	else:
		result_index = new_lst.index(searched_value)

	return new_lst, result_index

lst = [-3, 7, -3, 13, -4, 1, 10, 3, 19, 6, 12, 13, 3, 6, 19, 22, 25, 21, 11, 3]
print(advanced_search(lst, 3))
print(search(lst, 3))
