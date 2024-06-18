import pandas as pd
import glob


def walk(file_path) :
    df = pd.read_csv(file_path, sep='\t')
    df.columns = ['n','x','y','z']
    df['SVMacc'] = (df['x']**2+df['y']**2+df['z']**2)**(1/2)
    #df['SVMacc'] = math.sqrt(df['x']**2+df['y']**2+df['z']**2)
    df['SVMacc'] = round(df['SVMacc'],6)
    df.drop(['n','x','y','z'],axis = 1, inplace = True)
    df = df.transpose()
    df.insert(0,'y_class',0) # 라벨값에 따라 바꾸기
    return df
def run(file_path) :
    df = pd.read_csv(file_path, sep='\t')
    df.columns = ['n','x','y','z']
    df['SVMacc'] = (df['x']**2+df['y']**2+df['z']**2)**(1/2)
    #df['SVMacc'] = math.sqrt(df['x']**2+df['y']**2+df['z']**2)
    df['SVMacc'] = round(df['SVMacc'],6)
    df.drop(['n','x','y','z'],axis = 1, inplace = True)
    df = df.transpose()
    df.insert(0,'y_class',1) # 라벨값에 따라 바꾸기
    return df

def dangerous(file_path) :
    df = pd.read_csv(file_path, sep='\t')
    df.columns = ['n','x','y','z']
    df['SVMacc'] = (df['x']**2+df['y']**2+df['z']**2)**(1/2)
    #df['SVMacc'] = math.sqrt(df['x']**2+df['y']**2+df['z']**2)
    df['SVMacc'] = round(df['SVMacc'],6)
    df.drop(['n','x','y','z'],axis = 1, inplace = True)
    df = df.transpose()
    df.insert(0,'y_class',2) # 라벨값에 따라 바꾸기
    return df

def normal(file_path) :
    df = pd.read_csv(file_path, sep='\t')
    df.columns = ['n','x','y','z']
    df['SVMacc'] = (df['x']**2+df['y']**2+df['z']**2)**(1/2)
    #df['SVMacc'] = math.sqrt(df['x']**2+df['y']**2+df['z']**2)
    df['SVMacc'] = round(df['SVMacc'],6)
    df.drop(['n','x','y','z'],axis = 1, inplace = True)
    df = df.transpose()
    df.insert(0,'y_class',3) # 라벨값에 따라 바꾸기
    return df

file = '.../*.txt'
file_list = glob.glob(file)
dataframes=[]
for file_path in file_list:
    df = pd.read_csv(file_path, delimiter=' ')
    df = walk(file_path)
    dataframes.extend([df])
combined_df1 = pd.concat(dataframes)

file = '0221/run_0221/*.txt'
file_list = glob.glob(file)
dataframes=[]
for file_path in file_list:
    df = pd.read_csv(file_path, delimiter=' ')
    df = run(file_path)
    dataframes.extend([df])
combined_df2 = pd.concat(dataframes)

file = '0221/oth_0221/*.txt'
file_list = glob.glob(file)
dataframes=[]
for file_path in file_list:
    df = pd.read_csv(file_path, delimiter=' ')
    df = dangerous(file_path)
    dataframes.extend([df])
combined_df3 = pd.concat(dataframes)

file = '../pythonProject3/file/B/B02/*.txt'
file_list = glob.glob(file)
dataframes=[]
for file_path in file_list:
    df = pd.read_csv(file_path, delimiter=' ')
    df = normal(file_path)
    dataframes.extend([df])
combined_df4 = pd.concat(dataframes)



data_df = pd.concat([combined_df1,combined_df2, combined_df3, combined_df4])
print(data_df.shape)

data_df.to_csv("/.csv")
