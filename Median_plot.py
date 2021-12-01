car_data = pd.read_csv('train.csv') # 'train.csv' data source : https://www.kaggle.com/c/mercedes-benz-greener-manufacturing/data

def plot_medians(feature):
    '''This function plots the medians of each category under the selected feature'''
    
     # median values are sorted
    cat_pd = car_data.groupby(feature)['y'].median().sort_values()
    
    # plotting categories vs sorted values
    plt.figure(figsize=(12,4))
    plt.plot(cat_pd)
    plt.xlabel('Feature category')
    plt.ylabel('Median value of y')
    plt.grid()
    plt.title('Median plot of Feature '+feature)
    plt.show()
