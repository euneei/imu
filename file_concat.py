import pandas as pd
import glob


def adl(file_path) :
    df = pd.read_csv(file_path, sep='\t')
    df.columns = ['n','x','y','z']
    df['SVMacc'] = (df['x']**2+df['y']**2+df['z']**2)**(1/2)
    #df['SVMacc'] = math.sqrt(df['x']**2+df['y']**2+df['z']**2)
    df['SVMacc'] = round(df['SVMacc'],6)
    df.drop(['n','x','y','z'],axis = 1, inplace = True)
    df = df.transpose()
    df.insert(0,'y_class',1) # 라벨값에 따라 바꾸기
    return df


file = '.../*.txt'
file_list = glob.glob(file)
dataframes=[]
for file_path in file_list:
    df = pd.read_csv(file_path, delimiter=' ')
    df = adl(file_path)
    dataframes.extend([df])
combined_df1 = pd.concat(dataframes)

data_df = combined_df1
print(data_df.shape)

data_df = pd.DataFrame(data_df)
data_df.to_csv("/.csv")