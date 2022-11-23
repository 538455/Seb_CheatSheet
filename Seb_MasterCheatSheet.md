# Seb's Master Cheat Sheet - Table of content
- [Seb's Master Cheat Sheet - Table of content](#sebs-master-cheat-sheet---table-of-content)
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
    - [Add the URL of the new repo as a remote on your local repo (replace  with the URL of your repo):](#add-the-url-of-the-new-repo-as-a-remote-on-your-local-repo-replace--with-the-url-of-your-repo)
    - [Push the local repo to the remote repo:](#push-the-local-repo-to-the-remote-repo)
  - [Manage API keys](#manage-api-keys)
    - [Set API Key (Terminal in Jupyter Lab.)](#set-api-key-terminal-in-jupyter-lab)
    - [Set API Key (Windows)](#set-api-key-windows)
    - [Get API Key (using OS)](#get-api-key-using-os)
    - [Update SebCheatSheet](#update-sebcheatsheet)
- [SQL](#sql)
- [PostgresDB](#postgresdb)
- [Python](#python)
  - [Strings](#strings)
  - [Integers \& Floats](#integers--floats)
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
    - [Dropping values \& Dealing with Nulls](#dropping-values--dealing-with-nulls)
    - [Loops](#loops)
    - [Pandas \& SQL](#pandas--sql)
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
  - [Plotly](#plotly)
    - [Radar Plot](#radar-plot)
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
- [Data Preparation](#data-preparation)
  - [Orientation](#orientation)
    - [Import Dataset](#import-dataset)
  - [Data Cleaning](#data-cleaning)
    - [Data Cleaning Function](#data-cleaning-function)
    - [Clean - Formatting Issues](#clean---formatting-issues)
    - [Clean - Outliers](#clean---outliers)
    - [Clean - Missing Values](#clean---missing-values)
    - [Clean - Duplicate Values](#clean---duplicate-values)
    - [Export to CSV](#export-to-csv)
- [Feature Engineering (Variable Transformation)](#feature-engineering-variable-transformation)
  - [Log Transformation](#log-transformation)
  - [Binning](#binning)
  - [Scaling](#scaling)
    - [Scale entire DF](#scale-entire-df)
    - [Scale single value](#scale-single-value)
  - [Convert categorical feature into multiple dummy variables](#convert-categorical-feature-into-multiple-dummy-variables)
- [Sampling and dimensionality reduction](#sampling-and-dimensionality-reduction)
  - [Splitting Data into a 'Training' and a 'Testing' set](#splitting-data-into-a-training-and-a-testing-set)
    - [Holdout split](#holdout-split)
    - [K-fold split](#k-fold-split)
    - [Leave-One-Out split](#leave-one-out-split)
  - [Resampling (Class Imbalance)](#resampling-class-imbalance)
    - [1) Can You Collect More Data?](#1-can-you-collect-more-data)
    - [2) Try Changing Your Performance Metric](#2-try-changing-your-performance-metric)
    - [3) Try Resampling Your Dataset](#3-try-resampling-your-dataset)
    - [4) Try Generate Synthetic Samples](#4-try-generate-synthetic-samples)
    - [5) Try Different Algorithms](#5-try-different-algorithms)
    - [6) Try Penalized Models](#6-try-penalized-models)
    - [7) Try a Different Perspective](#7-try-a-different-perspective)
    - [8) Try Getting Creative](#8-try-getting-creative)
  - [Principal Component Analysis](#principal-component-analysis)
    - [PCA Function](#pca-function)
    - [Basic PCA use:](#basic-pca-use)
    - [Using PCA for 2D Scatter Plot](#using-pca-for-2d-scatter-plot)
    - [Using PCA for 3D Scatter Plot](#using-pca-for-3d-scatter-plot)
  - [Variable Selection](#variable-selection)
- [Modeling Techniques - Unsupervised Learning](#modeling-techniques---unsupervised-learning)
  - [Clustering](#clustering)
    - [Cluster Functions](#cluster-functions)
    - [Set Librairies and values](#set-librairies-and-values)
    - [Plot Custer Function](#plot-custer-function)
    - [K-Means Clustering (Distance-based, good for blobs)](#k-means-clustering-distance-based-good-for-blobs)
      - [Elbow Method (Determine # of clusters for K-Means)](#elbow-method-determine--of-clusters-for-k-means)
      - [K-Means Clustering](#k-means-clustering)
    - [Hierarchical Clustering](#hierarchical-clustering)
      - [Dendogram (Determine # Clusters for Hierarchical Clustering)](#dendogram-determine--clusters-for-hierarchical-clustering)
      - [Hierachical Clustering](#hierachical-clustering)
    - [Density Based Clustering (DBSCAN)](#density-based-clustering-dbscan)
  - [Generative Networks](#generative-networks)
  - [Dimension Reduction](#dimension-reduction)
- [Modeling Techniques - Supervised Learning](#modeling-techniques---supervised-learning)
  - [Classification](#classification)
    - [Random Forest Classifier](#random-forest-classifier)
  - [Regression](#regression)
    - [(Simple and Multiple) Linear Regression Model using Statsmodels](#simple-and-multiple-linear-regression-model-using-statsmodels)
    - [(Simple and Multiple) Linear Regression using sklearn](#simple-and-multiple-linear-regression-using-sklearn)
    - [Interpreting the Regression Results](#interpreting-the-regression-results)
    - [Polynomial Regression](#polynomial-regression)
      - [Multiple features (Set to 1 for single feature)](#multiple-features-set-to-1-for-single-feature)
      - [Single Feature](#single-feature)
- [Model Optimization](#model-optimization)
  - [Gradient Descent](#gradient-descent)
  - [Stochastic Gradient Descent](#stochastic-gradient-descent)
- [Model Evaluation](#model-evaluation)
  - [Regression Metrics](#regression-metrics)
    - [Mean Squared Error (MSE)](#mean-squared-error-mse)
    - [Root-Mean-Squared-Error (RMSE)](#root-mean-squared-error-rmse)
    - [Mean-Absolute-Error (MAE)](#mean-absolute-error-mae)
    - [R² or Coefficient of Determination](#r-or-coefficient-of-determination)
    - [Adjusted R²](#adjusted-r)
  - [Classification Metrics](#classification-metrics)
    - [Accuracy](#accuracy)
    - [Precision/Recall](#precisionrecall)
    - [F1-score](#f1-score)
    - [ROC curve/AUC score](#roc-curveauc-score)
      - [ROC curve](#roc-curve)
      - [AUC Score](#auc-score)
    - [Lift Curves](#lift-curves)
    - [Log-Loss](#log-loss)
- [Machine Learning - Reinforcement Learning](#machine-learning---reinforcement-learning)
- [Machine Learning - Semi-Supervised Learning](#machine-learning---semi-supervised-learning)
- [VSCode](#vscode)
  - [SQLite](#sqlite)
- [Useful Functions](#useful-functions)
  - [OLS Regression Results Function](#ols-regression-results-function)

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

### Update SebCheatSheet
```cmd
cd C:\Users\987\GIT_LHL\DataScienceBootcamp\Seb_Code\Seb_CheatSheet

git add Seb_MasterCheatSheet.md
git commit -m "Cheat Sheet Update"
git push
```
# SQL
# PostgresDB

# Python
```python
#Determine what type of object A is
type(A)
```
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

#Convert a 3 dimension tuple into a numpy array
import numpy as np
thistuple = ((1,2,3),(4,5,6),(7,8,9))
myarray = np.asarray(thistuple)

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

# Replace all values X from Column A with value Y
df.loc[df['A'] == X, 'A'] = Y

#Replace all values from Column A with value X where Column B == Y
df.loc[df['B'] == Y, 'A'] = X


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

# Return the unique combinations of Column A and Column B, including null combination
df.groupby(['A', 'B']).size()
df.groupby(['A', 'B'])
df.groupby(['A', 'B']).size().reset_index().sort_values(by='A') # sort by column A

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

#Convert tuple into numpy array of the appropriate shape
an_array = np.array(a_tuple)

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
## Plotly
### Radar Plot
```python
# Age and Income Clusters
import pandas as pd
import plotly.graph_objects as go


#Set categories to the columns of the dataframe
categories=list(scaled_X)

fig = go.Figure()

# Add clusters as traces
fig.add_trace(go.Scatterpolar(
        r=AI_cl0.tolist(),
        theta=categories,
        fill='toself',
        name='Cluster 0'
))
fig.add_trace(go.Scatterpolar(
        r=AI_cl1.tolist(),
        theta=categories,
        fill='toself',
        name='Cluster 1'
))
fig.add_trace(go.Scatterpolar(
        r=AI_cl2.tolist(),
        theta=categories,
        fill='toself',
        name='Cluster 2'
))
fig.add_trace(go.Scatterpolar(
        r=AI_cl3.tolist(),
        theta=categories,
        fill='toself',
        name='Cluster 3'
))
fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 10]
    )),
  showlegend=True
)
# Make the plot larger
fig.update_layout(
    autosize=False,
    width=900,
    height=900,
)

fig.show()
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
# Data Preparation
## Orientation
### Import Dataset
```python
df = pd.read_csv('name.csv')

print(df.shape)
print(df.head)
```
## Data Cleaning
### Data Cleaning Function
```python
def dataCleaning(df, code=True, tips=False, orientation=True, formatIssues=True, missingValues=True, duplicateValues=True, outliers=True):
    """
    ------------------
    Consolidation of the usual data cleaning steps for a df, November 2022
    Made by Sebastien Garneau, sebastien.garneau@gmail.com
    ------------------
    df: your dataframe

    code: A text template to note your observations as you go. Use the code snippets included in the output. copy-paste into vscode/notepad

    tips: Provides snippets of code to help you clean potential issues in your df. If you prefer this to code
    
    orientation: Provides information about the shape/objects of your data
    
    formatIssues: Provides detailed information on each column to help identify format issues
    
    missingValues: Provides information on missing values
    
    duplicateValues: Provides information on duplicate values
    
    outliers: Provides information on outliers
    """
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    if code==True:
        print("### CLEANING CODE:")
        print("df = dfX #Change to your df's name")
        print()
        print("#### Change column value:")
        print()
        print()
        print("#### Drop entire column:")
        print()
        print()
        print("#### Change column type:")
        print()
        print()
        print("#### Change column name:")
        print()
        print()
        print("#### Handle missing values:")
        print()
        print()
        print("#### Handle duplicate values:")
        print("# df.drop_duplicates(inplace=True) # drop ALL duplicate rows")
        print()
        print("#### Drop outliers:")
        print()
        print()
        print("#### Other observations / further investigations:")
        print("#")
        print("#")
        print("#")
        print()
        print("df.head() #Final Review")
        print("# dfX = df #Change to your df's name")
        print()
        print("=========================================")
    
    if orientation==True:
        print("ORIENTATION")
        print(df.info())
        print("=========================================")
        print()
        
    
    if formatIssues==True:
        print("FORMAT ISSUES")
        print()
        for col in df.columns:
            if df[col].dtype == 'object' or df[col].dtype == 'int64' or df[col].dtype == 'datetime64':
                print("df['" + col + "'] = df['" + col + "'].replace('old_value', 'new_value')")
                print("df['" + col + "'] = df['" + col + "'].astype('new_type') # new_type can be int64, float64, object, category, datetime64")
                print("df.drop('" + col + "', axis=1, inplace=True)")                
                pd.set_option('display.max_rows', None)
                print(df.groupby(col, sort=True).size())
                pd.reset_option('display.max_rows')
                #display the dtypes of the column
                print("Current Column DType: ", df[col].dtype, "     Do not compare with above. This one will always return int64 as it's the dtype of the count")                
                print("df['" + col + "'] = df['" + col + "'].astype('new_type') # new_type can be int64, float64, object, category, datetime64")
                print()
            #else:
            #    print(col)
            #    print(df[col].describe())
            #    print()

        if tips==True:
            print("TIPS")
            print("To make a correction to a column, use the following syntax:")
            print("df['A'] = df['A'].apply(lambda x: x.replace('old_value', 'new_value'))")
            print()
            print("To change a column data type, use the following syntax:")
            print("df['A'] = pd.to_datetime(df['A']) # for datetime")
            print("df['A'] = df['A'].astype('int64') # for integers")
            print("df['A'] = df['A'].astype('float64') # for floats")
            print("df['A'] = df['A'].astype('category') # for categorical")
            print("df['A'] = df['A'].astype('object') # for object")
            print()
        print("=========================================")
        print()

    if missingValues==True:
        print("MISSING VALUES")
        print()
        for col in df.columns:
            if df[col].isnull().sum() > 0:
                print(col, ":", df[col].isnull().sum(), " missing values")
                print("df.dropna(subset=['" + col + "'], inplace=True)")
                print("df['" + col + "'].fillna(df['" + col + "'].mean(), inplace=True) #fill NA entries with the mean")
                print("df['" + col + "'].fillna(0, inplace=True) # fill NA entries with a single value, such as zero")
                print()
                print(df.loc[df[col].isnull()].head())
                print()
            else:
                print(col, ": No missing values")
                print()
                                    
        if tips==True:
            print()
            print("TIPS")
            print("You can drop rows with missing values using one of the following code:")
            print("df.dropna(subset=['col'], inplace=True) #For a single column")
            print("df.dropna(inplace=True) #For all columns")
            print()
            print("You can fill rows with missing values using one of the following code:")
            print("df['col'].fillna(df['col'].mean(), inplace=True) #fill NA entries with the mean")
            print("df['col'].fillna(0, inplace=True) # fill NA entries with a single value, such as zero")
            print("df['col'].fillna(method='ffill') # forward-fill to propagate the previous value forward")
            print("df['col'].fillna(method='bfill' # back-fill to propagate the next values backward)")
            print()
            print("To view them:")
            print("df.loc[df[col].isnull()].head()")
            print()
        print("=========================================")
        print()

    if duplicateValues==True:
        print("DUPLICATE VALUES")
        print()
        print(df[df.duplicated()].head())
        print()

        if tips==True:
            print("TIPS")
            print("You can drop duplicate rows using the following code:")
            print("df.drop_duplicates(inplace=True)")
            print("df.drop_duplicates(subset=['col'], inplace=True) #For a single column")
            print()
            print("To view them:")
            print("df[df.duplicated()].head()")
            print()
    
        print("=========================================")
        print()

    if outliers==True:
        print("OUTLIERS")
        print()
        for col in df.columns:
            if df[col].dtype == 'int64' or df[col].dtype == 'float64':
                print(col)
                print("-----")
                print("Outlier(s):")
                print("Below ", df[col].mean() - 3*df[col].std(), " -> ", df[df[col] < df[col].mean() - 3*df[col].std()].shape[0], " low outlier(s)")
                print("Above ", df[col].mean() + 3*df[col].std(), " -> ", df[df[col] > df[col].mean() + 3*df[col].std()].shape[0], " high outlier(s)")
                low = df[col].mean() - 3*df[col].std()
                high = df[col].mean() + 3*df[col].std()
                print("df = df[(df['" + col + "'] > " + str(low) + ") & (df['" + col + "'] < " + str(high) + ")]")
                print()
                print(df[col].describe())
                print()
                print("Boxplot")
                sns.boxplot(df[col])
                plt.show()
                print()
                print("Histogram")
                sns.histplot(df[col])
                plt.show()
                print("=========================================")
                print()

        if tips==True:
            print("TIPS")
            print("You can drop outliers using the following code:")
            print("df = df[(df['column'] > lower_bound) & (df['column'] < upper_bound)]")
            print()
```
### Clean - Formatting Issues
```python
# Display the values of each columns to look for formatting issues
for col in df.columns:
    if df[col].dtype == 'object' or df[col].dtype == 'int64' or df3[col].dtype == 'datetime64':
        print(col)
        print(df[col].unique())
        print()
    else:
        print(col)
        print(df[col].describe())
        print()

```
Further Investigate
```python
#df['column'].unique()
#display unique values for column A in alphabetical order
#df['column'].unique().tolist()
#df['column'].describe()
#sns.histplot(df['column'])
```
Dropping all redundant/useless columns
```python
df.drop(['A', 'B'], axis=1, inplace=True)
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
df['Column'][(np.abs(stats.zscore(df['Column'])) > 3)]    # .describe() add if you want to see the details of the outliers
##Z-scores above 3 indicate the value is greater than 3 standard deviations from the mean. Data Scientists often label values with a z-score above 3 as outliers.

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
# Feature Engineering (Variable Transformation)
## Log Transformation
```python
#plot original distribution of Insulin
diabetes_df['Insulin'].plot.hist()

#plot distribution of Insulin after log transformation
np.log(diabetes_df['Insulin']).plot.hist()
```
## Binning
```python
#Binning with q-cut (bin according to quantiles)
pd.qcut(diabetes_df['Age'], q = 4).value_counts()

#Binning with cut (equally sized bins)
pd.cut(diabetes_df['Age'], bins = 4).value_counts()
```
## Scaling
### Scale entire DF
```python
#summary statistics before scaling
df.describe()

#use MinMaxScaler to scale data into a given range ((0,1) by default)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled = pd.DataFrame(scaler.fit_transform(df))

#summary statistics after scaling
scaled.describe()
```
### Scale single value
```python
# Standard Scaler
from sklearn.preprocessing import scale
A = scale(A, with_std=True)

# Min/Max Scaler
from sklearn.preprocessing import MinMaxScaler
A = MinMaxScaler(A)

# Old fashioned way
X['age_scaled'] = (X['age'] - X['age'].min()) / (X['age'].max() - X['age'].min()) * 10
```
## Convert categorical feature into multiple dummy variables
```python
#Print Pregnancies column
diabetes_df['Pregnancies']

#convert Pregnancies column into multiple dummy variables
pd.get_dummies(diabetes_df['Pregnancies'])

#convert Pregnancies column into multiple dummy variables in the same dataframe
pd.get_dummies(diabetes_df, prefix='preg', columns=['Pregnancies'])



## Alternate way to do it
# Since scikit-learn algorithms accept only numerical variables, we need to convert all categorical variables into numeric types.
# We will use the LabelEncoder class from the scikit-learn library to do this.
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

# New variable for outlet
data['Outlet'] = le.fit_transform(data['Outlet_Identifier'])

# New variable for Item_Fat_Content
data['Item_Fat_Content'] = le.fit_transform(data['Item_Fat_Content'])

# New variable for Item_Type
data['Item_Type'] = le.fit_transform(data['Item_Type'])

# New variable for Item_Category
data['Item_Category'] = le.fit_transform(data['Item_Category'])

# New variable for Outlet_Size
data['Outlet_Size'] = le.fit_transform(data['Outlet_Size'])

# New variable for Outlet_Location_Type
data['Outlet_Location_Type'] = le.fit_transform(data['Outlet_Location_Type'])

# New variable for Outlet_Type
data['Outlet_Type'] = le.fit_transform(data['Outlet_Type'])

# Drop the columns which have been converted to different types
data.drop(['Item_Identifier','Outlet_Identifier','Outlet_Establishment_Year'],axis=1,inplace=True)

```
# Sampling and dimensionality reduction
## Splitting Data into a 'Training' and a 'Testing' set
### Holdout split
```python
# import the **train_test_split** function from sklearn
from sklearn.model_selection import train_test_split

# Split the data to train set and test set, use a 70:30 ratio or a 80:20 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # 70:30 ratio
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 80:20 ratio

# split the data with the parameter shuffle = False
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)

# print the shape of X_train and X_test
print(X_train.shape)
print(X_test.shape)
```
### K-fold split
```python
# import the KFold function from sklearn
from sklearn.model_selection import KFold

# instantiate KFold with k=5
kf = KFold(n_splits=5)

print("Normal:")

# iterate over train_index and test_index in kf.split(X) and print them
for train_index, test_index in kf.split(X):
    print('Train Index: ', train_index)
    print('Test Index: ', test_index, '\n')

### Same as above, but with shuffle = True
# instantiate KFold with k=5 and shuffle=True
kf = KFold(n_splits=5, shuffle=True, random_state=42)

print('\n', "Shuffle:")

# iterate over train_index and test_index in kf.split(X) and print them
for train_index, test_index in kf.split(X):
    print('Train Index: ', train_index)
    print('Test Index: ', test_index, '\n')
```
### Leave-One-Out split
```python
# Each observation is used as test set separately.
## Popular method for tiny datasets.
## It takes a lot of time with bigger datasets and can lead to overfitting on a final model.

# import the LeaveOneOut function from sklearn
from sklearn.model_selection import LeaveOneOut

# instantiate LeaveOneOut
loo = LeaveOneOut()

# iterate over train_index and test_index in loo.split(X) and print them
for train_index, test_index in loo.split(X):
    print('Train Index: ', train_index)
    print('Test Index: ', test_index, '\n')
    
# Print the number of splits
print(loo.get_n_splits(X))
```
## Resampling (Class Imbalance)
https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/

### 1) Can You Collect More Data?
You might think it’s silly, but collecting more data is almost always overlooked.

Can you collect more data? Take a second and think about whether you are able to gather more data on your problem.

A larger dataset might expose a different and perhaps more balanced perspective on the classes.

More examples of minor classes may be useful later when we look at resampling your dataset.

### 2) Try Changing Your Performance Metric
Accuracy is not the metric to use when working with an imbalanced dataset. We have seen that it is misleading.

There are metrics that have been designed to tell you a more truthful story when working with imbalanced classes.

I give more advice on selecting different performance measures in my post “Classification Accuracy is Not Enough: More Performance Measures You Can Use“.

In that post I look at an imbalanced dataset that characterizes the recurrence of breast cancer in patients.

From that post, I recommend looking at the following performance measures that can give more insight into the accuracy of the model than traditional classification accuracy:

Confusion Matrix: A breakdown of predictions into a table showing correct predictions (the diagonal) and the types of incorrect predictions made (what classes incorrect predictions were assigned).
Precision: A measure of a classifiers exactness.
Recall: A measure of a classifiers completeness
F1 Score (or F-score): A weighted average of precision and recall.
I would also advice you to take a look at the following:

Kappa (or Cohen’s kappa): Classification accuracy normalized by the imbalance of the classes in the data.
ROC Curves: Like precision and recall, accuracy is divided into sensitivity and specificity and models can be chosen based on the balance thresholds of these values.
You can learn a lot more about using ROC Curves to compare classification accuracy in our post “Assessing and Comparing Classifier Performance with ROC Curves“.

Still not sure? Start with kappa, it will give you a better idea of what is going on than classification accuracy.


### 3) Try Resampling Your Dataset
You can change the dataset that you use to build your predictive model to have more balanced data.

This change is called sampling your dataset and there are two main methods that you can use to even-up the classes:

You can add copies of instances from the under-represented class called over-sampling (or more formally sampling with replacement), or
You can delete instances from the over-represented class, called under-sampling.
These approaches are often very easy to implement and fast to run. They are an excellent starting point.

In fact, I would advise you to always try both approaches on all of your imbalanced datasets, just to see if it gives you a boost in your preferred accuracy measures.

You can learn a little more in the the Wikipedia article titled “Oversampling and undersampling in data analysis“.


Some Rules of Thumb
Consider testing under-sampling when you have an a lot data (tens- or hundreds of thousands of instances or more)
Consider testing over-sampling when you don’t have a lot of data (tens of thousands of records or less)
Consider testing random and non-random (e.g. stratified) sampling schemes.
Consider testing different resampled ratios (e.g. you don’t have to target a 1:1 ratio in a binary classification problem, try other ratios)

### 4) Try Generate Synthetic Samples
A simple way to generate synthetic samples is to randomly sample the attributes from instances in the minority class.

You could sample them empirically within your dataset or you could use a method like Naive Bayes that can sample each attribute independently when run in reverse. You will have more and different data, but the non-linear relationships between the attributes may not be preserved.

There are systematic algorithms that you can use to generate synthetic samples. The most popular of such algorithms is called SMOTE or the Synthetic Minority Over-sampling Technique.

As its name suggests, SMOTE is an oversampling method. It works by creating synthetic samples from the minor class instead of creating copies. The algorithm selects two or more similar instances (using a distance measure) and perturbing an instance one attribute at a time by a random amount within the difference to the neighboring instances.

Learn more about SMOTE, see the original 2002 paper titled “SMOTE: Synthetic Minority Over-sampling Technique“.

There are a number of implementations of the SMOTE algorithm, for example:

In Python, take a look at the “UnbalancedDataset” module. It provides a number of implementations of SMOTE as well as various other resampling techniques that you could try.
In R, the DMwR package provides an implementation of SMOTE.
In Weka, you can use the SMOTE supervised filter.

### 5) Try Different Algorithms
As always, I strongly advice you to not use your favorite algorithm on every problem. You should at least be spot-checking a variety of different types of algorithms on a given problem.

For more on spot-checking algorithms, see my post “Why you should be Spot-Checking Algorithms on your Machine Learning Problems”.

That being said, decision trees often perform well on imbalanced datasets. The splitting rules that look at the class variable used in the creation of the trees, can force both classes to be addressed.

If in doubt, try a few popular decision tree algorithms like C4.5, C5.0, CART, and Random Forest.

For some example R code using decision trees, see my post titled “Non-Linear Classification in R with Decision Trees“.

For an example of using CART in Python and scikit-learn, see my post titled “Get Your Hands Dirty With Scikit-Learn Now“.

### 6) Try Penalized Models
You can use the same algorithms but give them a different perspective on the problem.

Penalized classification imposes an additional cost on the model for making classification mistakes on the minority class during training. These penalties can bias the model to pay more attention to the minority class.

Often the handling of class penalties or weights are specialized to the learning algorithm. There are penalized versions of algorithms such as penalized-SVM and penalized-LDA.

It is also possible to have generic frameworks for penalized models. For example, Weka has a CostSensitiveClassifier that can wrap any classifier and apply a custom penalty matrix for miss classification.

Using penalization is desirable if you are locked into a specific algorithm and are unable to resample or you’re getting poor results. It provides yet another way to “balance” the classes. Setting up the penalty matrix can be complex. You will very likely have to try a variety of penalty schemes and see what works best for your problem.

### 7) Try a Different Perspective
There are fields of study dedicated to imbalanced datasets. They have their own algorithms, measures and terminology.

Taking a look and thinking about your problem from these perspectives can sometimes shame loose some ideas.

Two you might like to consider are anomaly detection and change detection.

Anomaly detection is the detection of rare events. This might be a machine malfunction indicated through its vibrations or a malicious activity by a program indicated by it’s sequence of system calls. The events are rare and when compared to normal operation.

This shift in thinking considers the minor class as the outliers class which might help you think of new ways to separate and classify samples.

Change detection is similar to anomaly detection except rather than looking for an anomaly it is looking for a change or difference. This might be a change in behavior of a user as observed by usage patterns or bank transactions.

Both of these shifts take a more real-time stance to the classification problem that might give you some new ways of thinking about your problem and maybe some more techniques to try.


### 8) Try Getting Creative
Really climb inside your problem and think about how to break it down into smaller problems that are more tractable.

For inspiration, take a look at the very creative answers on Quora in response to the question “In classification, how do you handle an unbalanced training set?”

For example:

Decompose your larger class into smaller number of other classes…

…use a One Class Classifier… (e.g. treat like outlier detection)

…resampling the unbalanced training set into not one balanced set, but several. Running an ensemble of classifiers on these sets could produce a much better result than one classifier alone

These are just a few of some interesting and creative ideas you could try.

For more ideas, check out these comments on the reddit post “Classification when 80% of my training set is of one class“.

## Principal Component Analysis
### PCA Function
The steps of PCA have been consolidated into this function:
```python
def runPCA (data, componentsNumber):
    # Import required librairies
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import scale

    # Set data to A
    A = data

    # Scale the data
    A = scale(A, with_std=True)  #Std scaler
    ## can also use a min/max scaler

    # Run a PCA over the data
    pca = PCA(n_components=componentsNumber) #change to the number of components you want to keep
    pca.fit(A)
    A_pca = pca.transform(A)

    return A_pca
```
### Basic PCA use:
```python
# Setting our data
X = df10.drop(['cust_id', 'street_nbr', 'postal_code', 'gender', 'name_prefix', 'first_name', 'last_name', 'street_name', 'city_name', 'state_code', 'cc_creditUsed_perc', 'ck_tran_avg'], axis = 1) 

# Run PCA
data_pca = runPCA(X, 2)

# That's it
data_pca.shape
```
### Using PCA for 2D Scatter Plot
```python
import plotly.express as px

# Setting our data
X = df10.drop(['cust_id', 'street_nbr', 'postal_code', 'gender', 'name_prefix', 'first_name', 'last_name', 'street_name', 'city_name', 'state_code', 'cc_creditUsed_perc', 'ck_tran_avg'], axis = 1) 

# plot the data_pca and set the color of each cluster based on the 3rd column of the tuple using plotly
data_pca = runPCA(X, 2) #highly recommended you run you PCA with 2 dimensions

# Add the colour column to data_pca
data_pca = np.append(data_pca, X['AI_cluster'].values.reshape(-1, 1), axis=1)

# Make the Scatter Plot
fig = px.scatter(data_pca, x=0, y=1, color=2)

# Force the size of the plot
fig.update_layout(
    autosize=False,
    width=900,
    height=900,
)

# Set the title
fig.update_layout(
    title={
        'text': "PCA - Clustered with Age & Income",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

#Show the legend
fig.update_layout(showlegend=True)

#Set the legend
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="right",
    x=0.01
))

# Set the x and y axis limits
fig.update_xaxes(range=[-5, 5])
fig.update_yaxes(range=[-5, 5])

# Label the axes
fig.update_xaxes(title_text='PC1')
fig.update_yaxes(title_text='PC2')

#add the loadings to the plot
fig.add_trace(go.Scatter(x=[0, 1], y=[0, 0], mode='lines', name='PC1', line=dict(color='red', width=2)))
fig.add_trace(go.Scatter(x=[0, 0], y=[0, 1], mode='lines', name='PC2', line=dict(color='blue', width=2)))

fig.show()
```

### Using PCA for 3D Scatter Plot
```python
X = df10.drop(['cust_id', 'street_nbr', 'postal_code', 'gender', 'name_prefix', 'first_name', 'last_name', 'street_name', 'city_name', 'state_code', 'cc_creditUsed_perc', 'ck_tran_avg'], axis = 1) 

# Run PCA over your data
data_pca = runPCA(X, 3)

# Add the colour column to data_pca, you can add many, they will be added in order
data_pca = np.append(data_pca, X['AI_cluster'].values.reshape(-1, 1), axis=1)
data_pca = np.append(data_pca, X['IS_cluster'].values.reshape(-1, 1), axis=1)

# Make the Scatter Plot
fig = px.scatter_3d(data_pca, x=0, y=1, z=2, color=3, labels={'0': 'PC 1', '1': 'PC 2', '2': 'PC 3'})

# Set the title
fig.update_layout(
    title={
        'text': "PCA - Clustered with Age & Income",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

#Change the dots' size
fig.update_traces(marker=dict(size=3))

# Add the loadings
fig.add_trace(go.Scatter3d(
    x=[0, 1],
    y=[0, 0],
    z=[0, 0],
    mode='lines',
    line=dict(color='red', width=2),
    name='PC 1'
))
fig.add_trace(go.Scatter3d(
    x=[0, 0],
    y=[0, 1],
    z=[0, 0],
    mode='lines',
    line=dict(color='green', width=2),
    name='PC 2'
))
fig.add_trace(go.Scatter3d(
    x=[0, 0],
    y=[0, 0],
    z=[0, 1],
    mode='lines',
    line=dict(color='blue', width=2),
    name='PC 3'
))

fig.show()
```

Some extras (TO DETERMINE IF KEEPING)
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

# Plot a scree plot to determine the number of principal components you want to keep. Use the elbow rule.
pca = PCA()
pca.fit(wine_df)
plt.plot(pca.explained_variance_ratio_)
plt.show()

# Create a cumulative explained_variance_ratio plot. Determine the number of principal components you want to keep. Use the elbow rule.
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.show()

# Refit your PCA with the chosen optimal number of principal components and project the principal components to a DataFrame. Also, you should name the columns of the DataFrame appropriately.
pca = PCA(n_components=3)
pca.fit(wine_df)
wine_pca = pca.transform(wine_df)
wine_pca_df = pd.DataFrame(wine_pca, columns=['PC1', 'PC2', 'PC3'])
wine_pca_df

# Export the data with the new features to a CSV file. The number of rows should be the same as in the original dataset.
#wine_pca_df.to_csv('wine_pca.csv', index=False)
```

## Variable Selection
More details at this link:
https://data.compass.lighthouselabs.ca/days/w05e/activities/520
```python
import pandas as pd
df_numeric = pd.read_csv('df_numeric.csv')

y = df_numeric.SalePrice
df_numeric.drop("SalePrice",axis=1, inplace=True)

from sklearn.feature_selection import VarianceThreshold

vt = VarianceThreshold(0.1)
df_transformed = vt.fit_transform(df_numeric)

# columns we have selected
# get_support() is method of VarianceThreshold and stores boolean of each variable in the numpy array.
selected_columns = df_numeric.columns[vt.get_support()]
# transforming an array back to a data-frame preserves column labels
df_transformed = pd.DataFrame(df_transformed, columns = selected_columns)

import numpy as np

# step 1
df_corr = df_transformed.corr().abs()

# step 2
indices = np.where(df_corr > 0.8) 
indices = [(df_corr.index[x], df_corr.columns[y]) 
for x, y in zip(*indices)
    if x != y and x < y]

# step 3
for idx in indices: #each pair
    try:
        df_transformed.drop(idx[1], axis = 1, inplace=True)
    except KeyError:
        pass

#print(indices)

from sklearn.feature_selection import f_regression, SelectKBest
skb = SelectKBest(f_regression, k=10)
X = skb.fit_transform(df_transformed, y)

# this will give us the position of top 10 columns
skb.get_support()
# column names
df_transformed.columns[skb.get_support()]
X = pd.DataFrame(X,columns=df_transformed.columns[skb.get_support()])
X

```

# Modeling Techniques - Unsupervised Learning
## Clustering
A set of functions that allow to use all 3x clusters easily
- clusterPrep() -> Provides an overview graph, elbow methow and dendogram
- clusterPlot() -> Provides with K-Mean Clustering, Hierarchical and DBSCAN

- plot_clusters -> Used to plot clusters, generally don't call this one directly. It's a sub-function
### Cluster Functions
```python
# Setting up the function that will plot and display the cluster
def plot_clusters(X,y_res, plt_cluster_centers = False):
    X_centroids = []
    Y_centroids = []

    for cluster in set(y_res):
        x = X[y_res == cluster,0]
        y = X[y_res == cluster,1]
        X_centroids.append(np.mean(x))
        Y_centroids.append(np.mean(y))

        plt.scatter(x,
                    y,
                    s=50,
                    marker='s',
                    label=f'cluster {cluster}')

    if plt_cluster_centers:
        plt.scatter(X_centroids,
                    Y_centroids,
                    marker='*',
                    c='red',
                    s=250,
                    label='centroids')
    plt.legend()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.show()


def clusterPrep(X, y, x_label="X axis", y_label="Y axis", overview=True, elbowrule=True, dendogram=True):
    #Required Librairies
    import matplotlib.pyplot as plt
    import numpy as np

    if overview==True:
        #plot the data for an overview
        plt.rcParams["figure.figsize"] = (12,8) #set figure size
        plt.scatter(X, y, c='black', marker='o', edgecolor='black', s=50) #c='black' is the color of the dots, s=50 is the size of the dots, edgecolor='black' is the color of the border of the dots, marker='o' is the shape of the dots
        # Set the labels
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid()
        plt.show()


    # Elbow function
    if elbowrule == True:
        max_clusters
        distortions = []
        for i in range(1, max_clusters +1):
            km = KMeans(n_clusters=i,
                        init='k-means++',
                        n_init=10,
                        random_state=0)
            km.fit(X)
            distortions.append(km.inertia_)

        plt.plot(range(1,max_clusters +1), distortions, marker='o')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()


    # define plot_dendrogram function
    if dendogram == True:
        method ='ward'
        dendrogram = sch.dendrogram(sch.linkage(X, method=method))
        plt.title("Dendrogram")
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        plt.show()
        
def clusterPlot(X, cluster_K=3, cluster_H=3, dbeps=0.8, dbSample=2, kmean=True, hierarch=True, dbscan=True):
    from sklearn.cluster import KMeans #For KMeans

    from sklearn.cluster import AgglomerativeClustering #hierarchy
    import scipy.cluster.hierarchy as sch #hierarchy

    from sklearn.datasets import make_moons #DBSCAN
    from sklearn.cluster import DBSCAN #DBSCAN

    ### K-Means
    if kmean == True:
        # Instantiate the KMeans class
        km = KMeans(n_clusters=cluster_K, # how many clusters we expect. SEE ELBOW METHOD TO HELP DETERMINE
                    n_init=10, # how many initial runs
                    random_state=0)


        # fit and predict
        y_km = km.fit_predict(X)

        # plot clustering result
        plot_clusters(X, y_km, plt_cluster_centers= True) #If you want the centers plotted

    ### Hierarchical
    if hieararch == True:
        # create an object
        ac = AgglomerativeClustering(affinity='euclidean',
                                     linkage='ward',
                                     n_clusters = cluster_H) #Number of clusters. SEE DENDOGRAM TO HELP DETERMINE

        # fit and predict
        y_hc = ac.fit_predict(X)

        # Plot clustering result
        plot_clusters(X,y_hc)


    ### DBScan
    if dbscan == True:
        # create an instance of DBSCAN class from the Sklearn library:
        db = DBSCAN(eps=dbeps,
                    min_samples=dbSample,
                    metric='euclidean')

        # We created the instance of DBSCAN class with a few parameters we didn't use before:

        ## eps: The maximum distance between two samples for one to be considered as being in the neighborhood of the other. This is not a maximum bound on the distances of points within a cluster. It is the most important DBSCAN parameter to choose appropriately for our dataset and distance function.

        ## min_samples: The number of samples in a neighborhood for a point to be considered as a core point. This includes the point itself.

        # fit and predict
        y_db = db.fit_predict(X)

        # Plot DBSCAN clusters
        plot_clusters(X,y_db)
```

### Set Librairies and values
```python
#Required Librairies
import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans #For KMeans

from sklearn.cluster import AgglomerativeClustering #hierarchy
import scipy.cluster.hierarchy as sch #hierarchy

from sklearn.datasets import make_moons #DBSCAN
from sklearn.cluster import DBSCAN #DBSCAN

# If your data is contained into columns of a df, set it to x and y below
x = df['column1']
y = df['column2']

# Merge the two columns into a Numpy Array
X = np.array(list(zip(x, y)))


# You can also use the make blobs function for tests/samples
# generate clusters 
#X, y = make_blobs(n_samples=150,
#                  n_features=2,
#                  centers=3,
#                  cluster_std=0.5,
#                  random_state=0)


#plot the data for an overview
plt.rcParams["figure.figsize"] = (12,8) #set figure size
plt.scatter(X[:, 0], X[:, 1], c='black', marker='o', edgecolor='black', s=50) #c='black' is the color of the dots, s=50 is the size of the dots, edgecolor='black' is the color of the border of the dots, marker='o' is the shape of the dots
# Set the labels
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
```

### Plot Custer Function
```python
# Setting up the function that will plot and display the cluster
def plot_clusters(X,y_res, plt_cluster_centers = False):
    X_centroids = []
    Y_centroids = []

    for cluster in set(y_res):
        x = X[y_res == cluster,0]
        y = X[y_res == cluster,1]
        X_centroids.append(np.mean(x))
        Y_centroids.append(np.mean(y))

        plt.scatter(x,
                    y,
                    s=50,
                    marker='s',
                    label=f'cluster {cluster}')

    if plt_cluster_centers:
        plt.scatter(X_centroids,
                    Y_centroids,
                    marker='*',
                    c='red',
                    s=250,
                    label='centroids')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
```
### K-Means Clustering (Distance-based, good for blobs)
#### Elbow Method (Determine # of clusters for K-Means)
```python
# A great tool for deciding how many clusters to choose (and therefore to evaluate our model) is the elbow rule in a distortion plot. 

def plot_distortion(X,max_clusters = 10):
    distortions = []
    for i in range(1, max_clusters +1):
        km = KMeans(n_clusters=i,
                    init='k-means++',
                    n_init=10,
                    random_state=0)
        km.fit(X)
        distortions.append(km.inertia_)

    plt.plot(range(1,max_clusters +1), distortions, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Distortion')
    plt.show()

# Call the elbow function
plot_distortion(X,max_clusters=10)
```

#### K-Means Clustering 
```python
# Instantiate the KMeans class
km = KMeans(n_clusters=3, # how many clusters we expect. SEE ELBOW METHOD TO HELP DETERMINE
            n_init=10, # how many initial runs
            random_state=0)


# fit and predict
y_km = km.fit_predict(X)

# plot clustering result
plot_clusters(X, y_km, plt_cluster_centers= True) #If you want the centers plotted
#plot_clusters(X, y_km) #If you don't want the centers plotted
```
### Hierarchical Clustering
#### Dendogram (Determine # Clusters for Hierarchical Clustering)
```python
#To identify the right number of clusters we can plot a dendrogram. Let's define the function that plots a dendrogram:

# define plot_dendrogram function
def plot_dendrogram(X,method ='ward'):
    dendrogram = sch.dendrogram(sch.linkage(X, method=method))
    plt.title("Dendrogram")
    plt.ylabel("Euclidean distances")
    plt.xlabel('Points')
    plt.show()

# Plot dendrogram
plot_dendrogram(X)
```
#### Hierachical Clustering
```python
# create an object
ac = AgglomerativeClustering(affinity='euclidean',
                             linkage='ward',
                             n_clusters = 3) #Number of clusters. SEE DENDOGRAM TO HELP DETERMINE

# We set the Euclidean distance to the affinity parameter and set the number of clusters to three. We also set the linkage parameter to the "ward". The linkage criteria determine the metric used for the merge strategy:

## ward minimizes the sum of squared differences within all clusters. It is a variance-minimizing approach and, in this sense, is similar to the k-means objective function but tackled with an agglomerative hierarchical approach.

## maximum or complete linkage minimizes the maximum distance between observations of pairs of clusters.

## average linkage minimizes the average of the distances between all observations of pairs of clusters.

## single linkage minimizes the distance between the closest observations of pairs of clusters.

# fit and predict
y_hc = ac.fit_predict(X)

# Plot clustering result
plot_clusters(X,y_hc)
```
### Density Based Clustering (DBSCAN)
```python
# create an instance of DBSCAN class from the Sklearn library:
db = DBSCAN(eps=0.5,
            min_samples=5,
            metric='euclidean')

# We created the instance of DBSCAN class with a few parameters we didn't use before:

## eps: The maximum distance between two samples for one to be considered as being in the neighborhood of the other. This is not a maximum bound on the distances of points within a cluster. It is the most important DBSCAN parameter to choose appropriately for our dataset and distance function.

## min_samples: The number of samples in a neighborhood for a point to be considered as a core point. This includes the point itself.

# fit and predict
y_db = db.fit_predict(X)

# Plot DBSCAN clusters
plot_clusters(X,y_db)
```
## Generative Networks

## Dimension Reduction
# Modeling Techniques - Supervised Learning
## Classification

### Random Forest Classifier
```python
import RandomForestClassifier from sklearn

model = RandomForestClassifier

model.fit(X, Y) # learning

predictions = model.predict(X) # make predictions

model.score(X,Y) #Evaluation of the model

```
## Regression
### (Simple and Multiple) Linear Regression Model using Statsmodels

```python
import pandas as pd
import statsmodels.api as sm

# data = {'year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
#         'month': [12,11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
#         'interest_rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
#         'unemployment_rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
#         'index_price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]        
#         }

# Convert your data in a DF to start
df = pd.DataFrame(data) 

x = df.drop(['index_price', 'interest_rate','unemployment_rate'], axis = 1) # Start with your entire DF minus your y value. Add values here as you drop.
y = df['index_price']

x = sm.add_constant(x) # adding a constant

model = sm.OLS(y, x).fit()
# Above is sometimes done in two steps
# lin_reg = sm.OLS(y,X)
# model = lin_reg.fit()

predictions = model.predict(x) 

print_model = model.summary()
print(print_model)
```

### (Simple and Multiple) Linear Regression using sklearn

```python
#Import the model
from sklearn.linear_model import LinearRegression

# set values same as above

# initialize the object and fit the model on our data:
regressor = LinearRegression()
regressor.fit(X, y)

# This gives us an overview of the parameters we can set up for linear regression in sklearn. The most important one is fit_intercept. In sklearn, we don't have to add a constant to a dataset. We have to set this parameter to the value True if we want to compute an intercept as well.

# We can check the beta coefficient now:
print(regressor.coef_)

# This will show us a NumPy array with beta coefficients. They have the same order as our columns in X. the first one is 0 because we have added a constant column before statsmodel modeling. This column doesn't have any meaning is sklearn so we could have dropped that before.

# We can see that the results look much nicer in the statsmodel package. Another huge disadvantage of sklearn is that we don't have access to p-values, so we cannot check the importance of different variables for prediction.

#If we want to know the R-squared, we can get it with:
regressor.score(X,y)

```


### Interpreting the Regression Results
- Adjusted. R-squared reflects the fit of the model. R-squared values range from 0 to 1, where a higher value generally indicates a better fit, assuming certain conditions are met.
  
- const coefficient is your Y-intercept. It means that if both the interest_rate and unemployment_rate coefficients are zero, then the expected output (i.e., the Y) would be equal to the const coefficient.
- interest_rate coefficient represents the change in the output Y due to a change of one unit in the interest rate (everything else held constant)
- unemployment_rate coefficient represents the change in the output Y due to a change of one unit in the unemployment rate (everything else held constant)
- std err reflects the level of accuracy of the coefficients. The lower it is, the higher is the level of accuracy
- P >|t| is your p-value. A p-value of less than 0.05 is considered to be statistically significant
- Confidence Interval represents the range in which our coefficients are likely to fall (with a likelihood of 95%)

### Polynomial Regression
The main difference between multinomial and polynomial regression is that we still use only one feature but with many transformations.

#### Multiple features (Set to 1 for single feature)
```python
def poly_reg(X,y,degree=2,plot=False):
    """
    X = df.drop(['y_column'], axis = 1) 
    or
    X = df[["x_1", "x_2"]]
    
    y = df["y"]

    degree: degree of the polynomial (the higher, the more complex curved lines you can create). default = 2

    plot: Whether to display your raw data or not. Default = False
    """
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    # Split data into training and test data
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import LinearRegression

    if plot == True:
        # Display data into subplots
        
        # Determine the number of x columns
        x_columns = X.shape[1]

        # Create a figure with subplots
        fig, axs = plt.subplots(x_columns, 1, figsize=(10, 10))

        # Plot each x column against y
        for i in range(x_columns):
            axs[i].scatter(X.iloc[:, i], y)
            axs[i].set_title(X.columns[i])
            axs[i].set_ylabel(y.name)
        
        plt.show()


    # create the new polynomial features.
    poly = PolynomialFeatures(degree=degree, include_bias=False) 
    poly_features = poly.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=42) # Within the train_test_split method we define all of our features (poly_features) and all of our responses (y). Then, with test_size we set what percentage of our all features

    # Create polynomial regression model
    poly_reg_model = LinearRegression()
    poly_reg_model.fit(X_train, y_train)

    # Test how model performs on previously unseen data:
    poly_reg_y_predicted = poly_reg_model.predict(X_test) # save the predicted values our model predicts based on the previously unseen feature values (X_test)
    from sklearn.metrics import mean_squared_error
    poly_reg_rmse = np.sqrt(mean_squared_error(y_test, poly_reg_y_predicted)) # We take the square root of mean_squared_error to get the RMSE (root mean square error) which is a commonly used metric to evaluate a machine learning model’s performance. RMSE shows how far the values your model predicts
    print("Polynomial Reg RMSE: ", poly_reg_rmse) #  Roughly speaking: the smaller the RMSE, the better the model.

    # Create a linear regression model to compare the performance
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    lin_reg_model = LinearRegression()
    lin_reg_model.fit(X_train, y_train)
    lin_reg_y_predicted = lin_reg_model.predict(X_test)
    lin_reg_rmse = np.sqrt(mean_squared_error(y_test, lin_reg_y_predicted))
    print("Linear Reg RMSE (degree = 1): ", lin_reg_rmse)

    print()
    print("RMSE (root mean square error) which is a commonly used metric to evaluate a machine learning model’s performance. RMSE shows how far the values your model predicts are from the true values (y_test), on average. Roughly speaking: the smaller the RMSE, the better the model.")

```
#### Single Feature
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0, 30)
y = [3, 4, 5, 7, 10, 8, 9, 10, 10, 23, 27, 44, 50, 63, 67, 60, 62, 70, 75, 88, 81, 87, 95, 100, 108, 135, 151, 160, 169, 179]
# plt.figure(figsize=(10,6))
# plt.scatter(x, y)
# plt.show()

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# set an instance of PolynomialFeatures with the following settings:
poly = PolynomialFeatures(degree=2, include_bias=False)
## degree=2 means that we want to work with a 2nd degree polynomial: y = ß0 + ß1x + ß2x2

## LinearRegression() will take care of this setting by default, so there’s no need to set include_bias to True. If it wasn’t taken care of, then include_bias=False would mean that we deliberately want the y intercept (ß0) to be equal to 0 – but we don’t want that. Here’s a great explanation on all of this: https://stackoverflow.com/questions/59725907/scikit-learn-polynomialfeatures-what-is-the-use-of-the-include-bias-option

# fit our data to the model:
poly_features = poly.fit_transform(x.reshape(-1, 1))
## reshape(-1,1) transforms our numpy array x from a 1D array to a 2D array – this is required, otherwise we’d get the following error:

# Create the polynomial regression model
poly_reg_model = LinearRegression()

# Fit model to data
poly_reg_model.fit(poly_features, y)

# Now that our model is properly trained, we can put it to work by instructing it to predict the responses (y_predicted) based on poly_features, and the coefficients it had estimated:Now that our model is properly trained, we can put it to work by instructing it to predict the responses (y_predicted) based on poly_features, and the coefficients it had estimated:
y_predicted = poly_reg_model.predict(poly_features)

# Display Polynomial Regression
plt.figure(figsize=(10, 6))
plt.title("Your first polynomial regression – congrats! :)", size=16)
plt.scatter(x, y)
plt.plot(x, y_predicted, c="red")
plt.show()

```
# Model Optimization 
## Gradient Descent

## Stochastic Gradient Descent

# Model Evaluation

## Regression Metrics

### Mean Squared Error (MSE)
```python
# import numpy
import numpy as np

# generate 'ground truth'
y_true = np.random.normal(0,1,10)

# generate random errors
errors = np.random.normal(0,0.02,10)

# simulate predictions
y_pred = y_true + errors

# import MSE from sklearn
from sklearn.metrics import mean_squared_error

# compute MSE
MSE = mean_squared_error(y_true,y_pred)  

# print MSE
print(MSE)
```
MSE or Mean Squared Error is one of the most preferred metrics for regression tasks. It is simply the average of the squared difference between the target value and the value predicted by the regression model. As it squares the differences, it penalizes even a small error which leads to over-estimation of how bad the model is. It is preferred more than other metrics because it is differentiable and hence can be optimized better.


### Root-Mean-Squared-Error (RMSE)
```python
# import numpy
import numpy as np

# generate 'ground truth'
y_true = np.random.normal(0,1,10)

# generate random errors
errors = np.random.normal(0,0.02,10)

# simulate predictions
y_pred = y_true + errors

# RMSE by Numpy
RMSE = np.sqrt(MSE)
print(RMSE)

# RMSE by sklearn
RMSE = mean_squared_error(y_true,y_pred,squared=False)
print(RMSE)
```
RMSE is the most widely used metric for regression tasks and is the square root of the averaged squared difference between the target value and the value predicted by the model. It is preferred more in some cases because the errors are first squared before averaging which poses a high penalty on large errors. This implies that RMSE is useful when large errors are undesired.

### Mean-Absolute-Error (MAE)
```python
import numpy as np
from sklearn.datasets import make_regression

X,y = make_regression(n_features=10, n_samples=1000, noise=10)
print(X.shape)
print(y.shape)

from sklearn.linear_model import LinearRegression, Ridge
# creating linear regression
lr = LinearRegression()
lr.fit(X,y)
y_lr = lr.predict(X)

# creating ridge regression
rr = Ridge(alpha=0.1)
rr.fit(X,y)
y_rr = rr.predict(X)

#### MAE
# import mean_absolute_error from sklearn
import sklearn.metrics as metrics
from sklearn.metrics import mean_absolute_error

# calculate MAE for linear regression
mae_lr = metrics.mean_absolute_error(y, y_lr)

# calculate MAE for ridge regression
mae_rr = metrics.mean_absolute_error(y, y_rr)

# According to MAE, what is the better model?
print("MAE for linear regression: ", mae_lr)
print("MAE for ridge regression: ", mae_rr)
print("MAE for linear regression is better: ", mae_lr < mae_rr)

## The lower the MAE, the better the model
```
MAE is the absolute difference between the target value and the value predicted by the model. The MAE is more robust to outliers and does not penalize the errors as extremely as mse. MAE is a linear score which means all the individual differences are weighted equally. It is not suitable for applications where you want to pay more attention to the outliers.

### R² or Coefficient of Determination
```python
#### Preparation
import numpy as np
from sklearn.datasets import make_regression

X,y = make_regression(n_features=10, n_samples=1000, noise=10)
print(X.shape)
print(y.shape)

from sklearn.linear_model import LinearRegression, Ridge
# creating linear regression
lr = LinearRegression()
lr.fit(X,y)
y_lr = lr.predict(X)

# creating ridge regression
rr = Ridge(alpha=0.1)
rr.fit(X,y)
y_rr = rr.predict(X)

#### R2 
# import sklearn.metrics as metrics
from sklearn.metrics import r2_score

# compute R2
r2_lr = r2_score(y, y_lr)
r2_rr = r2_score(y, y_rr)

# According to R2, what is the better model?
print("R2 for linear regression: ", r2_lr)
print("R2 for ridge regression: ", r2_rr)
print("R2 for linear regression is better: ", r2_lr > r2_rr)

## The higher the R2, the better the model
```
Coefficient of Determination or R² is another metric used for evaluating the performance of a regression model. The metric helps us to compare our current model with a constant baseline and tells us how much our model is better. The constant baseline is chosen by taking the mean of the data and drawing a line at the mean. R² is a scale-free score that implies it doesn't matter whether the values are too large or too small, the R² will always be less than or equal to 1.

### Adjusted R²
```python
# Buils on R2 so do R2 first.

#### Adjusted R2
# compute adjusted R2 (Linear Regression)
adj_r2_lr = 1 - (1-r2_lr)*(len(y)-1)/(len(y)-X.shape[1]-1)

# compute adjusted R2 (Ridge Regression)
adj_r2_rr = 1 - (1-r2_rr)*(len(y)-1)/(len(y)-X.shape[1]-1)

# According to adjusted R2, what is the better model?
print("Adjusted R2 for linear regression: ", adj_r2_lr)
print("Adjusted R2 for ridge regression: ", adj_r2_rr)
print("Adjusted R2 for linear regression is better: ", r2_lr > r2_rr)

## The higher the adjusted R2, the better the model
```
Adjusted R² depicts the same meaning as R² but is an improvement of it. R² suffers from the problem that the scores improve on increasing terms even though the model is not improving which may misguide the researcher. Adjusted R² is always lower than R² as it adjusts for the increasing predictors and only shows improvement if there is a real improvement.

There is a misconception among people that the R² score ranges from 0 to 1 but actually, it ranges from -∞ to 1. Due to this misconception, they are sometimes scared why the R² is negative which is not a possibility according to them.

## Classification Metrics
For better visualization of the performance of a model, these four outcomes are plotted on a confusion matrix.
![IMG](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image11-6.png)
### Accuracy
```python
# ground truth
y_true = [1,1,0,1,0,0,1,0,0,1]

# simulate probabilites of positive class
y_proba = [0.9,0.7,0.2,0.99,0.7,0.1,0.5,0.2,0.4,0.6]

# set the threshold to predict positive class
thres = 0.5

# class predictions
y_pred = [int(value > thres) for value in y_proba]

## Accuracy
# import accuracy_score from sklearn
from sklearn.metrics import accuracy_score

# compute accuracy
accuracy = accuracy_score(y_true,y_pred)

# print accuracy
print(accuracy)
```
Accuracy = Number of correct predictions / Total number of predictions.
![IMG](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image14-2.png)
### Precision/Recall
```python

#### Preparation
from sklearn.linear_model import LogisticRegression, RidgeClassifier

# creating linear regression
lr = LogisticRegression()
lr.fit(X,y)
y_lr = lr.predict(X)

# creating ridge regression
rr = RidgeClassifier(alpha=0.1)
rr.fit(X,y)
y_rr = rr.predict(X)

​
#### Precision score
# import precision_score from sklearn
from sklearn.metrics import precision_score

# compute precision
precision_lr = precision_score(y, y_lr)
precision_rr = precision_score(y, y_rr)

#print precision
print("Precision for linear regression: ", precision_lr)
print("Precision for ridge regression: ", precision_rr)
print("Precision for linear regression is better: ", precision_lr > precision_rr,'\n')

#### Recall score
# import recall_score from sklearn
from sklearn.metrics import recall_score

# compute recall
recall_lr = recall_score(y, y_lr)
recall_rr = recall_score(y, y_rr)

#print recall
print("Recall for linear regression: ", recall_lr)
print("Recall for ridge regression: ", recall_rr)
print("Recall for linear regression is better: ", recall_lr > recall_rr)
```
Recall gives the fraction you correctly identified as positive out of all positives.
![IMG](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image15-2.png)

Precision gives the fraction of correctly identified as positive out of all predicted as positives.
![IMG](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image19-2.png)

Precision-Recall Tradeoff   
In general for most classifiers, there is going to be a trade-off between recall and precision as you vary the probability threshold.
![IMG](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image23.gif)

If you need to compare different models with different precision-recall value, It is often convenient to combine precision and recall into a single metric. Correct!! We need a metric that considers both recall and precision to compute the performance. -> F1-score
### F1-score
```python
# ground truth
y_true = [1,1,0,1,0,0,1,0,0,1]

# simulate probabilites of positive class
y_proba = [0.9,0.7,0.2,0.99,0.7,0.1,0.5,0.2,0.4,0.6]

# set the threshold to predict positive class
thres = 0.5

# class predictions
y_pred = [int(value > thres) for value in y_proba]

## F1-Score
# import f1_score from sklearn
from sklearn.metrics import f1_score

# compute F1-score
f1_score = f1_score(y_true,y_pred)

# print F1-score
print(f1_score)
```
It is defined as the harmonic mean of the model’s precision and recall.
![IMG](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image24.png)

We use Harmonic mean because it is not sensitive to extremely large values, unlike simple averages. Say, we have a model with a precision of 1, and recall of 0 gives a simple average as 0.5 and an F1 score of 0. If one of the parameters is low, the second one no longer matters in the F1 score. The F1 score favors classifiers that have similar precision and recall. Thus, the F1 score is a better measure to use if you are seeking a balance between Precision and Recall.
### ROC curve/AUC score
#### ROC curve
```python
#### Preparation
import numpy as np
from sklearn.datasets import make_regression

X,y = make_regression(n_features=10, n_samples=1000, noise=10)
print(X.shape)
print(y.shape)

from sklearn.linear_model import LinearRegression, Ridge
# creating linear regression
lr = LinearRegression()
lr.fit(X,y)
y_lr = lr.predict(X)

# creating ridge regression
rr = Ridge(alpha=0.1)
rr.fit(X,y)
y_rr = rr.predict(X)

#### ROC Curve
# import roc_curve from sklearn
from sklearn.metrics import roc_curve

# compute and store ROC curve values in fpr, tpr, thresholds variables
fpr_lr, tpr_lr, thresholds_lr = roc_curve(y, y_lr)
fpr_rr, tpr_rr, thresholds_rr = roc_curve(y, y_rr)

import matplotlib.pyplot as plt

# plot ROC curve
plt.plot(fpr_lr, tpr_lr, label='ROC curve for linear regression (area = %0.2f)')
plt.plot(fpr_rr, tpr_rr, label='ROC curve for ridge regression (area = %0.2f)')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.legend(loc="lower right")
plt.show()
```
#### AUC Score
```python
# ground truth
y_true = [1,1,0,1,0,0,1,0,0,1]

# simulate probabilites of positive class
y_proba = [0.9,0.7,0.2,0.99,0.7,0.1,0.5,0.2,0.4,0.6]

# set the threshold to predict positive class
thres = 0.5

# class predictions
y_pred = [int(value > thres) for value in y_proba]

## AUC-score
# import roc_auc_score from sklearn
from sklearn.metrics import roc_auc_score

# compute AUC-score
auc = roc_auc_score(y_true,y_proba)

# print AUC-score
print(auc)
```
The receiver operator characteristic is another common tool used for evaluation. It plots out the sensitivity and specificity for every possible decision rule cutoff between 0 and 1 for a model. For classification problems with probability outputs, a threshold can convert probability outputs to classifications. we get the ability to control the confusion matrix a little bit. So by changing the threshold, some of the numbers can be changed in the confusion matrix. But the most important question here is, how to find the right threshold? Of course, we don’t want to look at the confusion matrix every time the threshold is changed, therefore here comes the use of the ROC curve.

For each possible threshold, the ROC curve plots the False positive rate versus the true positive rate.

False Positive Rate: Fraction of negative instances that are incorrectly classified as positive.

True Positive Rate: Fraction of positive instances that are correctly predicted as positive.

Now, think about having a low threshold. So amongst all the probabilities arranged in ascending order, everything below bad is considered as negative and everything above 0.1 is considered as positive. By choosing this, you’re being very liberal.

![IMG](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image25.png)

But if you set your threshold as high, say 0.9.
![IMG](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image1-11.png)

Below is the ROC curve for the same model at different threshold values.
![IMG](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image2-11.png)

From the above graph, it can be seen that the true positive rate increases at a higher rate but suddenly at a certain threshold, the TPR starts to taper off. For every increase in TPR, we have to pay a cost, the cost of an increase in FPR. At the initial stage, the TPR increase is higher than FPR

So, we can select the threshold for which the TPR is high and FPR is low.

Now, let’s see what different values about TPR and FPR tell us about the model.
![IMG](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image3-9.png)

For different models, we will have a different ROC curve. Now, how to compare different models? From the above plot, it is clear that the curve is in the upper triangle, the good the model is.  One way to compare classifiers is to measure the area under the curve for ROC.
![IMG](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/image4-9.png)

AUC(Model 1) > AUC(Model 2) > AUC(Model 2)

Thus Model 1 is the best of all.
### Lift Curves
A lift chart pictures gains from applying a classification model in comparison to not applying it (i.e. using a random classifier) for a given section of data.

4 types of LIFT curves can be considered.
LIFT with percentage scale
1. accumulated
2. non-accumulated
LIFT with quotient scale
3. accumulated
4. non-accumuated

more info:
https://algolytics.com/tutorial-how-to-establish-quality-and-correctness-of-classification-models-part-5-lift-curve/

### Log-Loss
```python
#### Preparation
import numpy as np
from sklearn.datasets import make_regression

X,y = make_regression(n_features=10, n_samples=1000, noise=10)
print(X.shape)
print(y.shape)

from sklearn.linear_model import LinearRegression, Ridge
# creating linear regression
lr = LinearRegression()
lr.fit(X,y)
y_lr = lr.predict(X)

# creating ridge regression
rr = Ridge(alpha=0.1)
rr.fit(X,y)
y_rr = rr.predict(X)

#### Log-Loss
# import log_loss from sklearn
from sklearn.metrics import log_loss

# compute log-loss
log_loss_lr = log_loss(y, y_lr)
log_loss_rr = log_loss(y, y_rr)

#print log-loss
print("Log-loss for linear regression: ", log_loss_lr)
print("Log-loss for ridge regression: ", log_loss_rr)
print("Log-loss for linear regression is better: ", log_loss_lr < log_loss_rr)

## The lower the log-loss, the better the model
```
# Machine Learning - Reinforcement Learning
# Machine Learning - Semi-Supervised Learning
# VSCode
## SQLite
# Useful Functions


## OLS Regression Results Function
```python
def getOLS(x,y,Option = 0):
    """
    This function will provide you with OLS Regression Results for your dataset.

    Recommended nomenclature for x:
    df.drop(['y_column'], axis = 1) 
    
    Start with your entire DF minus your y value. 
    You can then easily add values here as you drop them.

    Recommended nomenclature for y:
    df['y_column']

    By default, the function will print the model, but if you want to do anything further, modify accordingly using Option for different scenarios.
    """
    import pandas as pd
    import statsmodels.api as sm
    
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    predictions = model.predict(x)
    print_model = model.summary()

    if Option == 0:
        print(print_model)
```
















