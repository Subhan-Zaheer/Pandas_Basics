import pandas as pd

if __name__ == '__main__':
    a = pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])
    print(a)
    a = a.fillna(0)  # This how you can solve the nan problem.
    print(a)