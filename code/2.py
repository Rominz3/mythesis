import pandas  as pd
df=pd.read_excel(R"C:\Users\ROMINA\Desktop\delete nan\data\2\ilam(11).xlsx")

final_columns={}
def unique(column):
    unique_percentage=[]
    unique_values =list(df[column].unique())
    for item in unique_values:
        item_count = df[column].value_counts()[item]
        percentages = item_count * 100 / len(df.index)
        unique_percentage.append(percentages)
        final_columns[column]=unique_values

    final_columns[column+""+"percentage"]=unique_percentage
    return(final_columns)

unique("HAVA_2")
unique("ROSHANAEI_2")
unique("SHARAYET_SATH_RAH_2")
unique("NOE_SHANE_RAH_2")
unique("TARIKH_SHAMSI_2")
unique("NOE_BARKHORD_2")
unique("HENDESE_MAHAL_2")
unique("AMEL_ENSANI_2")
unique("AMEL_VASILH_2")
unique("NAGHS_RAH_2")
unique("SEN_RANADEH_4")
unique("GENSIAT_4")
unique("TAHSILAT_4")
unique("NOE_GAVAHINAME_4")
unique("weekday")
unique("slope")
unique("time_of_day")
unique("NOE_SADAME_4")

max_len = max(len(val) for val in final_columns.values())

for key in final_columns.keys():
    if len(final_columns[key]) < max_len:
        final_columns[key].extend([None]*(max_len - len(final_columns[key])))
df2=pd.DataFrame(final_columns)
df2.to_excel(R"C:\Users\ROMINA\Desktop\delete nan\data\3\ilam(11).xlsx",index=False)
