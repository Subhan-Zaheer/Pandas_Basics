import pandas as pd

if __name__ == '__main__':

    a = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    # print(a)
    # print(a.values)
    # print(a['a':'c'])
    grades_dict = {'A':4, 'A-':3.5, 'B':3}
    grades = pd.Series(grades_dict)
    # print(grades['A':'B'])
    marks_dict = {'A':85, 'A-':75, 'B':65}
    marks = pd.Series(marks_dict)
    position_dict = {'A':"1st", 'A-':"2nd", 'B':"3rd"}
    position = pd.Series(position_dict)
    data_frame = pd.DataFrame({'Grades':grades, 'Marks':marks, 'Position':position})
    print(data_frame)
    print(data_frame.iloc[1:3:, 1:3])
    # print(data_frame.T)
    # print(data_frame.values[2, 2])
    # print(data_frame.index)
    # print(data_frame.columns)
    # print(data_frame.iterrows())
    # data_frame['percentage'] = (data_frame['Marks']/100)*100
    # print(data_frame)
    # print(data_frame.values[2, :])
    # del data_frame['Position']
    # print(data_frame)
    # print(data_frame[data_frame['Marks'] > 70])