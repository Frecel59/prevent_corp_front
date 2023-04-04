import pandas as pd
import plotly.express as px
# from data_cleaning.cha_cleaning import charac_clean_data_05_18, charac_clean_data_19_21, charac_concatenate_function
# from data_cleaning.lieux_cleaning import lieux_clean_data_12_18, lieux_clean_data_19_21, concatenate_function_lieux
# from data_cleaning.usagers_cleaning import usagers_clean_data_12_18, usagers_clean_data_19_21, concatenate_function_usagers
# from data_cleaning.vehicules_cleaning import vehicules_clean_data_12_18, vehicules_clean_data_19_21, concatenate_function_vehicules



# Concat + csv Caractéristiques

# df_car = concatenate_function_charac("Charactéristiques", charac_clean_data_05_18(), charac_clean_data_19_21())
# df_car


# Concat + csv Lieux

# df_car = concatenate_function_lieux("Lieux", lieux_clean_data_12_18(), lieux_clean_data_19_21())
# df_car


# Concat + csv Usagers
# df_car = concatenate_function_usagers("Usagers", usagers_clean_data_12_18(), usagers_clean_data_19_21())
# df_car


#Concat + csv Véhicules
# df_car = concatenate_function_vehicules("Véhicules", vehicules_clean_data_12_18(), vehicules_clean_data_19_21())
# df_car



# from data_viz_cleaning.caracteristiques import df_clean_car

# df_car = df_clean_car()
# print(df_car.shape)


# from data_viz_cleaning.lieux import df_clean_lieux

# df_lie = df_clean_lie()
# print(df_lie.shape)


# from data_viz_cleaning.vehicules import df_clean_veh

# df_veh = df_clean_veh()
# print(df_veh.shape)


from data_viz_cleaning.usagers import df_clean_usag

df_usag = df_clean_usag()
print(df_usag.shape)
