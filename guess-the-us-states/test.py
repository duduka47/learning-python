import pandas

csv = pandas.read_csv("50_states.csv")
print(csv["state"])