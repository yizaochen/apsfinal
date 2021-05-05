from os import path
import pandas as pd
from tabulate import tabulate

class TBTAgent:

    def __init__(self, csv_in):
        self.csv_in = csv_in
        self.df = self.read_csv()

    def read_csv(self):
        return pd.read_csv(self.csv_in)

    def show_two_by_two_table(self, feature1, feature2, age_criteria, gluc_criteria, bmi_criteria):
        tbt = TwoByTwoTable(feature1, feature2, self.df, age_criteria, gluc_criteria, bmi_criteria)
        table = tbt.get_table()
        print(table)

    def print_numerical_mean(self):
        for feature in ['age', 'avg_glucose_level', 'bmi']:
            mean = self.df[feature].mean()
            print(f'Mean of {feature}: {mean:.3f}')


class TwoByTwoTable:

    feature_cates = {'gender': ['Male', 'Female'],
                     'age': ['Young', 'Old'],
                     'hypertension': ['Hypertension', 'Non-Hypertension'],
                     'heart_disease': ['Heart-Disease', 'No-Heart-Disease'],
                     'ever_married': ['Ever-Married', 'Never-Married'],
                     'work_type': ['Work Type 1', 'Work Type 2'],
                     'Residence_type': ['Rural', 'Urban'],
                     'avg_glucose_level': ['Low-Glucose', 'High-Glucose'],
                     'bmi': ['Low-bmi', 'High-bmi'],
                     'smoking_status': ['Smoke', 'No smoke'],
                     'stroke': ['Stroke', 'No Stroke']
    }

    numerical_features = ['age', 'avg_glucose_level', 'bmi']

    d_subcategory = {'gender': {'Male': ['Male'], 'Female': ['Female']},
                     'hypertension': {'Hypertension': [1], 'Non-Hypertension': [0]},
                     'heart_disease': {'Heart-Disease': [1], 'No-Heart-Disease': [0]},
                     'ever_married': {'Ever-Married': ['Yes'], 'Never-Married': ['No']},
                     'work_type': {'Work Type 1': ['children', 'Govt_job', 'Never_worked', 'Self-employed'],
                                   'Work Type 2': ['Private']},
                     'Residence_type': {'Rural': ['Rural'], 'Urban': ['Urban']},
                     'smoking_status': {'Smoke': ['smokes', 'formerly smoked'], 'No smoke': ['never smoked']},
                     'stroke': {'Stroke': [1], 'No Stroke': [0]}

    }
    
    def __init__(self, feature1, feature2, df, age_criteria, gluc_criteria, bmi_criteria):
        self.feature1 = feature1 # Top
        self.feature2 = feature2 # Left
        self.df = df
        self.d_data = {i: dict() for i in range(4)}
        self.num_crit = {'age': age_criteria, 
                         'avg_glucose_level': gluc_criteria, 
                         'bmi': bmi_criteria}

    def get_table(self):
        self.d_data[0][0] = ''
        self.d_data[0][3] = 'Row Total'
        self.d_data[3][0] = 'Column Total'

        self.d_data[0][1] = self.feature_cates[self.feature1][0]
        self.d_data[0][2] = self.feature_cates[self.feature1][1]

        self.d_data[1][0] = self.feature_cates[self.feature2][0]
        self.d_data[2][0] = self.feature_cates[self.feature2][1]

        a, b, c, d = self.get_abcd()
        self.d_data[1][1] = a
        self.d_data[1][2] = b
        self.d_data[2][1] = c
        self.d_data[2][2] = d

        self.d_data[1][3] = a+b
        self.d_data[2][3] = c+d
        self.d_data[3][1] = a+c
        self.d_data[3][2] = b+d
        self.d_data[3][3] = a+b+c+d
        
        table_list = [[i,i,i,i] for i in range(4)]
        for row_id in range(4):
            for col_id in range(4):
                table_list[row_id][col_id] = self.d_data[row_id][col_id]
        return tabulate(table_list, tablefmt='fancy_grid')

    def get_abcd(self):
        if self.feature1 in self.numerical_features:
            df_f1_0, df_f1_1 = self.get_sub_df_by_numerical_f(self.feature1, self.df)
        else:
            df_f1_0 = self.get_sub_df_by_categorical_f(self.feature1, self.df, 0)
            df_f1_1 = self.get_sub_df_by_categorical_f(self.feature1, self.df, 1)
        
        if self.feature2 in self.numerical_features:
            df_f1_f2_00, df_f1_f2_01 = self.get_sub_df_by_numerical_f(self.feature2, df_f1_0)
            df_f1_f2_10, df_f1_f2_11 = self.get_sub_df_by_numerical_f(self.feature2, df_f1_1)
        else:
            df_f1_f2_00 = self.get_sub_df_by_categorical_f(self.feature2, df_f1_0, 0)
            df_f1_f2_01 = self.get_sub_df_by_categorical_f(self.feature2, df_f1_0, 1)
            df_f1_f2_10 = self.get_sub_df_by_categorical_f(self.feature2, df_f1_1, 0)
            df_f1_f2_11 = self.get_sub_df_by_categorical_f(self.feature2, df_f1_1, 1)

        a = df_f1_f2_00.shape[0]
        b = df_f1_f2_10.shape[0]
        c = df_f1_f2_01.shape[0]
        d = df_f1_f2_11.shape[0]
        return a, b, c, d

    def get_sub_df_by_categorical_f(self, feature, df_in, idx_subfeature):
        subfeature = self.feature_cates[feature][idx_subfeature]
        df_list = list()
        for category in self.d_subcategory[feature][subfeature]:
            df_list.append(df_in[df_in[feature] == category])
        return pd.concat(df_list)

    def get_sub_df_by_numerical_f(self, feature, df_in):
        df_small = df_in[df_in[feature] <= self.num_crit[feature]]
        df_big = df_in[df_in[feature] > self.num_crit[feature]]
        return df_small, df_big



