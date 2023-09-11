import sympy as sp
import pulp
from pulp import *
import re


objective = "6*y + -3*z + -1*k"
constraints = "2*y + 3*z <= 5, 6*y + 5*z >= 9"

constraints_list = constraints.split(',')
constraints_list = [constraint.strip() for constraint in constraints_list]

cons = []

for constraint in constraints_list:
    simplified_constraint = sp.simplify(constraint)
    # print(simplified_constraint)
    cons.append(simplified_constraint)


simplified_object = objective

# split each part
terms = re.split(r'\s*[+-]\s*', objective)
obj = []
for term in terms:
    term = term.strip()  
    obj.append(term)
# print(obj)

# split var and coef
coef = []
var = [] 
for i in range(len(obj)):
    if '*' in obj[i]:
        obj1 = obj[i].split('*')
        coef.append(obj1[0])
        var.append(obj1[1])
    else:
        var.append(obj[i])
    
# Ghi vào tệp "Lpfile.txt"
with open("Lpfile.txt", "w") as f:
    
    f.write("Maximize \n\n")
    f.write("Obj: " + str(simplified_object))


    # Ghi các ràng buộc
    f.write("\n")
    f.write("Constraints:\n")
    for i, constraint in enumerate(cons):
        f.write(f"C{i + 1}: {str(constraint)}\n")

    # Ghi các biến:
    f.write("Variable\n")
    for i in range(len(obj)):
        f.write(var[i] + " ")
    
    f.write("\n\nEnd")


# Read the text file
with open("Lpfile.txt", "r") as file:
    lines = file.readlines()

# Create a LP problem

if 'Maximize' in lines[0]: 
    problem = LpProblem("LP_Problem", LpMaximize)
elif 'Minimize' in lines[0]: 
    problem = LpProblem("LP_Problem", LpMinimize)



vari = {}
# Khai bao cac bien
for i in range(len(lines)):
    if 'Variable' in lines[i]:
        a = i
# print(lines[a+1].split())
for term in lines[a+1].split():
    vari[term] = pulp.LpVariable(term, cat = LpBinary)

#Them ham muc tieu
for i in range(len(lines)):
    if 'Obj' in lines[i]:
        b = i
# print(lines[b].split(":"))

line = lines[b].replace(" ", "")
obj_name, obj_expr = line.split(":")
# print(obj_name, obj_expr)
thanh_phan = obj_expr.split('+')
# print(thanh_phan)
muc_tieu = 0
biens = {}
for i in range(len(thanh_phan)):
    he_so, bien = thanh_phan[i].split('*')
    he_so = float(he_so)
    # print(he_so)
    biens[bien] = LpVariable(bien)
    # print(biens[bien])
    muc_tieu += he_so * biens[bien]
# print(muc_tieu)

problem += muc_tieu, "objective"


#Them cac rang buoc
variables = {}
for i in range(len(lines)):
    if 'Constraints:' in lines[i]:
        c = i
for i in range(c+1,a):
    constraint_name, constraint_expr = lines[i].split(":")
    constraint_name = constraint_name.strip()
    constraint_expr = constraint_expr.strip()
    if "<=" in constraint_expr:
        parts = constraint_expr.split("<=")
    elif ">=" in constraint_expr:
        parts = constraint_expr.split(">=")
    lhs = parts[0].strip()
    rhs = parts[1].strip()
    # print(lhs, ",", rhs)    
    if "+" in lhs:
        terms = lhs.split("+")
    elif "-" in constraint_expr:
        terms = lhs.split("-")
    print(terms)
    a = 0
    for term in terms:
        coefficient, variable_name = term.split("*")
        coefficient = float(coefficient.strip())
        # print(coefficient)
        variable_name = variable_name.strip()
        variables[variable_name] = LpVariable(variable_name)
        # print(variables[variable_name])
        a += coefficient * variables[variable_name]
        print(a)
    if "<=" in constraint_expr:
        constraint = a <= float(rhs)
    elif ">=" in constraint_expr:
        constraint = a >= float(rhs)
    problem += constraint


# Solve the LP problem
problem.solve()

# Print the results
print("Status:", LpStatus[problem.status])
for var in variables.values():
    print(f"{var.name}: {var.varValue}")

print("Objective Value:", value(problem.objective))

print("cons Value:", problem.constraints)
