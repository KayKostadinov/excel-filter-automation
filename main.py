from Watcher import Watcher
import os
import pandas as pd
from datetime import datetime
import re
from TimeTurner import TimeTurner as tt

# enable watcher
Watcher.watch('/Users/kay/Downloads')

# read initial file
data = pd.read_excel('data/Book3.xlsx', usecols=['Date', 'From', 'Subject'])

# strip UTC and empty spaces in dates
data.Date = [str(x).replace(' UTC+0000', '') for x in data.Date]
data.Date = [re.sub(r'\n\d', '', x) for x in data.Date]

# ======== filter by date, including last report ========
start_date = tt.get_start_date()

# filter date and remove no-reply cisco mails
data = data.iloc[[index for index, row in data.iterrows()
                  if datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S').date() >= start_date
                  and 'reply' not in row['From']
                  and 'cisco' not in row['From']]]

# remove “RE: “, “FW: “ and trim empty from subject
data.Subject = data.Subject.replace(dict.fromkeys(['RE: ', 'FW: '], ''), regex=True)
data.Subject = [x.strip() for x in data.Subject]

# sort by date
data.sort_values(['Date'], ascending=True)

# export excel
try:
    os.mkdir('./filtered')
except:
    pass

# data.to_excel(f'filtered/data_{datetime.today().date()}.xlsx')



