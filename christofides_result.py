from christofides_code import tsp
from timeit import default_timer as timer
from graphs import sh07, sp11, uk12, wg22,  wg59, sgb128

start = timer()
result = tsp(sgb128)
end = timer()
print(["Christofides", result[0], result[1]])
print(f'{end - start}s')
