from TimeTurner import TimeTurner as tt
import os
import pandas as pd
from datetime import datetime
import re


class FileFilter:

    # TODO: rename method
    @staticmethod
    def awaiting_name(file_path='data/Book3.xlsx',
                      file_type=None,
                      use_columns=['Date', 'From', 'Subject'],
                      from_date=tt.get_start_date(),
                      export_path=f"{os.path.expanduser('~/Desktop')}/filtered"
                      ):

        # read initial file
        if file_type == 'xlsx':
            data = pd.read_excel(file_path, usecols=use_columns)
        elif file_type == 'csv':
            data = pd.read_csv(file_path, usecols=use_columns)
        else:
            return

        start_date = from_date

        # strip UTC and empty spaces in dates
        data.Date = [str(x).replace(' UTC+0000', '') for x in data.Date]
        data.Date = [re.sub(r'\n\d', '', x) for x in data.Date]

        # ======== filter by date, including last report ========

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
            os.mkdir(export_path)
        except:
            pass

        data.to_excel(f'{export_path}/data_{datetime.today().date()}.xlsx')
