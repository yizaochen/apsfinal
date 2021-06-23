import pandas as pd
from tabulate import tabulate
import numpy as np
from scipy.stats import chi2_contingency

class TBTAgent:

    def __init__(self, csv_in):
        self.csv_in = csv_in
        self.df = self.read_csv()

    def read_csv(self):
        return pd.read_csv(self.csv_in)

    def show_two_by_two_table(self, feature1, feature2, age_criteria, gluc_criteria, bmi_criteria, d_worktype):
        tbt = TwoByTwoTable(feature1, feature2, self.df, age_criteria, gluc_criteria, bmi_criteria, d_worktype)
        table = tbt.get_table()
        print(table)

    def get_odds_ratio_and_CI(self, feature1, feature2, age_criteria, gluc_criteria, bmi_criteria, d_worktype):
        tbt = TwoByTwoTable(feature1, feature2, self.df, age_criteria, gluc_criteria, bmi_criteria, d_worktype)
        theta, ci_left, ci_right = self.get_CI(tbt)
        print(f'theta: {theta:.3f}')
        print(f'CI of log(theta): ({ci_left:.3f}, {ci_right:.3f})')

    def get_CI(self, tbt):
        a, b, c, d = tbt.get_abcd()
        theta = (a * d) / (b * c)
        log_theta = np.log(theta)
        inner_term = (1/a) + (1/b) + (1/c) + (1/d)
        ci = 1.96 * np.sqrt(inner_term)
        ci_left = log_theta - ci
        ci_right = log_theta + ci
        return theta, ci_left, ci_right

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
                     'Residence_type': {'Rural': ['Rural'], 'Urban': ['Urban']},
                     'smoking_status': {'Smoke': ['smokes', 'formerly smoked'], 'No smoke': ['never smoked']},
                     'stroke': {'Stroke': [1], 'No Stroke': [0]}

    }
    
    def __init__(self, feature1, feature2, df, age_criteria, gluc_criteria, bmi_criteria, d_worktype):
        self.feature1 = feature1 # Top
        self.feature2 = feature2 # Left
        self.df = df
        self.d_data = {i: dict() for i in range(4)}
        self.num_crit = {'age': age_criteria, 
                         'avg_glucose_level': gluc_criteria, 
                         'bmi': bmi_criteria}
        self.d_subcategory['work_type'] = d_worktype

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


class ContigencyAgent:
    feature_cates = {'age': ['<50', '50-60', '60-70', '70-80', '80-90'],
                     'age_detail': ['10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90'],
                     'work_type': ['Private', 'Self-employed', 'Govt_job'],
                     'smoking_status' : ['never smoked', 'formerly smoked', 'smokes'],
                     'avg_glucose_level': ['<80', '80-110', '110-160', '>160'],
                     'bmi': ['Underweight', 'Normal', 'Overweight'],
                     'stroke': ['Stroke', 'No Stroke']}

    feature_values = {'age': ['<50', '50-60', '60-70', '70-80', '80-90'],
                      'age_detail': ['10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90'],
                      'work_type': ['Private', 'Self-employed', 'Govt_job'],
                      'smoking_status' : ['never smoked', 'formerly smoked', 'smokes'],
                      'avg_glucose_level': ['<80', '80-110', '110-160', '>160'],
                      'bmi': ['Underweight', 'Normal', 'Overweight'],
                      'stroke': [1, 0]}

    def __init__(self, csv_in):
        self.df = pd.read_csv(csv_in)

    def show_contingency_table(self, feature1, feature2):
        data_array = self.initialize_data_array(feature1, feature2)
        data_array = self.get_table(data_array, feature1, feature2)
        table = tabulate(data_array, tablefmt='fancy_grid')
        print(table)
        chi2, p, dof, ex = self.get_chi_square(data_array, feature1)
        print(f'X-square={chi2:.2f}, df={dof}, p-value={p:.3e}')
        return data_array

    def show_contingency_table_include_expected_values(self, feature1, feature2):
        data_array = self.initialize_data_array(feature1, feature2)
        data_array = self.get_table(data_array, feature1, feature2)
        chi2, p, dof, ex = self.get_chi_square(data_array, feature1)
        data_array = self.add_expected_value_into_data_array(data_array, ex, feature1, feature2)
        table = tabulate(data_array, tablefmt='fancy_grid')
        print(table)
        print(f'X-square={chi2:.2f}, df={dof}, p-value={p:.3e}')
        return data_array, ex

    def get_table_shape(self, feature1, feature2):
        n_row = len(self.feature_cates[feature2]) + 2
        n_col = len(self.feature_cates[feature1]) + 2
        return n_row, n_col

    def initialize_data_array(self, feature1, feature2):
        n_row, n_col = self.get_table_shape(feature1, feature2)
        return np.empty((n_row,n_col), dtype=object)

    def get_table(self, data_array, feature1, feature2):
        n_row, n_col = self.get_table_shape(feature1, feature2)
        data_array[0,0] = ''
        data_array[0,n_col-1] = 'Row Total'
        data_array[n_row-1,0] = 'Column Total'

        for idx, subfeature in enumerate(self.feature_cates[feature1]):
            data_array[0,idx+1] = subfeature # Put title on the top row
        for idx, subfeature in enumerate(self.feature_cates[feature2]):
            data_array[idx+1,0] = subfeature # Put title on the most left column

        for idx_f1, subfeature1 in enumerate(self.feature_values[feature1]):
            for idx_f2, subfeature2 in enumerate(self.feature_values[feature2]):                
                df_temp_1 = self.df[self.df[feature1] == subfeature1]

                if feature2 == 'age':
                    mask = self.get_age_mask(df_temp_1, subfeature2)
                    df_temp_2 = df_temp_1[mask]
                elif feature2 == 'age_detail':
                    mask = self.get_age_detail_mask(df_temp_1, subfeature2)
                    df_temp_2 = df_temp_1[mask]                    
                elif feature2 == 'work_type':
                    df_temp_2 = df_temp_1[df_temp_1[feature2] == subfeature2]
                elif feature2 == 'avg_glucose_level':
                    mask = self.get_glucose_mask(df_temp_1, subfeature2)
                    df_temp_2 = df_temp_1[mask]
                elif feature2 == 'bmi':
                    mask = self.get_bmi_mask(df_temp_1, subfeature2)
                    df_temp_2 = df_temp_1[mask]
                elif feature2 == 'smoking_status':
                    mask = (df_temp_1[feature2] == subfeature2)
                    df_temp_2 = df_temp_1[mask]

                data_array[idx_f2+1, idx_f1+1] = df_temp_2.shape[0]

        # Row Total
        for row_id in range(len(self.feature_cates[feature2])):
            data_array[row_id+1, n_col-1] = data_array[row_id+1, 1:-1].sum()

        # Column Total
        for col_id in range(len(self.feature_cates[feature1])):
            data_array[n_row-1, col_id+1] = data_array[1:-1, col_id+1].sum()

        # Total
        data_array[n_row-1, n_col-1] = data_array[1:-1, n_col-1].sum()
        return data_array

    def add_expected_value_into_data_array(self, data_array, expected_values, feature1, feature2):
        for idx_f1 in range(len(self.feature_values[feature1])):
            for idx_f2 in range(len(self.feature_values[feature2])):
                observed_value = data_array[idx_f2+1, idx_f1+1]
                expected_value = expected_values[idx_f1, idx_f2]
                new_data_value = f'{observed_value} ({expected_value:.1f})'
                data_array[idx_f2+1, idx_f1+1] = new_data_value
        return data_array

    def get_age_mask(self, df_in, age_range):
        d_mask = {'<50': df_in['age'] < 50, 
                  '50-60': (df_in['age'] >= 50) & (df_in['age'] < 60), 
                  '60-70': (df_in['age'] >= 60) & (df_in['age'] < 70), 
                  '70-80': (df_in['age'] >= 70) & (df_in['age'] < 80),
                  '80-90': df_in['age'] >= 80}
        return d_mask[age_range]

    def get_age_detail_mask(self, df_in, age_range):
        d_mask = {'10-20': (df_in['age'] >= 10) & (df_in['age'] < 20),
                  '20-30': (df_in['age'] >= 20) & (df_in['age'] < 30),
                  '30-40': (df_in['age'] >= 30) & (df_in['age'] < 40),
                  '40-50': (df_in['age'] >= 40) & (df_in['age'] < 50),
                  '50-60': (df_in['age'] >= 50) & (df_in['age'] < 60), 
                  '60-70': (df_in['age'] >= 60) & (df_in['age'] < 70), 
                  '70-80': (df_in['age'] >= 70) & (df_in['age'] < 80),
                  '80-90': (df_in['age'] >= 80) & (df_in['age'] < 90)}
        return d_mask[age_range]

    def get_glucose_mask(self, df_in, glu_range):
        d_mask = {'<80': df_in['avg_glucose_level'] < 80, 
                  '80-110': (df_in['avg_glucose_level'] >= 80) & (df_in['avg_glucose_level'] < 110), 
                  '110-160': (df_in['avg_glucose_level'] >= 110) & (df_in['avg_glucose_level'] < 160), 
                  '>160': df_in['avg_glucose_level'] >= 160}
        return d_mask[glu_range]

    def get_bmi_mask(self, df_in, bmi_range):
        d_mask = {'Underweight': df_in['bmi'] < 18.5, 
                  'Normal': (df_in['bmi'] >= 18.5) & (df_in['bmi'] < 25), 
                  'Overweight': (df_in['bmi'] >= 27) & (df_in['bmi'] < 30)}
        return d_mask[bmi_range]
    
    def get_chi_square(self, data_array, feature1):
        obs_list = list()
        for col_id in range(len(self.feature_cates[feature1])):
            obs_list.append(data_array[1:-1, col_id+1])
        obs_array = np.array(obs_list)
        chi2, p, dof, ex = chi2_contingency(obs_array, correction=False)
        return chi2, p, dof, ex

