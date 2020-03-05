import pandas as pd
import config as cf


# xlsx_list = ['/IL_1_kmh.xlsx', '/IL_1_davlenie.xlsx', '/IL_1_temperatura.xlsx', '/IL_1_rashod.xlsx']
# for i in xlsx_list:
#     data_xls = pd.read_excel(cf.base_dir + cf.raw_data + i, index_col=None)
#     data_xls.to_csv(cf.base_dir + cf.converted + '{0}.csv'.format(i[:-5]), encoding='utf-8', index=False)

data = pd.read_csv(cf.base_dir + cf.converted + '/IL_1_davlenie.csv')
data = data.loc[2:]
print(data.columns)