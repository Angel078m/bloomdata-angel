# import pandas as pd
# import numpy as np

# test_df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
# null_df = pd.DataFrame(np.array([[1,np.nan,3],[4,5,np.nan],[7,8,9]]))

# def null_count(df):
#     return df.isnull().sum().sum()

# # print(null_count(test_df))
# # print(null_count(null_df))

# def train_test_split(df, frac=0.8):
#     train = df.sample(frac=frac)
#     test = df.drop(train.index).sample(frac=0.1)
#     return train, test

# print(train_test_split(test_df))

import random

adjectives = ['blue', 'large', 'grainy', 'substancial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']


def random_phrase(list1, list2):

    item1 = random.choice(list1)
    item2 = random.choice(list2)
   
    return str(item1) + ' ' + str(item2)

if __name__ == '__main__':
    pass
    #print(random_phrase(adjectives, nouns))
    


