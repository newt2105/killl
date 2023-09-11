# # Parse the objective function
# var_line = lines[1].strip().split(":")
# obj_expr = obj[1].strip()

# # Define the objective function
# for term in obj_expr.split('+' or "-"):
#     term = term.strip()
#     var = term
#     variables[var] = pulp.LpVariable(var, lowBound=0)
#     if obj is None:
#         obj = variables[var]
#     else:
#         obj += variables[var]
# problem += obj, "Objective"

# # Parse the constraints
# for line in lines[2:]:
#     line = line.strip()
#     if not line:
#         continue
#     constraint_name, constraint_expr = line.split(":")
#     constraint_name = constraint_name.strip()
#     constraint_expr = constraint_expr.strip()
#     if "<=" in constraint_expr:
#         parts = constraint_expr.split("<=")
#     elif ">=" in constraint_expr:
#         parts = constraint_expr.split(">=")
#     # print(parts)
#     lhs = parts[0].strip()
#     rhs = parts[1].strip()
#     # print(lhs, ",", rhs)
#     if "+" in lhs:
#         terms = lhs.split("+")
#     elif "-" in constraint_expr:
#         terms = lhs.split("+")
#     # print(terms)
#     a = 0
#     for term in terms:
#         term = term.strip()
#         coefficient, variable_name = term.split("*")
#         coefficient = float(coefficient.strip())
#         # print(coefficient)
#         variable_name = variable_name.strip()
#         # variables[variable_name] = LpVariable(variable_name)
#         # print(variables[variable_name])
#         a += coefficient * variables[variable_name]
        
#         # print(a)
#     if "<=" in constraint_expr:
#         constraint = a <= float(rhs)
#     elif ">=" in constraint_expr:
#         constraint = a >= float(rhs)
#     problem += constraint


# # Solve the LP problem
# problem.solve()

# # Print the results
# print("Status:", LpStatus[problem.status])
# for var in variables.values():
#     print(f"{var.name}: {var.varValue}")

# print("Objective Value:", value(problem.objective))

# print("cons Value:", problem.constraints)
