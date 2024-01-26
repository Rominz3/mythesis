import pandas as pd
df = (pd.read_excel(R"C:\Users\ROMINA\Desktop\delete nan\data\3\isfahan(11).xlsx"))


def change(old,new,column):
    column_name = 'column_name_to_replace_in'
    df[column] = df[column].replace(old, new)



change(0,"صاف","HAVA_2")
change(1,"ناصاف","HAVA_2")
change(0,"روز","ROSHANAEI_2")
change(1,"شب","ROSHANAEI_2")
change(0,"خشک","SHARAYET_SATH_RAH_2")
change(1,"تر","SHARAYET_SATH_RAH_2")
change(0,"شانه ندارد","NOE_SHANE_RAH_2")
change(1,"شانه دارد","NOE_SHANE_RAH_2")
change(0,"spring","TARIKH_SHAMSI_2")
change(1,"summer","TARIKH_SHAMSI_2")
change(2,"fall","TARIKH_SHAMSI_2")
change(3,"winter","TARIKH_SHAMSI_2")
change(0,"بر خورد موتورسيكلت با عابر","NOE_BARKHORD_2")
change(1,"برخورد با وسایل سبک","NOE_BARKHORD_2")
change(2,"برخورد وسيله نقليه با  موتورسيكلت","NOE_BARKHORD_2")
change(0,"مستقیم","HENDESE_MAHAL_2")
change(1,"پیچ","HENDESE_MAHAL_2")
change(0,"ندارد","AMEL_ENSANI_2")
change(1,"دارد","AMEL_ENSANI_2")
change(0,"ندارد","AMEL_VASILH_2")
change(1,"دارد","AMEL_VASILH_2")
change(0,"ندارد","NAGHS_RAH_2")
change(1,"دارد","NAGHS_RAH_2")
change(0,"age_1","SEN_RANADEH_4")
change(1,"age_2","SEN_RANADEH_4")
change(2,"age_3","SEN_RANADEH_4")
change(0,"مرد","GENSIAT_4")
change(1,"زن","GENSIAT_4")
change(0,"education_1","TAHSILAT_4")
change(1,"education_2","TAHSILAT_4")
change(2,"education_3","TAHSILAT_4")
change(0,"ندارد","NOE_GAVAHINAME_4")
change(1,"دارد","NOE_GAVAHINAME_4")
change(0,"weekday","weekday")
change(1,"weekend","weekday")
change(0,"مسطح","slope")
change(1,"شیبدار","slope")
change(0,"day","time_of_day")
change(1,"peak","time_of_day")
change(2,"night","time_of_day")
change(0,"صدمه نديده","NOE_SADAME_4")
change(1,"مصدوم","NOE_SADAME_4")
change(2,"فوت","NOE_SADAME_4")

df.to_excel(R"C:\Users\ROMINA\Desktop\delete nan\data\4\isfahan(11).xlsx", index=False)


