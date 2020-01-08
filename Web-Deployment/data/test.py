# Convert the datasets in the .csv files to HTML tables
import pandas as pd 

trial_df = pd.read_csv('../../Pymaceuticals/data/clinicaltrial_data.csv')
trial_df.to_html(open('trial_html.txt', 'w'))

mouse_df = pd.read_csv('../../Pymaceuticals/data/mouse_drug_data.csv')
mouse_df.to_html(open('mouse_html.txt', 'w'))