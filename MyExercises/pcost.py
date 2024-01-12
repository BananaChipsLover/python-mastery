import os

# current_dir = os.getcwd()
current_dir = os.path.dirname(__file__)
# Get the relative path of the file
file_path = os.path.join(current_dir, "..", "Data", "portfolio.dat")


with open(file_path, "r") as f:
  lines = f.readlines()

sum_cost=0.0

for line in lines:
    info = line.replace('\n','').split()
    sum_cost = sum_cost + float(info[1]) * float(info[2])

print(str(sum_cost))