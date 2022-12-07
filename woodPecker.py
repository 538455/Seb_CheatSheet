def cheatSheet(topic):
    if topic == 'pandas':
        print('https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf')

def dataCleaning(df, code=True, tips=False, orientation=True, formatIssues=True, missingValues=True, duplicateValues=True, outliers=True):
    """
    Consolidation of all data cleaning steps into one function
    
    df: your dataframe

    code: A text template to note your observations as you go. Use the code snippets included in the output. copy-paste into vscode/notepad

    tips: Provides snippets of code to help you clean potential issues in your df. If you prefer this to code
    
    orientation: Provides information about the shape/objects of your data
    
    formatIssues: Provides detailed information on each column to help identify format issues
    
    missingValues: Provides information on missing values
    
    duplicateValues: Provides information on duplicate values
    
    outliers: Provides information on outliers
    """
    if code==True:
        print("Copy this Cleaning Code Template into another file to capture your observations as you go"'\n\n')
        print("### CLEANING CODE:"'\n')
        print("df = dfX #Change to your df's name"'\n')
        print('\n'"#### Column values:"'\n')
        print('\n'"#### Column's dtypes:"'\n')
        print('\n'"#### Rename columns:"'\n')
        print('\n'"#### Missing values:"'\n')
        print('\n'"#### Duplicate values:"'\n')
        print('\n'"#### Outliers:"'\n')
        print('\n'"#### Drop entire column:"'\n')
        print('\n'"#### Other observations / further investigations:")
        print('#\n#\n#\n')
        print('\n'"df.head() #Final Review")
        print("# dfX = df #Change to your df's name"'\n')
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
            if df[col].dtype == 'object' or df[col].dtype == 'int64' or df[col].dtype == 'float64' or df[col].dtype == 'datetime64':
            #if df[col].dtype == 'float64':

                print("df.rename(columns={'" + col + "': ''}, inplace=True)", "#rename column")
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

def dataExploration(df):
    """
    Consolidation of the basic data exploration steps into one function
    
    df: your dataframe

    """


def stringReverse(string):
    """Reverse a string"""
    
    #convert the string into a list
    string_list = list(string)

    #reverse the list
    string_list.reverse()

    #Convert the list back into a string
    string = "".join(string_list)

    #Return the string
    return string

def countUnique(string): 
    """Count the number of unique characters in a string"""
    
    unique_chars = set(string)
    
    #Return the length of the set
    return len(unique_chars)

def readExcel(file_path):
    """Read all the sheets in an excel file and return all the data into a df with a sheet name column"""
    xl = pd.ExcelFile(file_path)
    sheets = xl.sheet_names
    df = pd.DataFrame()
    for sheet in sheets:
        dftemp = pd.read_excel(file_path, sheet_name=sheet)
        dftemp['sheet'] = sheet
        df = pd.concat([df, dftemp])
    return df

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





















































































