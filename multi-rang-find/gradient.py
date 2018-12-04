import random
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import functions
import sympy


x1 = sympy.Symbol('x1')	# symbol <x1>
x2 = sympy.Symbol('x2')	# symbol <x2>

x_sym = list()	# symbols of multidimensional variable
x_sym.append(x1)
x_sym.append(x2)

				# initialization of multidimensional variable
x = dict()		# access to each component is through symbolic key
for var_name in x_sym:
	x[str(var_name)] = random.randint(0, 22) - 13	# random value of x components

f_sym = 4 * (x1-5)**2 + 70 * (x2-2)**2 + 31	# symbolic function

print("\n-------------------------\nSTART Gradient method")

print("X[0]")
for item in x.items():
	print(item)

print("keys of dict")
for key in x.keys():
	print(key)

print("values of dict")
for key in x.values():
	print(key)

nabl_x = dict()
for key in x.keys():
	nabl_x[key] = sympy.diff(f_sym, key, 1)
	print(nabl_x[key])

for key in nabl_x.keys():
	print("nabl_x['", key, "'] := ", nabl_x[key], " = ", nabl_x[key].subs({key:x[key]}), sep='')
########################## PYTHON HISTORY: .python_history #######################
# print(f_sym)
# print(nabl_x)