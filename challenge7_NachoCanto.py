print("\t\tSummary Table\n")
#Ponemos valores a las variables.
num_strings = ['15','100','55','42']
num_ints = [15,100,55,42]
num_floats = [1.5,52.987,7.333,0.6]
num_lists = [[1,2,3],[4,5,6],[7,8,9]]
print("La variable num_strings es de tipo: ",type(num_strings))
print("Esta contiene los valores: ", num_strings)
print("El elemento",num_strings[0],"es de tipo: ",type(num_strings[0]),"\n")
print("La variable num_ints es de tipo: ",type(num_ints))
print("Esta contiene los valores: ", num_ints)
print("El elemento",num_ints[0],"es de tipo: ",type(num_ints[0]),"\n")
print("La variable num_ints es de tipo: ",type(num_floats))
print("Esta contiene los valores: ", num_floats)
print("El elemento",num_floats[0],"es de tipo: ",type(num_floats[0]),"\n")
print("La variable num_ints es de tipo: ",type(num_lists))
print("Esta contiene los valores: ", num_lists)
print("El elemento",num_lists[0],"es de tipo: ",type(num_lists[0]),"\n")
print("Ahora ordenamos num_strings y num_ints")
print("La lista num_strings ordenada: ", sorted(num_strings))
print("La lista num_strings ordenada: ", sorted(num_ints))
#Ahora notamos un diferencia.
print("\n¡Las cadenas son ordenadas alfabeticamente y los enteros son ordenados numericamente!")