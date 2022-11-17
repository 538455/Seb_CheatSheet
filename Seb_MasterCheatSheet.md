Seb's Master Cheat Sheet
- [Skipped](#skipped)
- [Terminal (GIT)](#terminal-git)
  - [Clone a Git Repo](#clone-a-git-repo)
    - [Go to the required folder (needs to be cloned/created already)](#go-to-the-required-folder-needs-to-be-clonedcreated-already)
    - [Copy the link provided to you by GitHub, then open the terminal on your computer and enter](#copy-the-link-provided-to-you-by-github-then-open-the-terminal-on-your-computer-and-enter)
  - [Push updates to a Git Repo](#push-updates-to-a-git-repo)
    - [Change to the directory of the Git Repo.](#change-to-the-directory-of-the-git-repo)
    - [Add the file to the staging area.](#add-the-file-to-the-staging-area)
    - [Commit the file with a message.](#commit-the-file-with-a-message)
    - [Push the file to GitHub.](#push-the-file-to-github)
  - [Create a new Git Repo](#create-a-new-git-repo)
    - [Create a folder on your local machine which will serve as the project directory:](#create-a-folder-on-your-local-machine-which-will-serve-as-the-project-directory)
    - [Switch into your newly created directory:](#switch-into-your-newly-created-directory)
    - [Initialize a new Git repository:](#initialize-a-new-git-repository)
    - [Create a new file called `README.md`:](#create-a-new-file-called-readmemd)
    - [Add the README.md file to the repository](#add-the-readmemd-file-to-the-repository)
    - [Commit the README.md file to the repository](#commit-the-readmemd-file-to-the-repository)
    - [Create a new Github page on your profile](#create-a-new-github-page-on-your-profile)
    - [Add the URL of the new repo as a remote on your local repo (replace <URL> with the URL of your repo):](#add-the-url-of-the-new-repo-as-a-remote-on-your-local-repo-replace-url-with-the-url-of-your-repo)
    - [Push the local repo to the remote repo:](#push-the-local-repo-to-the-remote-repo)
  - [Manage API keys](#manage-api-keys)
    - [Set API Key (Terminal in Jupyter Lab.)](#set-api-key-terminal-in-jupyter-lab)
    - [Set API Key (Windows)](#set-api-key-windows)
    - [Get API Key (using OS)](#get-api-key-using-os)
- [SQL](#sql)
- [PostgresDB](#postgresdb)
- [Python](#python)
  - [Strings](#strings)
  - [Integers & Floats](#integers--floats)
    - [Common operations](#common-operations)
  - [Date Objects](#date-objects)
    - [Import required librairies](#import-required-librairies)
    - [Set dates](#set-dates)
      - [Set current date](#set-current-date)
      - [strptime](#strptime)
      - [alternate way](#alternate-way)
      - [From a pandas dataframe](#from-a-pandas-dataframe)
    - [Get parts of Date](#get-parts-of-date)
    - [Work with Timestamp](#work-with-timestamp)
  - [List Operations](#list-operations)
  - [Tuple Operations](#tuple-operations)
  - [Dictionaries](#dictionaries)
    - [Build](#build)
    - [Access elements](#access-elements)
    - [Add/Remove elements](#addremove-elements)
    - [Search for a value](#search-for-a-value)
    - [Convert to/from](#convert-tofrom)
  - [Sets](#sets)
  - [Pandas](#pandas)
    - [Panda Series](#panda-series)
    - [Creating a new DF](#creating-a-new-df)
    - [Get more info](#get-more-info)
    - [Reshaping (Merge, pivot)](#reshaping-merge-pivot)
    - [Get / Change a specific value](#get--change-a-specific-value)
    - [Operation on columns/rows](#operation-on-columnsrows)
    - [Sorting](#sorting)
    - [Filtering](#filtering)
    - [Dropping values & Dealing with Nulls](#dropping-values--dealing-with-nulls)
    - [Loops](#loops)
    - [Pandas & SQL](#pandas--sql)
    - [Converting to/from a Dataframe](#converting-tofrom-a-dataframe)
  - [CSV](#csv)
    - [Opening/Reading a CSV](#openingreading-a-csv)
      - [Simple](#simple)
      - [Set headers](#set-headers)
      - [Change the comma separator](#change-the-comma-separator)
      - [Setting the row index](#setting-the-row-index)
      - [Import a few rows](#import-a-few-rows)
      - [Import a few columns](#import-a-few-columns)
      - [Skip rows](#skip-rows)
    - [Exporting to a CSV](#exporting-to-a-csv)
  - [JSON](#json)
    - [Import required librairies](#import-required-librairies-1)
    - [Load JSON Object](#load-json-object)
    - [Normalize a JSON](#normalize-a-json)
  - [XLS](#xls)
  - [TXT](#txt)
  - [XML](#xml)
  - [Images](#images)
  - [Numpy](#numpy)
    - [Import required librairies](#import-required-librairies-2)
    - [Create a numpy array](#create-a-numpy-array)
    - [Convert to and from a numpy array](#convert-to-and-from-a-numpy-array)
    - [Transpose](#transpose)
    - [Matrix addition](#matrix-addition)
    - [Scalar](#scalar)
    - [Matrix Multiplication](#matrix-multiplication)
    - [Identity Matrix](#identity-matrix)
    - [Determinant](#determinant)
    - [Inverse Matrices](#inverse-matrices)
    - [Matrix Decomposition](#matrix-decomposition)
  - [Matplotlib](#matplotlib)
    - [Install and Import](#install-and-import)
    - [Appearances](#appearances)
    - [Line Plot](#line-plot)
    - [Grid of plots](#grid-of-plots)
    - [Histogram](#histogram)
    - [Time Series](#time-series)
    - [Scatter Plot](#scatter-plot)
    - [Bar Graph](#bar-graph)
    - [Pie Chart](#pie-chart)
    - [Box Plot](#box-plot)
    - [Heatmap](#heatmap)
    - [Violin Plot](#violin-plot)
    - [Others](#others)
  - [Seaborn](#seaborn)
    - [Required Librairies](#required-librairies)
    - [Regression Plot](#regression-plot)
    - [Box Plot](#box-plot-1)
  - [Scipy](#scipy)
  - [BeautifulSoup](#beautifulsoup)
    - [Import required librairies](#import-required-librairies-3)
    - [Using Beautiful Soup](#using-beautiful-soup)
  - [Making an API Request](#making-an-api-request)
    - [Function](#function)
    - [Get the Status code](#get-the-status-code)
  - [Data Cleaning](#data-cleaning)
    - [Import Dataset](#import-dataset)
    - [Clean - Formatting Issues](#clean---formatting-issues)
    - [Clean - Outliers](#clean---outliers)
    - [Clean - Missing Values](#clean---missing-values)
    - [Clean - Duplicate Values](#clean---duplicate-values)
    - [Export to CSV](#export-to-csv)
  - [Data Preparation - Variable Transformation](#data-preparation---variable-transformation)
    - [Log Transformation](#log-transformation)
    - [Binning](#binning)
    - [Scaling](#scaling)
    - [Convert categorical feature into multiple dummy variables](#convert-categorical-feature-into-multiple-dummy-variables)
- [VSCode](#vscode)
  - [SQLite](#sqlite)

# Skipped
- Exploratory_Data_Analysis.py
- Functions.py
- Hypothesis Testing.py
- Loops_Conditions.py
- PostgesDB.py
- Python_Advanced
- Plotly
- Seaborn
- SQLite
# Terminal (GIT)
## Clone a Git Repo
### Go to the required folder (needs to be cloned/created already)
``` cmd
cd ~/git_lhl/data_science_bootcamp/lighthouse-python-exercises
```
### Copy the link provided to you by GitHub, then open the terminal on your computer and enter 
```cmd
git clone git@github.com:YOUR_USER_NAME/lighthouse-python-fundamentals.git
```
If you just want to clone to access files, this is as far as you need to go. 

## Push updates to a Git Repo
### Change to the directory of the Git Repo.
```cmd
cd lighthouse-python-fundamentals
```

### Add the file to the staging area.
```cmd
git add main.py
```
OR
```cmd
git add --all
```

### Commit the file with a message.
```cmd
git commit -m "Added main.py"
``` 

### Push the file to GitHub.
```
git push
```

## Create a new Git Repo
### Create a folder on your local machine which will serve as the project directory:
```cmd
cd ~/git_lhl/data_science_bootcamp/
mkdir lighthouse-data-notes
```

### Switch into your newly created directory:
```cmd
cd lighthouse-data-notes
```

### Initialize a new Git repository:
```cmd
git init
```

### Create a new file called `README.md`:
```cmd
touch README.md
```

### Add the README.md file to the repository
```cmd
git add README.md
```

### Commit the README.md file to the repository
```cmd
git commit -m "Initial commit"
```

### Create a new Github page on your profile

### Add the URL of the new repo as a remote on your local repo (replace <URL> with the URL of your repo):
```cmd
git remote add origin <URL>
```

### Push the local repo to the remote repo:
```cmd
git push -u origin main
```

## Manage API keys
### Set API Key (Terminal in Jupyter Lab.)
- XXX = Name of your API
- YYY = API Key

```cmd
export XXX_API_KEY=YYY
```
Note: When the command export is used in Terminal the variable will be created only in local Terminal session.

### Set API Key (Windows)

### Get API Key (using OS)
```python
import os   #used to access the values of environment variables
api_key = os.environ["XXX_API_KEY"]
```
# SQL
# PostgresDB

# Python
## Strings
```python
string.upper() #convert the string to uppercase
string.lower() #convert the string to lowercase
string.count("a") #count the number of times the letter a appears in the string
string.replace("a", "b") #replace all instances of a with b
string.strip() #remove all leading and trailing whitespace
string.lstrip() #remove all leading whitespace
string.rstrip() #remove all trailing whitespace
string.strip(::-1) #reverse the string
string[3] #get the character at index 3

#convert string to list
string_list = list(string)

#convert string to a set to remove duplicates
string_set = set(string)

#convert set back to a string
string = "".join(string_set)

#Only return the first 4 characters of the string value of column X
df["X"] = df["X"].astype(str).str[0:4]


def string_reverse(string):
    #convert the string into a list
    string_list = list(string)

    #reverse the list
    string_list.reverse()

    #Convert the list back into a string
    string = "".join(string_list)

    #Return the string
    return string


def count_unique_chars(string_1, string_2): 
    # Get the unique characters from string_1 and string 2 by converting them to sets
    unique_chars_1 = set(string_1)
    unique_chars_2 = set(string_2)

    #Combine the two sets
    unique_chars = unique_chars_1.union(unique_chars_2)

    #Return the length of the set
    return len(unique_chars)
```
## Integers & Floats
### Common operations
```python
#Addition & Subtraction
a = 4
b = 2
c = a + b

#Multiplication & Division
a = 4
b = 2
c = a * b

#Exponentiation
a = 4
b = 2
c = a ** b
 
#Modulus
a = 4
b = 2
c = a % b

#Floor Division
a = 4
b = 2
c = a // b

#Assignment Operators
a = 4
b = 2
c = a + b

#Comparison Operators
a = 4
b = 2
c = a == b

#Logical Operators
a = 4
b = 2
c = a > b and a < b

#Identity Operators
a = 4
b = 2
c = a is b

#Membership Operators
a = 4
b = 2
c = a in b

#Bitwise Operators
a = 4
b = 2
c = a & b
```
## Date Objects
### Import required librairies
```python
from datetime import datetime
```
### Set dates
#### Set current date
```python
datetime_object = datetime.now()
```
#### strptime
```python
#Set a date using strptime
x = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
#Set a date using strptime without time
x = datetime.strptime('Jun 1 2005', '%b %d %Y')
```
#### alternate way
```python
x = datetime(2020, 5, 17)
```
#### From a pandas dataframe
```python

#Converting a string to a datetime object
x = pd.to_datetime('2020-05-17 10:00:00')

#Converting a string to a datetime object with a specific format
x = pd.to_datetime('17-05-2020 10:00:00', format = '%d-%m-%Y %H:%M:%S')

## Converting the string value contained in the first row of column A to a datetime object
x = pd.to_datetime(df['A'][0])

```

### Get parts of Date
```python
print(x.year)
print(x.month)
print(x.day)
print(x.weekday) #returns 0 for Monday, 1 for Tuesday, etc.
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)

#Getting Week number of the year from date
print(x.strftime("%W"))

import calendar
print(calendar.month_name[x.month]) #to get NAME of the month
print(calendar.day_name[x.weekday()]) #to get NAME of day from date
```
### Work with Timestamp
```python
#Converting date object into timestamp
print(x.timestamp())

#Converting UNIX timestamp string to date object
Timestamp = 'Insert timestamp'
x = datetime.fromtimestamp(Timestamp)

#Handling timedelta objects
x = datetime.now()
y = datetime.timedelta(days = 7)
print(x + y)

#Getting the difference between two dates and times
x = datetime.now()
y = datetime(2020, 5, 17)
z = x - y

#Formatting dates: strftime() and strptime()
x = datetime.now()
print(x.strftime("%B"))
##The difference between strftime() and strptime() is that strftime() converts a date object to a string, and strptime() converts a string to a date object.

#Handling timezones
import pytz
x = datetime.now()
y = pytz.timezone('Asia/Kolkata')
z = x.astimezone(y)

```
## List Operations
```python
#List
thislist = ["apple", "banana", "cherry"]

#Access elements in a list
thislist = ["apple", "banana", "cherry"]
print(thislist[0])  #Prints the first element in the list(0 is the first element)
print(thislist[1])  #Prints the second element in the list(1 is the second element)

#Change the value of a specific item in a list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

#Loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#Check if an item exists in a list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#Print the number of items in a list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#Add an item to the end of a list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")

#Add an item at the specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") #Inserts "orange" at index 1 but pushes everything else down by 1

#Remove an item from the end of a list
thislist = ["apple", "banana", "cherry"]
thislist.pop() #Removes the last item in the list

#Remove an item at a specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #Removes the item at index 1

#Remove an item by value
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #Removes the item with the value "banana"

#Remove all items from a list
thislist = ["apple", "banana", "cherry"]
thislist.clear() #Removes all items from the list

#Copy a list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #Copies the list to a new list

#Join two lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2 #Joins list1 and list2 into list3

#Sort a list
thislist = [100, 50, 65, 82, 23]
thislist.sort() #Sorts the list in ascending order
thislist.sort(reverse = True) #Sorts the list in descending order

#Reverse a list
thislist = ["a", "b", "c", "d"]
thislist.reverse() #Reverses the order of the list

#slice a list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #Returns the items from index 2 to index 5 (not included)
print(thislist[:4]) #Returns the items from the beginning to index 4 (not included)
print(thislist[2:]) #Returns the items from index 2 to the end
print(thislist[-4:-1]) #Returns the items from index -4 (included) to index -1 (excluded)

#Verify if an item exists in a list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#Use of concatination in a list
thislist = ["apple", "banana", "cherry"]
mylist = ["Ford", "BMW", "Volvo"]
newlist = thislist + mylist

#Use of the append() method to add an item to a list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")

#Use of prepend() method to add an item to a list
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")

#Use of the insert() method to add an item at a specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")

#Nested lists
mylist = ["apple", "banana", "cherry"]
mylist2 = ["Ford", "BMW", "Volvo"]
mylist3 = [mylist, mylist2]

#Access elements in a sublist
mylist = ["apple", "banana", "cherry"]
mylist2 = ["Ford", "BMW", "Volvo"]
mylist3 = [mylist, mylist2]
print(mylist3[0][1]) #Prints the second item in the first list

#Modify multiple list items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] #Changes the second and third items in the list
```
## Tuple Operations
```python
#Access elements in a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #Prints the second element in the tuple

#Change the value of a specific item in a tuple
x = ("apple", "banana", "cherry")
y = list(x) #Converts the tuple into a list so that it can be changed
y[1] = "kiwi"
x = tuple(y) #Converts the list back into a tuple

#Loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

#Check if an item exists in a tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

#Print the number of items in a tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Add an item to a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple) #Converts the tuple into a list so that it can be changed
y.append("orange")
thistuple = tuple(y) #Converts the list back into a tuple

#Remove an item from a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple) #Converts the tuple into a list so that it can be changed
y.remove("banana")
thistuple = tuple(y) #Converts the list back into a tuple

#Join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2 #Joins tuple1 and tuple2 into tuple3

#Copy a tuple
thistuple = ("apple", "banana", "cherry")
mytuple = thistuple #Copies the tuple to a new tuple
```
## Dictionaries
### Build
```python
#Construct a dictionary with the buil-in dict() function
thisdict = dict(brand="Ford", model="Mustang", year=1964)

#Construct a dictionary with the buil-in dict() function on multiple lines
thisdict = dict(
    brand="Ford",
    model="Mustang",
    year=1964
)

#Construct a dictionary with the buil-in dict() function on multiple lines and square brackets
thisdict = dict([
    ("brand", "Ford"),
    ("model", "Mustang"),
    ("year", 1964)
])

#building a dictionary incrementaly
thisdict = {}
thisdict["brand"] = "Ford"
thisdict["model"] = "Mustang"
thisdict["year"] = 1964
```
### Access elements
```python
#Access elements in a dictionary
for x in thisdict:
    print(x) #Prints all the keys in the dictionary

#Access elements in a dictionary using index
for x in thisdict:
    print(thisdict[x]) #Prints all the values in the dictionary

#Access elements in a dictionary using get()
for x in thisdict:
    print(thisdict.get(x)) #Prints all the values in the dictionary
```
### Add/Remove elements
```python
#Add an item to a dictionary
thisdict["color"] = "red" #Adds an item to the dictionary

#Add an item to a dictionary with the update() method
thisdict.update({"color": "red"}) #Adds an item to the dictionary

#Remove an item from a dictionary
thisdict.pop("model") #Removes the item with the specified key name
thisdict.popitem() #Removes the last inserted item
del thisdict["model"] #Removes the item with the specified key name
thisdict.clear() #Removes all the items from the dictionary

#Clear a dictionary
thisdict.clear() #Removes all the items from the dictionary
```

### Search for a value
```python
#Return the value of a key if it exists
x = thisdict.get("model") #Returns the value of the specified key

#Return the value of a key if it exists, otherwise return a default value
x = thisdict.get("model", "No model found") #Returns the value of the specified key

#Return a list of values in a dictionary
x = thisdict.values() #Returns a list of all the values in the dictionary

#Removes a key from a dictionary, if it is present, and returns its value
x = thisdict.pop("model", "No model found") #Returns the value of the specified key
```

### Convert to/from
```python
# Convert a dictionary into a df
df = pd.DataFrame.from_dict(thisdict, orient='index')

# Convert a df into a dictionary
thisdict = df.to_dict()

```
## Sets
```python
#Defining a set
set1 = {1,2,3,4,5,6,7,8,9,10}
##When a set is defined this way, each <obj> becomes a distinct element of the set, even if it is an iterable. This behavior is similar to that of the .append() list method.

#Defining a set with the built-in set() function
set2 = set([1,2,3,4,5,6,7,8,9,10])
##This set() function converts a list into a set

#The difference between the two is that set1 is a set of sets, while set2 is a set of integers 
#Observe the difference between the two sets
print(set1)
print(set2)

#The set() function can also be used to convert a string into a set
set3 = set("Hello World")
#This set contains the letters of the string "Hello World" in the following format: {' ', 'H', 'W', 'd', 'e', 'l', 'o', 'r'}
print('Hello, World!')

#The set() function can also be used to convert a tuple into a set
set4 = set((1,2,3,4,5,6,7,8,9,10))
#This set contains the integers of the tuple (1,2,3,4,5,6,7,8,9,10) in the following format: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#The set() function can also be used to convert a dictionary into a set
set5 = set({1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j"})
#This set contains the keys of the dictionary {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j"} in the following format: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#The set() function can also be used to convert a range into a set
set6 = set(range(1,11))
#This set contains the integers of the range 1-10 in the following format: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}




#Access elements in a set
for x in thisset:
    print(x)

#Check if an item exists in a set
print("banana" in thisset) #Prints True if "banana" is in the set

#Print the number of items in a set
print(len(thisset))

#Add an item to a set
thisset.add("orange") #Adds "orange" to the set

#Add multiple items to a set
thisset.update(["orange", "mango", "grapes"]) #Adds multiple items to the set

#Remove an item from a set
thisset.remove("banana") #Removes "banana" from the set

#Remove an item from a set if it is present
thisset.discard("banana") #Removes "banana" from the set

#Remove the last item from a set
x = thisset.pop() #Removes the last item from the set

#Remove all items from a set
thisset.clear() #Removes all items from the set

#Copy a set
myset = thisset.copy() #Copies the set to a new set

#Join two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #Joins set1 and set2 into set3

#Remove items in set1 that are not present in set2
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.difference_update(set2) #Removes items in set1 that are not present in set2

#Remove items that are present in both sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.symmetric_difference_update(set2) #Removes items that are present in both sets

#Keep only the items that are present in both sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.intersection_update(set2) #Keeps only the items that are present in both sets
```
## Pandas
### Panda Series
```python
#Understanding what a series is
##A series is a one-dimensional array-like object containing a sequence of values (of similar types to NumPy types) and an associated array of data labels, called its index.
##The simplest Series is formed from only an array of data.
##The more complex Series is formed from a dictionary.

#The basic method to create a Series is to call:
pd.Series(data, index=index)

#Creating a series from a dictionary
b = pd.Series({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})

#Creating a series from a list
c = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])

#Creating a series from a numpy array
d = pd.Series(np.random.randn(5), index=['a','b','c','d','e'])
##randn is a function that returns a sample (or samples) from the "standard normal" distribution. It takes a single integer as an argument and returns a numpy array of that length.


#Creating a series from a scalar
e = pd.Series(5, index=['a','b','c','d','e'])

#Accessing data from a series
##Series acts in many ways like a one-dimensional ndarray, and in many ways like a standard Python dict.
##You can get the array representation and index object of the Series via its values and index attributes, respectively.
##If the data is stored in an ndarray, the index will be a RangeIndex object (which is an ndarray implementation of the pandas Index object).
##If the data is stored in some other manner, the index may be an instance of some other Index type, like Int64Index or CategoricalIndex.
##The Series is ndarray-like in that you can get and set values by position:
a[0]
a[1:3]
a[1:3] = 100
a

#You can also get and set values by label:
b['a']
b['a':'c']
b['a':'c'] = 100
b

#You can also use the get method, which takes an index value and returns the corresponding value if it exists in the object:
b.get('a')

#When looping through a Series, it is regarded as array-like, and the value and index are both retrieved:
for i in b:
    print(i)
##This is the same as:
for i in b.index:
    print(b[i])

#Series can also have a name attribute:
b.name = 'My Series'
```
### Creating a new DF
```python
#Creating an empty DataFrame
df= pd.DataFrame()

#Creating a DataFrame from a dictionary
df = pd.DataFrame({ 'name' : ["a", "b", "c", "d", "e","f", "g"],
                   'age' : [20,27, 35, 55, 18, 21, 35],
                   'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]}
                    )

#Create a DataFrame by passing a dict of objects
df2 = pd.DataFrame({'A':1., 
                    'B':pd.Timestamp('20130102'), 
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'), 
                    'D':np.array([3]*4,dtype='int32'), 
                    'E':pd.Categorical(["test","train","test","train"]), 
                    'F':'foo'})
##The columns of the resulting DataFrame have different dtypes.

#Creating a DataFrame from a list
df = pd.DataFrame([['a', 20, 'VP'], ['b', 27, 'CEO'], ['c', 35, 'CFO'], ['d', 55, 'VP'], ['e', 18, 'VP'], ['f', 21, 'CEO'], ['g', 35, 'MD']],
                    columns=['name', 'age', 'designation'])

#Create a dataframe by passing a numpy array with a datetime index and labeled columns
dates = pd.date_range('20130101', periods=6)
datetimeindex = pd.DatetimeIndex(['2011-07-06', '2011-08-06', '2011-09-06', '2011-10-06', '2011-11-06', '2011-12-06'], dtype='datetime64[ns]', freq='D') #Creates a DatetimeIndex with a specified frequency (D = daily)(M = monthly)(Y = yearly)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))



```
### Get more info
```python
df.head() #Returns the first 5 rows of the DataFrame. Can also take an integer argument for the number of rows you want to see.
df.tail() #Returns the last 5 rows of the DataFrame. Can also take an integer argument for the number of rows you want to see.
df.index #Returns the index (row labels) of the DataFrame
df.describe() #Generates descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values

```
### Reshaping (Merge, pivot)
```python
pd.merge(df1, df2, on='column') #Merges two DataFrames together

pd.concat([df1, df2, df3]) #Concatenates DataFrames together

pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']) #Creates a pivot table that groups by A and B and calculates the sum of C

df.T #Returns the transpose of the DataFrame

#----------------------------------------------Merge, join, and concatenate
#Pandas provides various facilities for easily combining Series and DataFrame objects with various kinds of set logic for the indexes and relational algebra functionality in the case of join / merge-type operations.
#Concatenating Pandas objects together with concat() (equivalent to UNION in SQL):
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]] #Splits the dataframe into 3 pieces
pd.concat(pieces) #Concatenates the pieces into one dataframe

#Joining
#To join two dataframes, you can use the merge() function. The merge() function is similar to the join() function in SQL. The merge() function takes two dataframes as arguments and a column name that is common to both dataframes. The merge() function will join the two dataframes on the column that is common to both dataframes.
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pd.merge(left, right, on='key') #Joins the two dataframes on the column 'key'
##Inner join is done by default. You can also do left, right, and outer joins:
pd.merge(left, right, on='key', how='left') #Left join
pd.merge(left, right, on='key', how='right') #Right join
pd.merge(left, right, on='key', how='outer') #Outer join

#Grouping
#By group by, we are referring to a process involving the following steps:

#Splitting the data into groups based on some criteria
#Applying a function to each group independently
#Combining the results into a data structure
#Let's create the DataFrame we will work on.
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                    'B': ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                    'C': np.random.randn(8),
                    'D': np.random.randn(8)})

#To group the dataframe by the column 'A' and sum the values in the column 'C' and 'D', we would do the following:
df.groupby('A').sum() #Returns a dataframe with the column 'A' as the index and the columns 'C' and 'D' as the values. The values in the columns 'C' and 'D' are the sum of the values in the columns 'C' and 'D' for each unique value in the column 'A'. Column 'B' is not included because it is not a numeric column.
#We can also group by multiple columns:
df.groupby(['A','B']).sum() #Returns a dataframe with the columns 'A' and 'B' as the index and the columns 'C' and 'D' as the values. The values in the columns 'C' and 'D' are the sum of the values in the columns 'C' and 'D' for each unique combination of values in the columns 'A' and 'B'. Column 'B' is not included because it is not a numeric column.
#You cannot apply two aggregations on the same column. For example, you cannot do the following:
-X df.groupby(['A','B']).sum().mean() #This will return an error. You can only apply one aggregation on a column. You can apply multiple aggregations on different columns. For example, you can do the following:
#However, you can apply multiple aggregations on different columns. For example, you can do the following:
df.groupby(['A','B']).agg({'C': ['sum', 'mean'], 'D': ['sum', 'mean']}) #Returns a dataframe with the columns 'A' and 'B' as the index and the columns 'C' and 'D' as the values. The values in the columns 'C' and 'D' are the sum and mean of the values in the columns 'C' and 'D' for each unique combination of values in the columns 'A' and 'B'. Column 'B' is not included because it is not a numeric column.



#------------------------------------------Reshaping
#Stack
#The stack() method “compresses” a level in the DataFrame’s columns. First, let’s create a DataFrame to work with:
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                    'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                    'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]

#The stack() method compresses a level in the DataFrame’s columns.
stacked = df2.stack() #Returns a Series with a MultiIndex as the index. The first level of the MultiIndex is the index of the original dataframe. The second level of the MultiIndex is the column of the original dataframe. The values of the Series are the values of the original dataframe.

#Unstack
#The unstack() method pivots a level of the (possibly hierarchical) index labels. If the index is not a MultiIndex, the output will be a Series (the analogue of stack when the columns are not a MultiIndex). If the level involved is not sorted, the output will be sorted. The level involved will automatically get sorted.
unstacked = stacked.unstack() #Returns a dataframe with the index of the original dataframe as the index and the column of the original dataframe as the columns. The values of the dataframe are the values of the original dataframe.
unstacked = stacked.unstack(1) #This will unstack the second level of the MultiIndex. The first level of the MultiIndex will be the index of the dataframe. The second level of the MultiIndex will be the columns of the dataframe. The values of the dataframe are the values of the original dataframe.

#Pivot tables
#Pivot tables are a way of summarizing data in a DataFrame. Let's create a DataFrame to work with:
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                    'B': ['A', 'B', 'C'] * 4,
                    'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                    'D': np.random.randn(12),
                    'E': np.random.randn(12)})

#We can create a pivot table that groups the dataframe by the column 'A' and the column 'C' and calculates the mean of the values in the column 'D' for each unique combination of values in the columns 'A' and 'C'.
pd.pivot_table(df, values='D', index=['A', 'C']) #Returns a dataframe with the columns 'A' and 'C' as the index and the column 'D' as the values. The values in the column 'D' are the mean of the values in the column 'D' for each unique combination of values in the columns 'A' and 'C'.


```
### Get / Change a specific value
```python
#change a value in a specific row and specific column
df.loc['row_name', 'column_name'] = new_value
df.loc[] #Access a group of rows and columns by label(s) or a boolean array.
df.iloc[] #Purely integer-location based indexing for selection by position.

#Getting:
df[A] #Selects column A of the DataFrame df as a Series
df.loc[B] #Selects row labeled B of the DataFrame df as a Series
df.iloc[4] #Selects row 4 of the DataFrame df as a Series
df[2:4] #Selects rows 2 through 4 of the DataFrame df as a DataFrame
fd[bool_vector] #Selects the rows of the DataFrame df where bool_vector is True as a DataFrame.. Not sure I get this one..
    #example
    df[df['A'] > 0] #Selects the rows of the DataFrame df where the value in column A is greater than 0 as a DataFrame
df2[df2['E'].isin(['two','four'])] #Selects the rows of the DataFrame df2 where the value in column E is either 'two' or 'four' as a DataFrame

#setting values
df.iat[0,1]=-1 #Sets the value at row 0, column 1 of the DataFrame df to -1
df.iloc[0,1]=-1 #Sets the value at row 0, column 1 of the DataFrame df to -1
df.at[0, 'float64']=-1 #Sets the value at row 0, column 'float64' of the DataFrame df to -1
df.loc[0, 'float64']=-1 #Sets the value at row 0, column 'float64' of the DataFrame df to -1
df.loc[:, 'float64']= np.array([5] * len(df)) #Sets the values in column 'float64' of the DataFrame df to the values in the array [5, 5, 5, 5, 5, 5]

```
### Operation on columns/rows
```python

#Remove columns from a dataframe
df.drop(['A', 'B'], axis=1) #axis=1 for columns, axis=0 for rows
## this removes the columns from the dataframe, but does not change the original dataframe. To change the original dataframe, use inplace=True:
df.drop(['A', 'B'], axis=1, inplace=True)




```
### Sorting
```python
df.sort_values(by='column_name')  #sort a dataframe by column
df.sort_values(by='column_name', ascending=False) #Sorts a DataFrame by a specified column in ascending or descending order.
df.sort_values(by=['column_name1', 'column_name2'], ascending=[True, False]) #sort a df by multiple columns

#Sort a dataframe by column 'A' in descending order where column 'B' is equal to 'bar'
df[df['B'] == 'bar'].sort_values(by='A')
df[df['B'] == 'bar'].sort_values(by='A', ascending=False)
```
### Filtering
```python
#count the number of rows where column 'A' is equal to 'foo'
df[df['A'] == 'foo'].shape[0]

#count the number of rows where column 'A' is equal to 'foo' and 'B' is equal to 'one'
df[(df['A'] == 'foo') & (df['B'] == 'one')].shape[0]

#count the number of rows where column 'A' is equal to 'foo' and column 'B' is empty
df[(df['A'] == 'foo') & (df['B'].isnull())].shape[0]

#count the number of rows where column 'A' is equal to 'foo' or 'bar'
df[(df['A'] == 'foo') | (df['A'] == 'bar')].shape[0]

#count the number of rows where column 'A' is equal to 'foo' and 'B' is equal to 'one' and 'C' is equal to 'dull'
df[(df['A'] == 'foo') & (df['B'] == 'one') & (df['C'] == 'dull')].shape[0]

#count the number of rows where column 'A' has a value between 5 and 10
df[(df['A'] > 5) & (df['A'] < 10)].shape[0]

#Count rows where column 'A' contains 'bar' and column c us equal to 'foo' grouped by name of the month of column 'B'
df[df['A'].str.contains('bar') & (df['C'] == 'foo')].groupby(df['B'].dt.month_name()).size()
df[df['A'].str.contains('bar')].groupby(df['B'].dt.month_name()).size() #month name
df[df['A'].str.contains('bar')].groupby(df['B'].dt.month).size() #month number

#filter a dataframe by column value
df[df['column_name'] == some_value]
df2 = df[df['column_name'] == some_value] #assign to a new dataframe

# Return a count of unique values in column 'A' over 50 using size
df[df['A'] > 50].groupby('A').size()
df.groupby('A').size()

#Return the number of rows where column A is over 50
df[df['A'] > 50].shape[0]
df[df['A'] > 50]['A'] #return the values of rows where column A is over 50

#Loop thru returned values of column 'A' where column 'B' is equal to 'bar' with no index and one per line
for i in df[df['B'] == 'bar']['A'].values:
    print(i)

#Count rows grouped by column B where column 'B' is between 5 and 10 and sort by count
df[(df['B'] > 5) & (df['B'] < 10)].groupby('B').size().sort_values(ascending=False)
df[(df['B'] > 5) & (df['B'] < 10)].groupby('B').size()

### Which three years in the 1930s saw the most films released?
df[(df['year'] >= 1930) & (df['year'] < 1940)].groupby('year').size().sort_values(ascending=False).head(3)

#date in df is between two dates
df[(df['date']>datetime.date(2016,1,1)) & (df['date']<datetime.date(2016,3,1))] 

#get the minimum value of column 'A'
df['A'].min()
round(df['A'].min(), 2) #rounded to 2 decimal places

#count the number of times each value appears in column 'A' grouped by column 'B' and sort by count
df.groupby('B')['A'].value_counts().sort_values(ascending=False) 
df.groupby('B')['A'].count() #count the number of rows grouped by column 'B'


```
### Dropping values & Dealing with Nulls
```python
df.drop_duplicates() #Returns a DataFrame where the duplicated rows have been removed.

# remove duplicates in column A of a DF
df.drop_duplicates(subset=['A'], keep='first', inplace=True)

#-------------------------------------------------------------------Operating on Null Values-----------------------------------------------------

##As we have seen, Pandas treats None and NaN as essentially interchangeable for indicating missing or null values. To facilitate this convention, there are several useful methods for detecting, removing, and replacing null values in Pandas data structures. They are:
isnull() # Generate a boolean mask indicating missing values
notnull() # Opposite of isnull()
dropna() # Return a filtered version of the data
fillna()  # Return a copy of the data with missing values filled or imputed

##Detecting null values
##Pandas data structures have two useful methods for detecting null data: 
isnull()
notnull()
#Either one will return a Boolean mask over the data. For example:

data = pd.Series([1, np.nan, 'hello', None])
OUT:
data.isnull()
0    False
1     True
2    False
3     True
dtype: bool

data[data.notnull()]
OUT:
0        1
2    hello
dtype: object

#n addition to the masking used before, there are the convenience methods, dropna() (which removes NA values) and fillna() (which fills in NA values). For a Series, the result is straightforward:
data.dropna()
OUT:
0        1
2    hello
dtype: object

#For a DataFrame, there are more options. 
df = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6]])
df
OUT:                            #Nothing is done here. This is just making the table that will be used for the demo
    0   	1	    2
0	1.0	    NaN	    2
1	2.0	    3.0	    5
2	NaN 	4.0	    6

# We cannot drop single values from a DataFrame; we can only drop full rows or full columns. Depending on the application, you might want one or the other, so dropna() gives a number of options for a DataFrame.
df.dropna()
OUT:                            #This drops all rows that have any NaN values
    0   	1	    2
1	2.0	    3.0	    5

#Alternatively, you can drop NA values along a different axis; axis=1 drops all columns containing a null value:
df.dropna(axis='columns')

# But this drops some good data as well; you might rather be interested in dropping rows or columns with all NA values, or a majority of NA values. This can be specified through the how or thresh parameters, which allow fine control of the number of nulls to allow through.
# The default is how='any', such that any row or column (depending on the axis keyword) containing a null value will be dropped. You can also specify how='all', which will only drop rows/columns that are all null values:

df.dropna(axis='columns', how='all')
#In the table above, no columns were dropped because none of them are all NaN values. However:
	0	1	2	3
0	1.0	NaN	2	NaN
1	2.0	3.0	5	NaN
2	NaN	4.0	6	NaN

to 

	0	1	2
0	1.0	NaN	2
1	2.0	3.0	5
2	NaN	4.0	6


# For finer-grained control, the thresh parameter lets you specify a minimum number of non-null values for the row/column to be kept:
df.dropna(axis='rows', thresh=3)    #This drops all rows that have less than 3 non-NaN values
OUT:
	0	1	2	3
1	2.0	3.0	5	NaN


#-----------------------Filling null values
#Sometimes rather than dropping NA values, you'd rather replace them with a valid value. This value might be a single number like zero, or it might be some sort of imputation or interpolation from the good values. You could do this in-place using the isnull() method as a mask, but because it is such a common operation Pandas provides the fillna() method, which returns a copy of the array with the null values replaced.

#Consider the following Series:
data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
data
OUT:
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64

# We can fill NA entries with a single value, such as zero:
data.fillna(0)
OUT:
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64

# We can specify a forward-fill to propagate the previous value forward:
data.fillna(method='ffill')
OUT:
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64

# Or we can specify a back-fill to propagate the next values backward:
data.fillna(method='bfill')
OUT:
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0

#With Dataframe
df.fillna(method='ffill', axis=1)

FROM:
0	1	2	3
0	1.0	NaN	2	NaN
1	2.0	3.0	5	NaN
2	NaN	4.0	6	NaN

TO: 
0	1	2	3
0	1.0	1.0	2.0	2.0
1	2.0	3.0	5.0	5.0
2	NaN	4.0	6.0	6.0

#Notice that if a previous value is not available during a forward fill, the NA value remains.



# drop 5 columns with the biggest ratio of null values
to_drop = missing_data.head(5).index.tolist()
df_train.drop(to_drop, axis=1, inplace=True)
## Warning: Be careful when removing columns. Sometimes a column can give us some relevant information even if 50% of values are Null. It's always good to be cautious when removing columns.


#Example of numeric variables null replacement
    # We will create a separate column to keep the information whether the value was missing. This way, we will have this information available in this column after we replace the value in the original one.
    num_cols_with_missing = df_train.dtypes[missing_cols][df_train.dtypes[missing_cols] == 'float'].index.tolist()
    # create new variable with the information that it was missing
    for cl in num_cols_with_missing:
        df_train[cl + "_missing_ind"] = 0
        df_train.loc[df_train[cl].isnull(), cl + "_missing_ind"] = 1

    #Now we can work on the Null value replacement.
    df_train["LotFrontage"] = df_train["LotFrontage"].fillna(df_train["LotFrontage"].mean())    # We replace the missing values with the mean.
    df_train["GarageYrBlt"] = df_train["GarageYrBlt"].fillna(df_train["GarageYrBlt"].min())     # If the house has a garage and the year is missing, we assume it's the minimum value available.
    df_train["MasVnrArea"] = df_train["MasVnrArea"].fillna(0)                                   # If the veneer area is missing, we assume it's 0

# Example of Object (String) Variables Null replacement
    #Find the variables with the dtype == "object" and having at least one missing value.
    df_train.dtypes[missing_cols][df_train.dtypes[missing_cols] == 'object']
    cat_cols_with_missing = df_train.dtypes[missing_cols][df_train.dtypes[missing_cols] == 'object'].index.tolist()

    # With the help of the data documentation we have, we can figure out that the missing values in Garage and Basement variables mean no garage and no basement respectively. Therefore, we will replace the missing values with "None".
        # GarageFinish : data description says NA means "no garage"
        df_train["GarageFinish"] = df_train["GarageFinish"].fillna("None")

        # GarageCond : data description says NA means "no garage"
        df_train["GarageCond"] = df_train["GarageCond"].fillna("None")

        # GarageQual : data description says NA means "no garage"
        df_train["GarageQual"] = df_train["GarageQual"].fillna("None")

        # GarageType : data description says NA means "no garage"
        df_train["GarageType"] = df_train["GarageType"].fillna("None")

        # BsmtExposure : data description says NA means "no basement"
        df_train["BsmtExposure"] = df_train["BsmtExposure"].fillna("None")

        # BsmtFinType2 : data description says NA means "no basement"
        df_train["BsmtFinType2"] = df_train["BsmtFinType2"].fillna("None")

        # BsmtFinType1 : data description says NA means "no basement"
        df_train["BsmtFinType1"] = df_train["BsmtFinType1"].fillna("None")

        # BsmtCond : data description says NA means "no basement"
        df_train["BsmtCond"] = df_train["BsmtCond"].fillna("None")

        # BsmtQual : data description says NA means "no basement"
        df_train["BsmtQual"] = df_train["BsmtQual"].fillna("None")

    # The information about Electrical and MasVnrType is missing in the documentation. Since we are dealing with categorical variables, we will create a new category for a missing value.
    df_train["Electrical"] = df_train["Electrical"].fillna("Empty")
    df_train["MasVnrType"] = df_train["MasVnrType"].fillna("Empty")

```
### Loops
```python
#iterrows() allows you to iterate through the rows of a DataFrame as Series objects. It returns an iterator yielding each index value along with a Series containing the data in each row:
for row_index, row in df.iterrows():
    print(row_index, row, sep='\n')

#The itertuples() method will return an iterator yielding a namedtuple for each row in the DataFrame. The first element of the tuple will be the row’s corresponding index value, while the remaining values are the row values.
for row in df.itertuples():
    print(row)
```
### Pandas & SQL
```python
#------------------------------------------Pandas with SQL------------------------------------------------#

#Required imports
import sqlite3 as sqlite
import pandas as pd
from sqlalchemy import create_engine #may require installation of sqlalchemy via anaconda

#Create a connection to the database using SQLAlchmey
##We have already learned how to make a connection to the SQLite database with the sqlite3 module. Another option is, to connect to the SQLite (or any other supported databases) database using SQLAlchemy. This type of connection is also recommended by Pandas.
##Let's create a connection with SQLAlchemy.
connection = create_engine('sqlite:///population.db')
##The syntax is as simple as that. The only required parameter in the create_engine function is a connection string. This connection string consists of the name of the database driver and the name of the database we want to connect.

#-------------------------------------------Reading SQL data with Pandas------------------------------------------#

#Pandas allows us to query SQL tables with three methods:

## 1. read_sql_query()
    #This method requires two parameters as input. The first parameter is a string with a SQL query and the second one is a connection to the database. Let's try to read all the rows from our Population table.

    # create SQL query
    sql = 'SELECT * FROM Population'

    with create_engine('sqlite:///population.db').connect() as con:
        df = pd.read_sql_query(sql, con)
    df

## 2. read_sql_table()
    # Another way to load data from the database and into the data-frame is the read_sql_table() method. Compared to the read_sql_query() method, the first argument is the table name instead of the SQL query. The second argument stays the same.

    # table name
    table = 'Population'

    with create_engine('sqlite:///population.db').connect() as con:
        df = pd.read_sql_table(table, con)
    df

## 3. read_sql()
    # This function is a combination of the two mentioned above. Depending on the type of the first argument (SQL query or table name), this function internally calls read_sql_query() instead of read_sql_table().
    # So we can use it both ways:

        # with SQL query:
        sql = 'SELECT * FROM Population'

        with create_engine('sqlite:///population.db').connect() as con:
            df = pd.read_sql(sql, con)
        df

        # with table name:
        table = 'Population'

        with create_engine('sqlite:///population.db').connect() as con:
            df = pd.read_sql(table, con)
        df


```
### Converting to/from a Dataframe
```python

```
## CSV
### Opening/Reading a CSV
#### Simple
```python
#Open CSV file to a pd.DF:
df = pd.read_csv("regression_exercise.csv")

# If this one gives issues, this solution can help:
url = ''
storage_options = {'User-Agent': 'Mozilla/5.0'}
df = pd.read_csv(url, storage_options=storage_options)

#you can follow this by the following arguments to select key columsn and drop the nulls
# load data
titanic = pd.read_csv("titanic.csv")
titanic = titanic[["survived", "pclass", "sex", "age", "embark_town"]]
titanic = titanic.dropna()
```
#### Set headers
```python
df = pd.read_csv('csv_example', header=[0,1,2]) #the first row will be the header, the second row will be the subheader and the third row will be the subsubheader

df = pd.read_csv('csv_example', header=5) #the sixth row will be the header. Data prior to the sixth row will be ignored.

#You can also import the csv without headers and then add the headers later:
df = pd.read_csv('csv_example', index=False, header=False)
```
#### Change the comma separator
```python
df = pd.read_csv('csv_example', sep=';') #the separator is now a semicolon
```
#### Setting the row index
```python
df = pd.read_csv('csv_example', index_col=0, header=0) #the first column will be the index and the first row will be the header
df = pd.read_csv('csv_example', index_col='name', header=0) #the column named 'name' will be the index and the first row will be the header
df = pd.read_csv('csv_example', index_col=0, header='name') #the first column will be the index and the column named 'name' will be the header
```
#### Import a few rows
```python
df = pd.read_csv('csv_example', nrows=3) #only the first three rows will be read
```
#### Import a few columns
```python
df = pd.read_csv('csv_example', usecols=['name', 'age']) #only the columns named 'name' and 'age' will be read
```
#### Skip rows
```python
df = pd.read_csv('csv_example', skiprows=3) #the first three rows will be skipped
df = pd.read_csv('csv_example', skiprows=[0,1,2]) #the first three rows will be skipped
df = pd.read_csv('csv_example', skip_blank_lines=True, sep=":") #the blank lines will be skipped and the separator will be a colon
```
### Exporting to a CSV
```python
#Export to CSV
df.to_csv('csv_example')
```
```python
#Export to CSV without the index
df.to_csv('csv_example', index-False)
```
The second one is usually goot
## JSON
### Import required librairies
```python
import json
```
### Load JSON Object
```python
#json.load -> import json from filepath
#json.loads -> import from text (string)

#Load JSON object as a string into a df (API)
response_json = json.loads(reponse.text)

#print(response_json.keys()) #Returns two keys. The second one has no information of interest so focus on the first one
#print(pd.json_normalize(response_json['results'])) #replace result by your keys
#print(pd.json_normalize(venues_json['results'], record_path=['categories'])) #Parse down the categories. 

add_df = pd.json_normalize('best code from above')


#Load JSON object as a dictionnary
with open('nested.json') as f: #replace nested.json with your file name
    nested_json = json.load(f)
print(nested_json)

# some JSON:
json_content = {"key1": value1,"key2": value2}
json_dump = json.dumps(json_content)

# the result is a JSON string:
print(json_dump)
```
### Normalize a JSON
```python
#Using a Panda function to normalize
pd.json_normalize(nested_json)  #replace nested_json with your variable name (first need to load the file with code above)

#To put a focus on a specific column
pd.json_normalize(nested_json, record_path=['column1', 'column2']) #replace nested_json with your variable name 

# Finding the normalize statement that will be used to put the json in a dataframe
pd.json_normalize(json_file['network'], record_path=['stations'])

# Redoing the query above to only keep key columns
pd.json_normalize(json_file['network'], record_path=['stations'], meta=['id', 'name', 'location.city', 'location.country'])

```
## XLS
```python
#Dealing with xlsx files
import openpyxl #may be required
import pandas as pd

#read excel file
df = pd.read_excel('data.xlsx', sheet_name = "months", engine='openpyxl') #replace data.xlsx with your file name, df with your variable name and months with your sheet name, if required

#read an excel file and return a DataFrame that reads every sheet fo the dataframe and add the sheet name as a column
def read_excel_sheets(file_path):
    xl = pd.ExcelFile(file_path)
    sheets = xl.sheet_names
    df = pd.DataFrame()
    for sheet in sheets:
        dftemp = pd.read_excel(file_path, sheet_name=sheet)
        dftemp['sheet'] = sheet
        df = pd.concat([df, dftemp])
    return df
```
## TXT
```python
#Dealing with txt files
#read txt file
text_files = open('data.txt', 'r') #replace data.txt with your file name and text_files with your variable name
text_files.read()
#when you say read, it reads the whole file. If you want to read a specific line, you can use the following syntax
text_files.readline(2) #replace 2 with the line number you want to read. If left empty, it will read the first line and then the second line when run again and so on.

#You can convert all lines into a list using the following syntax
x= text_files.readlines() #replace text_files with your variable name and x with your variable name
```
## XML
```python
#Import required librairies
import xml.etree.ElementTree as ET
import pandas as pd

#load and parse the XML file
tree = ET.parse('data.xml') #replace data.xml with your file name and tree with your variable name

#Get the object type
type(tree)

#Get the root element
root = tree.getroot()

#Check all tags and attributes of the root element
print(root.tag)
print(root.attrib)



#Print child elements elements of root
for child in root:
    print(child.tag)
    print("---")
    print(child.attrib)
    print("---")


#Print only the name of the child elements and the grandchild elements
for child in root:
    print("Child: " + child.tag, child.attrib)
    for grandchild in child:
        print("Grandchild:" + grandchild.tag, grandchild.attrib)
        print("---")
    print("-------")

##If the child attribute is a dictionary, you can break it down further
for child in root:
    print("Child: " + child.tag)
    for key, value in child.attrib.items():
        print("Grandchild:" + key)
        print(value)
        print("---")
    print("-------")
    
#Print child elements and grandchild elements of root
for child in root:
    print("---")  # Totally optional, just to make the output more readable
    print(child.tag, child.attrib)
    for subchild in child: 
        print(subchild.tag, subchild.attrib)

#Print child elements, grandchild elements and great grandchild elements of root
for child in root:
    print("---")
    print(child.tag, child.attrib)
    for subchild in child: 
        print(subchild.tag, subchild.attrib)
        for subsubchild in subchild:
            print(subsubchild.tag, subsubchild.attrib)
        
#Additional ways to break down an XML file here: https://notebook.community/farfan92/SpringBoard-/data_wrangling_xml/chrisfarfan_xml_exercise

#If the XML file is completely disorganized it is possible to extract specific values this way:
# get infant mortality of each country, add to heap if under capacity 
# otherwise check if new value is greater than smallest.
inf_mort = dict()
for element in root.iterfind('country'):
    for subelement in element.iterfind('infant_mortality'):
        inf_mort[element.find('name').text] = float(subelement.text) 

##You can then take the dictionary and convert it to a dataframe
infmort_df = pd.DataFrame.from_dict(inf_mort, orient ='index')
infmort_df.columns = ['infant_mortality']
infmort_df.index.names = ['country']
infmort_df.sort_values(by = 'infant_mortality', ascending = True).head(10)

###ABOVE MADE AS A FUNCTION###


#With the name of the child element, we can access the child element using the following syntax
##First child of the root
country1 = root[0]

###First child of the first child of the root
rank = country1[0] #or root[0][0]

###Tag of the grandchild
print(rank.tag) #replace rank with your variable name

###Text of the grandchild
print(rank.text) #replace rank with your variable name


#Extract information from all child elements
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

#Using findall() to find all top-level child elements
root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level elements
root.findall("./country/neighbor")

# elements with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")

# 'year' elements that are children of elements with name='Singapore'
root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' elements that are the second child of their parent
root.findall(".//neighbor[2]")
```
## Images
```python
#Need to install pillow
pip install pillow #or conda install pillow
pip install matplotlib #or conda install matplotlib

#and import into the notebook
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#Open Image
myImage = Image.open("./flower_square.jpg") #replace flower_square.jpg with your image name and myImage with your variable name
plt.figure(figsize=(9, 6)) #configure the size of the image. optional
plt.imshow(myImage) #display the image

#convert image to array
imgmat = np.array(myImage) #replace myImage with your variable name and imgmat with your variable name
plt.figure(figsize=(9,6)) #configure the size of the image. optional
plt.imshow(imgmat)  #display the image

#convert array to image
img2 = Image.fromarray(img_array) #replace img_array with your variable name and img2 with your variable name

#In NumPy, we have a 3-D array. The first 2 dimensions are 900x900. This represents the size of the picture. The last dimension is 3, therefore we have one layer for red, one for blue and one for green. Each value represents the intensity of a particular color in that specific position.
#Representation of images in Numpy (using NumPy arrays) allows us to do simple changes to these images using mathematical operations.
```
## Numpy
### Import required librairies
```python
import numpy as np
```
### Create a numpy array
```python
#Creating a numpy array
a = np.array([1,2,3,4,5,6,7,8,9,10])

#create a 3x2 array)
A=np.array([[1,2],[3,4],[5,6]])

# Generate a random matrix 'A' with a shape of 150x50, using the 'np.random.rand' function
A = np.random.rand(150, 50)

# The shape of an array tells us the number of values for each dimension. For a 2-dimensional array, it will give us the number of rows and the number of columns. Let’s find the shape of the previous 2-dimensional matrix A. Since A was created with the array() function, we can access its shape attribute with:
A.shape

```
### Convert to and from a numpy array
```python
# Convert a list into numpy array
an_array = np.array(a_list)
```
### Transpose
```python
# We can access the transpose() method of a numpy.ndarray object by:
A_T = A.T
#or
A_T = A.transpose()
A_T.shape
```
### Matrix addition
```python
#We can add two matrices together if they have the same shape. 

#Let's create matrice B
B = np.array([[2, 5], [7, 4], [4, 3]])

#Now let's add A and B and save the result in C
C = A + B #or C = np.add(A, B)
```

### Scalar
```python
#We can also add a scalar to a matrix. Let's add 5 to A and save the result in D
D = A + 5 
## This adds 5 to each element of A
```

### Matrix Multiplication
```python
## The standard way to multiply matrices is not to multiply each element of one matrix with each element of another one (called the element-wise product), but to calculate the sum of the products between the rows and the columns. A matrix product is also called a dot product.
## The number of columns of the first matrix must be equal to the number of rows of the second one. If the dimensions of the first matrix are (m×n), the second matrix needs to be of shape (n×x). The resulting matrix will have the shape (m×x).
## To compute a matrix product we can use the Numpy function dot().

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[2], [4]])

## Because the matrix A has 2 columns and the matrix B has 2 rows, we can multiply them and store the result in a matrix C:
C = np.dot(A, B)

## It is the equivalent of using the dot() method of a numpy.ndarray object:
C = A.dot(B)

### !!!!!!! Matrix multiplication is not commutative. That is, A*B is not equal to B*A. !!!!!!
### Matrix multiplication is associative. That is, (A*B)*C = A*(B*C). Weird, right?

## Multiplcation can also be done with the * operator:
B = 2*I*A
## This is the same as B = np.dot(2*I, A) above
```

### Identity Matrix
```python
## An identity matrix **In** is a special square (nxn) matrix which has 1s on the main diagonal and 0s everywhere else.
## An identity matrix can be created with the Numpy function eye():
I = np.eye(3)

# When multiplying an identity matrix with another matrix the result is the same matrix:
A = np.array([[1, 2], [3, 4], [5, 6]])
I = np.eye(3)
B = np.dot(I, A)
## Returns the same matrix as A

## The purpose of np.eye is to create a matrix that can be used to multiply another matrix. For example, if we want to multiply a matrix by 2, we can multiply it by the identity matrix multiplied by 2:
A = np.array([[1, 2], [3, 4], [5, 6]])
I = np.eye(3)
B = np.dot(2*I, A)
## Returns the same matrix as A multiplied by 2
```
### Determinant
```python
## To compute a determinant of a matrix using Numpy, we have to use the linalg module. The numpy.linalg module specializes in linear algebra with matrices and vectors.
## Define a new matrix M with the shape (2x2):
M = np.array([[1, 2], [3, 4]])

## Compute the determinant of the matrix M: 
det_M = np.linalg.det(M)
### Returns -2.0

## Determinants can be computed only from square matrices.
## This code below will return an error:
M = np.array([[1,2],[3,4],[5,6]])
det_M = np.linalg.det(M)
det_M
```
### Inverse Matrices
```python
# Inverse Matrices
## The inverse matrix of A with shape (nxn) is denoted as A-1. It is a matrix that when multiplied by A, resultsin an identity matrix. (AA-1 = In). This means that if we apply a linear transformation to the matrix with A, it is possible to go back with A-1. This provides a way to cancel the transformation.
## For this example, we will use the Numpy function linalg.inv() to calculate the inverse of A. Let’s start by creating A with the shape (3x3):
A = np.array([[3, 0, 2], [2, 0, -2], [0, 1, 1]])

## Compute the inverse of A:
A_inv = np.linalg.inv(A)

## We can check if the inverse matrix is correct by multiplying A with A_inv:
I = np.dot(A, A_inv)
```
### Matrix Decomposition
```python
# Generate a random matrix 'A' with a shape of 150x50, using the 'np.random.rand' function
A = np.random.rand(150, 50)

# Decompose the matrix 'A' with SVD using numpy (decompose into matrices U, D, and V)
U, D, V = np.linalg.svd(A)

# Print the shape of the matrices U, D, and V
print(U.shape)
print(D.shape)
print(V.shape)

# Reconstruct matrix 'A' from matrices U (150,150),D (50,),V(50,50) making sure the shapes match
A_reconstructed = np.dot(U[:,:50]*D, V)

# compare matrices A and A_reconstructed with the 'np.allclose' function
np.allclose(A, A_reconstructed)
## Returns True if the matrices are equal, False otherwise

# Reduce the dimension of matrix A to shape 150x20 with SVD
U, D, V = np.linalg.svd(A, full_matrices=False)
A_reduced = np.dot(U[:,:20]*D[:20], V[:20,:20])

#Filter the noise from matrix A with 20 largest singular values (keep the shape of the matrix 150x50)
A_filtered = np.dot(U[:,:20]*D[:20], V[:,:20])


# Decompose to UDV, check the shapes of the matrices, and reconstruct the matrix A
```
## Matplotlib
### Install and Import
```python
#Install Matplotlib
pip install matplotlib

import matplotlib.pyplot as plt

```
### Appearances
```python
# Legends, labels and titles
# Let’s go ahead and create a plot with two lines and add a legend, title, and axis labels:
fig=plt.figure(figsixe=(8,2),dpi=100)
ax=fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label=‘X Squared’)
ax.plot(x,x**3,label=‘X Cubed’, 'r')

ax.legend(loc=0) #loc=0 is the best location for the legend. Can also use loc=1,2,3,4 or be left blank

#PLot appearance
# Matplotlib gives us a lot of options for customizing the appearance of our plots. By now, you should be familiar with changing line color using color=’red’ or ‘red’ like we did in previous examples. Now we want to change linewidth or lw , linestyle or ls, and mark out data points using marker. You can find a whole list of what is possible here and here.
# For the sake of this example, we want our plot to have a linewidth of 3, our linestyle to be double dashes, we want to map out our datapoints using ‘o’ as our marker having a the markersize of 8:
fig=plt.figure(figsize=(8,2),dpi=100)
ax=fig.add_axes([0,0,1,1])
ax.plot(x,x**2,color=’red’,lw=3,ls=’--’,marker=’o’,markersize=8,markerfacecolor=’yellow’,markeredgewidth=3,markeredgecolor=’green’) #markerfacecolor=’yellow’,markeredgewidth=3,markeredgecolor=’green’ are optional arguments

#PLot Range
# Matplotlib allows us to set limits for our plots. We can easily configure the range of our plots using the set_ylim and set_xlim methods of the axis object, or axis(‘tight’) to automatically get “tightly fitted” axes ranges. For example, we can choose to show only plots between 0 to 1 of the x axis, and 0 to 5 of the y axis:
fig=plt.figure(figsize=(8,2),dpi=100)
ax=fig.add_axes([0,0,1,1])

ax.plot(x,x**2,color=’red’,lw=3,ls=’--’,marker=’o’,markersize=8,markerfacecolor=’yellow’,markeredgewidth=3,markeredgecolor=’green’) #markerfacecolor=’yellow’,markeredgewidth=3,markeredgecolor=’green’ are optional arguments

ax.set_xlim([0,1]) #set the x axis range. [0,1] signifies the lower and upper limits of the x axis
ax.set_ylim([0,5]) #set the y axis range. [0,5] signifies the lower and upper limits of the y axis

# Annotations
    # If we want to add annotations to the figure we created in the example above, we can do that by making the following changes in the code.
    # the same code as before
    plt.scatter(setosa['sepal length (cm)'],setosa['sepal width (cm)'],
                marker ='o', color = 'red', label = 'setosa')

    plt.scatter(versicolor['sepal length (cm)'],versicolor['sepal width (cm)'],
                marker ='o', color = 'green', label = 'versicolor')

    plt.scatter(virginica['sepal length (cm)'],virginica['sepal width (cm)'],
                marker ='o', color = 'blue', label = 'virginica')

    # new lines of code
    # it can be tricky to find the right coordinates for the first time
    ######################
    plt.annotate('setosa', xy =(5.0,3.5),
                xytext = (4.25,4.0), arrowprops={'color':'red'})
    plt.annotate('versicolor', xy =(7.2,3.6),
                xytext = (6.5,4.0), arrowprops={'color':'red'})
    plt.annotate('virginica', xy =(5.05,1.95),
                xytext = (5.5,1.75), arrowprops={'color':'red'})
    ######################

    # the same code as before
    plt.legend(loc='upper right')
    plt.title('Iris flower')
    plt.xlabel('sepal length (cm)')
    plt.ylabel('sepal width (cm)')
    plt.ylim(1.5,4.7)
    plt.show()

```
### Line Plot
```python
x = np.linspace(0, 5, 11)
y = x ** 2
plt.plot(x, y)

plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()

# plt.subplot(nrows, ncols, plot_number)
plt.subplot(1,2,1)
plt.plot(x, y, 'r') # 'r' is the color red

plt.subplot(1,2,2)
plt.plot(y, x, 'b') # 'b' is the color blue

#2. Object oriented Interface: This is the best way to create plots. The idea here is to create Figure objects and call methods off it. Let’s create a blank Figure using the .figure() method.
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,'p')    # 'p' is the color purple
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Title')

#2B Remember, we noted that a Figure can contain multiple figures. Let’s try to put in two sets of figures on one canvas:
fig=plt.figure()

ax1=fig.add_axes([0.1,0.1,0.8,0.8])
ax2=fig.add_axes([0.2,0.5,0.4,0.3])

ax1.plot(x,y)
ax2.plot(y,x)

# Line plot
# Line plots are used to visualize a trend in data over intervals of time – a time series – thus the line is often drawn chronologically. Using .plot() method, we can create a line plot:
x = np.linspace(0, 5, 11)
y = np.random.randn(11)
plt.plot(x, y)
plt.show()

#Multiline plot
x = df['month_number']
y1 = df['facecream']
y2 = df['facewash']
y3 = df['toothpaste']
y4 = df['bathingsoap']
y5 = df['shampoo']
y6 = df['moisturizer']

plt.plot(x,y1, label = 'facecream')
plt.plot(x,y2, label = 'facewash')
plt.plot(x,y3, label = 'toothpaste')
plt.plot(x,y4, label = 'bathingsoap')
plt.plot(x,y5, label = 'shampoo')
plt.plot(x,y6, label = 'moisturizer')
plt.legend()
plt.show()
```
### Grid of plots
```python
#2C Create a 3x3 grid of plots:
fig,axes=plt.subplots(nrows=3,ncols=3) 
plt.tight_layout() #This will prevent overlapping of plots
## The only difference between plt.figure() and plt.subplots() is that plt.subplots() automatically does what the .add_axes() method of .figure() will do for you based off the number of rows and columns you specify.
## Now that we know how to create subplots, let’s see how we can plot our x and y arrays on them. We want to plot x, y on the axes at index position (0,1) and y, x on the axes at position (1,2) respectively:

fig,axes=plt.subplots(nrows=3,ncols=3)
    axes[0,1].plot(x,y)
    axes[1,2].plot(y,x)
plt.tight_layout()

#---------
```
### Histogram
```python
# Histograms: help us understand the distribution of a numeric value in a way that you cannot with mean or median alone. Using .hist() method, we can create a simple histogram:
x = np.random.randn(1000)
plt.hist(x)

##Mutliple Histograms
import numpy as np
import matplotlib.pyplot as plt

#makes the data
y1 = np.random.normal(-2, 2, 1000)
y2 = np.random.normal(2, 2, 5000)
colors = ['b','g']

#plots the histogram
fig, ax1 = plt.subplots()
ax1.hist([y1,y2],color=colors)
ax1.set_xlim(-10,10)
ax1.set_ylabel("Count")
plt.tight_layout()
plt.show()
```
### Time Series
```python
# Time series (Line Plot) is a chart that shows a trend over a period of time. It allows you to test various hypotheses under certain conditions, like what happens different days of the week or between different times of the day.
import matplotlib.pylot as plt
import datetime
import numpy as np

x = np.array([datetime.datetime(2017, 1, 1, 0, 0) for i in range(24)])
y = np.random.randint(100, size=x.shape)

plt.plot(x, y)
plt.show()

```
### Scatter Plot
```python
#Scatter plots 
## Scatter plots offer a convenient way to visualize how two numeric values are related in your data. It helps in understanding relationships between multiple variables. Using .scatter() method, we can create a scatter plot:
fig, ax = plt.subplots()
x = np.linspace(0, 5, 11)
y = np.random.randn(11)
ax.scatter(x, y)
```
### Bar Graph
```python
# Bar graphs are convenient for comparing numeric values of several groups. Using .bar() method, we can create a bar graph:
my_df = pdDataframe(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
my_df.plot.bar()
```
### Pie Chart
```python
my_df = pdDataframe(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
my_df.plot.pie(subplots=True)
```
### Box Plot
```python
# Box plots are useful for comparing distributions of numeric values. Using .box() method, we can create a box plot:
my_df = pdDataframe(np.random.randn(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
my_df.plot.box()
```
### Heatmap
```python
# Heatmaps are useful for visualizing the relationship between two variables. Using .heatmap() method, we can create a heatmap:
my_df = pdDataframe(np.random.randn(10, 10))
sns.heatmap(my_df)
```
### Violin Plot
```python
# Violin plots are useful for comparing distributions of numeric values. Using .violin() method, we can create a violin plot:
my_df = pdDataframe(np.random.randn(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
my_df.plot.violin()
```

### Others
```python
# Area plot
# Area plots are useful for visualizing the relationship between two variables. Using .area() method, we can create an area plot:
my_df = pdDataframe(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
my_df.plot.area()

# Scatter matrix
# Scatter matrix is useful for visualizing the relationship between two variables. Using .scatter_matrix() method, we can create a scatter matrix:
my_df = pdDataframe(np.random.randn(1000, 4), columns=['a', 'b', 'c', 'd'])
pd.plotting.scatter_matrix(my_df, alpha=0.2)

# Hexagonal bin plot
# Hexagonal bin plot is useful for visualizing the relationship between two variables. Using .hexbin() method, we can create a hexagonal bin plot:
my_df = pdDataframe(np.random.randn(1000, 2), columns=['a', 'b'])
my_df['b'] = my_df['b'] + np.arange(1000)
my_df.plot.hexbin(x='a', y='b', gridsize=25)

# Kernel density estimation plot
# Kernel density estimation plot is useful for visualizing the relationship between two variables. Using .kde() method, we can create a kernel density estimation plot:
my_df = pdDataframe(np.random.randn(1000, 2), columns=['a', 'b'])
my_df.plot.kde()

# Density plot
# Density plot is useful for visualizing the relationship between two variables. Using .density() method, we can create a density plot:
my_df = pdDataframe(np.random.randn(1000, 2), columns=['a', 'b'])
my_df.plot.density()

# Andrews curves
# Andrews curves is useful for visualizing the relationship between two variables. Using .andrews_curves() method, we can create an Andrews curves:
my_df = pdDataframe(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
pd.plotting.andrews_curves(my_df, 'a')

# Parallel coordinates
# Parallel coordinates is useful for visualizing the relationship between two variables. Using .parallel_coordinates() method, we can create a parallel coordinates:
my_df = pdDataframe(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
pd.plotting.parallel_coordinates(my_df, 'a')

# Lag plot
# Lag plot is useful for visualizing the relationship between two variables. Using .lag_plot() method, we can create a lag plot:
my_df = pdDataframe(np.random.randn(1000, 2), columns=['a', 'b'])
pd.plotting.lag_plot(my_df['a'])

# Autocorrelation plot
# Autocorrelation plot is useful for visualizing the relationship between two variables. Using .autocorrelation_plot() method, we can create an autocorrelation plot:
my_df = pdDataframe(np.random.randn(1000, 2), columns=['a', 'b'])
pd.plotting.autocorrelation_plot(my_df['a'])

# Bootstrap plot
# Bootstrap plot is useful for visualizing the relationship between two variables. Using .bootstrap_plot() method, we can create a bootstrap plot:
my_df = pdDataframe(np.random.randn(1000, 2), columns=['a', 'b'])
pd.plotting.bootstrap_plot(my_df['a'])

# RadViz
# RadViz is useful for visualizing the relationship between two variables. Using .radviz() method, we can create a RadViz:
my_df = pdDataframe(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
pd.plotting.radviz(my_df, 'a')

# Plotting with categorical data
# Plotting with categorical data is useful for visualizing the relationship between two variables. Using .plot() method, we can create a plot with categorical data:
my_df = pdDataframe(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
my_df.plot.bar(stacked=True)

# Plotting with missing data
# Plotting with missing data is useful for visualizing the relationship between two variables. Using .plot() method, we can create a plot with missing data:
my_df = pdDataframe(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
my_df.iloc[5, :] = np.nan
my_df.plot.bar(stacked=True)

# Plotting with duplicate data
# Plotting with duplicate data is useful for visualizing the relationship between two variables. Using .plot() method, we can create a plot with duplicate data:
my_df = pdDataframe(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
my_df.iloc[5, :] = my_df.iloc[2, :]
my_df.plot.bar(stacked=True)

# Plotting with mixed data types
# Plotting with mixed data types is useful for visualizing the relationship between two variables. Using .plot() method, we can create a plot with mixed data types:
my_df = pdDataframe(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
my_df.iloc[5, :] = 'foo'
my_df.plot.bar(stacked=True)

```
## Seaborn
### Required Librairies

### Regression Plot
```python
f, ax = plt.subplots(figsize=(9, 6))
# seaborn's regression plot
sns.regplot(x=(df['Column1']), y=df['Column2'], data=df, order=1)
```
### Box Plot
```python
fig = sns.boxplot(x=(df['Column1']), y=('Column2'), data=df)
fig.axis(ymin=0, ymax=800000)
```

## Scipy
## BeautifulSoup
### Import required librairies
```python
# Required modules
from bs4 import BeautifulSoup
```
### Using Beautiful Soup
```python
# String containing what you want to clean
VARIABLE = ""

# Creating a BeautifulSoup object
soup = BeautifulSoup(VARIABLE, 'lxml')
```
Need further development
## Making an API Request
### Function
I like to contain them in a function. That way, when you loop it makes things easier and you can have all API calls at the same place in your Notebook.
```python
#Import required libraries
import os   #used to access the values of environment variables
import requests #used to make the API request

def API_pull(required_values): 

    #Retrieving API key
    api_key=os.getenv('XXX_API_KEY')
    
    # Format the URL to the API standard
    URL = 'http://api.translink.ca/rttiapi/v1/status' + '?apikey=' + api_key

    ## If you need headers:
    headers = {
        "accept": "application/json",
        "Authorization": api_key 
    }

    # Storing the API return into response
    response = requests.get(url, headers=headers)  # if you use headers
    #response = requests.get(URL)                   # if you don't use headers

    # Depending on the format of the return, it will need to be parsed
    ##TO DO

    ## When you're parsing, you may be working with a df from outside the function. You can call it using:
    #global df_name
    

    # Once parsed, return below. If you leave it as is, you'll just get the raw return from the website
    return response
```
### Get the Status code
Add to the function above:
```python
#Print the status code of the response
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

##Easier way to do this:
if response:
    print('Success!')
else:
    print('An error has occurred.')

# check the response’s status code in an if statement. Instead, you want to raise an exception if the request was unsuccessful. You can do this using .raise_for_status():
import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()   ##If you invoke .raise_for_status(), an HTTPError will be raised for certain status codes. If the status code indicates a successful request, the program will proceed without that exception being raised.
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
```
## Data Cleaning
### Import Dataset
```python
df = pd.read_csv('name.csv')

print(df.shape)
print(df.head)
```
### Clean - Formatting Issues
```python
df['column'].unique()

sns.histplot(df['column'])

#Dropping all redundant/useless columns
df.drop(['UOM', 'UOM_ID', 'SCALAR_FACTOR', 'SCALAR_ID', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS'], axis=1, inplace=True)
```
### Clean - Outliers
```python
#Method 1 - Using Describe
df.describe()

#Method 2 - Single Variable (Boxplots)
import matplotlib.pyplot as plt
import seaborn as sns
sns.boxplot(x=df['Column']);
plt.show()

#Method 3 - Visualizing Multi-variable (Scatterplot)
fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(df['column'], y)
ax.set_xlabel('Per capita crime rate by town')
ax.set_ylabel('Median value of owner-occupied homes in $1000’s')
plt.show()

#Method 4 - Z-Score
from scipy import stats

#Finding Z Score on Column
stats.zscore(df['Column'])

#Turning Absolute
#np.abs(stats.zscore(df['Column']))

#view the outliers
df['Column'][(np.abs(stats.zscore(df['Column'])) > 3)]    #Z-scores above 3 indicate the value is greater than 3 standard deviations from the mean. Data Scientists often label values with a z-score above 3 as outliers.

#Dealing with Outliers
## Can drop the observation (if appropriate)
## Can fix the observation (e.g., obvious typo)
## Explore what caused the outlier
```
### Clean - Missing Values
```python
df.info()


## Sometimes null values aren't exactly NaNs. They are encoded as -1 or 9999, or 0s. 
## The key is to encode them as NaNs. Won't be used in summary calculations (e.g., average, count)
cols_missing_vals = ['Column1', 'Column3', 'Column4'] # cols with inappropriate 0s or whatever else
df[cols_missing_vals] = df[cols_missing_vals].replace(0, np.NaN) # replace 0's with NaNs

# Dropping missing values
df.loc[df['column', 'column2'].isnull()] #to see them
df.dropna(subset=['column', 'column2'], inplace=True) #to drop them


# Replacing Null by the average
df['column'] = df['column'].fillna(value=df['column'].mean())
```
### Clean - Duplicate Values
```python
df[df.duplicated()]

df.drop_duplicates(inplace=True)
```
### Export to CSV
```python
df.to_csv('name.csv')
```
## Data Preparation - Variable Transformation
### Log Transformation
```python
#plot original distribution of Insulin
diabetes_df['Insulin'].plot.hist()

#plot distribution of Insulin after log transformation
np.log(diabetes_df['Insulin']).plot.hist()
```
### Binning
```python
#Binning with q-cut (bin according to quantiles)
pd.qcut(diabetes_df['Age'], q = 4).value_counts()

#Binning with cut (equally sized bins)
pd.cut(diabetes_df['Age'], bins = 4).value_counts()
```
### Scaling
```python
#summary statistics before scaling
diabetes_df.describe()

#use MinMaxScaler to scale data into a given range ((0,1) by default)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled = pd.DataFrame(scaler.fit_transform(diabetes_df))

#summary statistics after scaling
scaled.describe()
```
### Convert categorical feature into multiple dummy variables
```python
#Print Pregnancies column
diabetes_df['Pregnancies']

#convert Pregnancies column into multiple dummy variables
pd.get_dummies(diabetes_df['Pregnancies'])

#convert Pregnancies column into multiple dummy variables in the same dataframe
pd.get_dummies(diabetes_df, prefix='preg', columns=['Pregnancies'])
```
# VSCode
## SQLite















