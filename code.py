def univ_plot(col_name, df, fig_size=(25, 10), rot_ticks=80, rot_labels=45, miss=0, top='all', labels = True):
    '''
    To plot univariate visualizations
    Parameters:
        - col_name
        - df: default df
        - fig_size : default (25,10)
        - rot_ticks: rotation of xticks
        - rot_labels: rotation of labels on the barplot 
        - miss: number of first entries to miss/skip 
        - top: number of top entries to include like top 10 or 20
        - labels: flag to show labels on top of bar or not

    Returns:
        - plots the visualization
    '''

    plt.figure(figsize=fig_size)
    plt.title('Univariate Analysis - ' + str(col_name))
    plt.xlabel('Categories')
    plt.ylabel('Count')

    if top == 'all':
        value_counts = df[col_name].value_counts()[miss:]
    else:
        value_counts = df[col_name].value_counts()[miss:int(top)]

    value_counts = value_counts.sort_index()

    values = [int(count) for count in value_counts.values]
    ax = sns.barplot(x=value_counts.index.astype(str), y=values)
    plt.xticks(rotation=rot_ticks)

    # To add labels above each bar
    if labels == True:
      for p, label in zip(ax.patches, values):
        ax.annotate(label, (p.get_x() + 0.25, p.get_height() + 0.5), rotation=rot_labels)

def univ_plot_both(col_name, df1, df2, fig_size=(25, 10), rot_ticks=60, rot_labels=45, miss=0, top='all', labels=True):
    '''
    Plot side-by-side univariate bar graphs for two dataframes with percentage counts. Used for comparing Churned and not churned data.
    Parameters :
        - col_name
        - df1: dataframe1
        - df2: dataframe 2
        - fig_size : default (25,10)
        - rot_ticks: rotation of xticks
        - rot_labels: rotation of labels on the barplot (labels on top of each bar)
        - miss: how many first entries to miss/skip
        - top: how many top entries to show like top 10, or top 20
        - labels: flag to show labels on top of bar or not
        
    Returns:
        - plots the visualization using matplotlib
    '''

    plt.figure(figsize=fig_size)
    plt.title('Univariate Analysis - ' + str(col_name))
    plt.xlabel('Categories')
    plt.ylabel('Percentage')

    if top == 'all':
        value_counts1 = df1[col_name].value_counts(normalize=True)
        value_counts2 = df2[col_name].value_counts(normalize=True)
    else:
        value_counts1 = df1[col_name].value_counts(normalize=True).head(int(top))
        value_counts2 = df2[col_name].value_counts(normalize=True).head(int(top))

    value_counts1 = value_counts1.sort_index()
    value_counts2 = value_counts2.sort_index()

    # Combine categories from both dataframes
    categories = sorted(set(value_counts1.index) | set(value_counts2.index))

    # Filter categories that exist in both dataframes
    categories_exists_in_both = [c for c in categories if c in value_counts1 and c in value_counts2]

    value_counts1 = value_counts1.loc[categories_exists_in_both]
    value_counts2 = value_counts2.loc[categories_exists_in_both]

    values1 = value_counts1.values * 100
    values2 = value_counts2.values * 100

    width = 0.35  # Width of the bars
    x = np.arange(len(categories_exists_in_both))

    # Plotting the bars for DataFrame 1
    plt.bar(x, values1, width, label='DataFrame 1')

    # Plotting the bars for DataFrame 2
    plt.bar(x + width, values2, width, label='DataFrame 2')

    plt.xticks(x + width / 2, categories_exists_in_both, rotation=rot_ticks)

    # To add labels above each bar
    if labels:
        for i, v in enumerate(values1):
            plt.text(i, v + 0.5, f'{v:.2f}%', ha='center', va='bottom', rotation=rot_labels)
        for i, v in enumerate(values2):
            plt.text(i + width, v + 0.5, f'{v:.2f}%', ha='center', va='bottom', rotation=rot_labels)

    plt.legend()

    print(f'Removed columns in DataFrame 1: {len(set(df1[col_name])) - len(set(categories))}')
    print(f'Removed columns in DataFrame 2: {len(set(df2[col_name])) - len(set(categories))}')


def plot_date_time():
  ''' date time column visualization 
      count plot of month, days and hour'''
  pass


def plot_date_time():
  ''' date time column visualization (side by side) - for two dataframes
      count plot of month, days and hour'''
  pass
