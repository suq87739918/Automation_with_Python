import pandas as pd

df = pd.read_excel("/Users/sunyueqian/Desktop/Automation with Python/complete source code/automation-main/3.Excel Report/supermarket_sales.xlsx")

#select multiple columns
df = df[['Gender', 'Product line', 'Total']]
#print(df)

pivot_table = df.pivot_table(index="Gender", columns="Product line", values="Total",aggfunc="sum").round(0)
#print(pivot_table)

pivot_table.to_excel(excel_writer="pivot_table.xlsx",sheet_name="Report",startrow=4)