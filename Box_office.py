#%%
import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#%%
# get the response in the form of html
url="https://en.wikipedia.org/wiki/List_of_films_impacted_by_the_COVID-19_pandemic"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(url)
print(response.status_code)

# %%
url = "https://en.wikipedia.org/wiki/List_of_films_impacted_by_the_COVID-19_pandemic"
df_list = pd.read_html(url)

#%%
df = df_list[1]
print(df)
#%%
df.to_excel(r'C:\Users\scari\Documents\DS 499\vod.xlsx', index=False)


#%%
df2 = df_list[2]
print(df2)
# %%
df2.to_excel(r'C:\Users\scari\Documents\DS 499\int.xlsx', index=False)

#%%
df3 = df_list[3]
print(df3)
#%%
df3.to_excel(r'C:\Users\scari\Documents\DS 499\forward.xlsx', index=False)

#%%
df4 = df_list[4]
print(df4)
#%%
df4.to_excel(r'C:\Users\scari\Documents\DS 499\delayed.xlsx', index=False)

#%%
df5 = df_list[5]
print(df5)
#%%
df5.to_excel(r'C:\Users\scari\Documents\DS 499\cancelled.xlsx', index=False)


# %%
