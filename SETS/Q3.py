A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {1, 2}

print("Symmetric difference:", A ^ B)

print("C is subset of A:", C.issubset(A))
print("A is superset of C:", A.issuperset(C))
print("A and B disjoint:", A.isdisjoint(B))