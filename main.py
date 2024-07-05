immutable_var = (1,2,3)
print(immutable_var)
immutable_var = ('mouse',2)
immutable_var.extend(['mouse',2]) # значения элементов кортежа нельзя изменять, потому что кортеж сам по себе неизменяемый и служит для фиксации элемнтов списка.
mutable_list = (['a','b','c'])
mutable_list.append('d')
print(mutable_list)
