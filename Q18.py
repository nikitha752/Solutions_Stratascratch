#Finding Updated Records

import pandas as pd

df = ms_employee_salary.groupby(['id','first_name','last_name','department_id']).salary.agg(salary='max').reset_index()
df
