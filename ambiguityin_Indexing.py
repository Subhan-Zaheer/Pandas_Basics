import pandas as pd

if __name__ == '__main__':
    a = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
    print(a)
    print(a[5])
    print(a.loc[1])
    print(a[1:3])
    print(a.loc[1 : 3])
