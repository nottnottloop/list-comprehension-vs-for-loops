import time

TIMES_TO_RUN = 10000
SIZE_OF_LIST = 10000

# List comp
start_time = time.time()

for i in range(TIMES_TO_RUN):
  arr = [i for i in range(SIZE_OF_LIST)]
  print(f"Comp loop iteration {i}")

list_comp_time = time.time() - start_time

# For loops
start_time = time.time()

for i in range(TIMES_TO_RUN):
  arr = []
  for j in range(SIZE_OF_LIST):
    arr.append(j)
  print(f"For loop iteration {i}")

for_loop_time = time.time() - start_time

print(f"\nSeconds to initialise {TIMES_TO_RUN} lists with {SIZE_OF_LIST} objects using list comprehension:")
print(list_comp_time)
print(f"Seconds to initialise {TIMES_TO_RUN} lists with {SIZE_OF_LIST} objects using appending over a for loop:")
print(for_loop_time)