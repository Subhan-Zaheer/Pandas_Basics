"""
Following are some functions to read data from csv file and to do some processing.

1. read_csv() : This function is actually used to read data from CSV files into a Pandas Data frame object.
2. .info() : This function will give us basic info about rows, columns and data types.
3. .describe() : This will give us statistical info about numerical columns.
4. .columns() : Get list of column names.
5. .shape() : Get the number of columns and rows as tuple.


READING FROM PANDAS DATA FRAME :

dict = {
    col1 : [list of data]
    col2 : [list of data]
    col3 : [list of data]
       .....
    col n: [list of data]
}
In above example I have shown how the data is stored in pandas data frame when we get it from CSV files or
any other.
More over when we have to retrieve data form these data frames it will be easy for compiler to get it.
We can retrieve data from pandas data frame same as from dictionary.
.at() function is also used to retrieve data
.at[row/index number, 'column name']
We can also access columns using '.' operator.
We can also access multiple columns at a same time.
data_frame[[list of columns which we want to retrieve.]]
.copy() function is used to create a copy of data frame.
Other wis if we assign a data frame to other variable or a part of complete data frame,
each variable will be pointing to same data frame. It will not create a copy of data frame.
To access specific row we have .loc[] function.
To access a first row that doesn't contain NAN value we have to use .first_valid_index() function.
.sample(10) is used to get random rows of our data frame.
The number given in this function will be number of rows you want to get.

QUERYING AND SORTING DATA FROM DATA FRAME :

column.sum() : Will add the enteries of this column.
covid_df[covid_df['new_cases'] > 1000] : Querying a subset of data according to our need.
covid_df['new_col_name'] : We can also add new column into our data frame by this method.
.drop('col_name'] : We can also drop a column using this method.
.sort() : This function is used to sort values in data frame.
We can also replace value in data frame.
"""