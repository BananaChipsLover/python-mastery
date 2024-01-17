import os


def portfolio_cost(file_path):
    sum_cost=0.0

    with open(file_path, "r") as f:
      # lines = f.readlines()


      for line in f:
        try:
          info = line.replace('\n','').split()
          sum_cost = sum_cost + float(info[1]) * float(info[2])
        except ValueError as e:
          print("Couldn't parse:", repr(line))

    print(str(sum_cost))



# current_dir = os.getcwd()
current_dir = os.path.dirname(__file__)
# Get the relative path of the file
file_path = os.path.join(current_dir, "..", "Data", "portfolio2.dat")
portfolio_cost(file_path)
