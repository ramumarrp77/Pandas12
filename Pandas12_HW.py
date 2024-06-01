# Problem 1 : Managers with at Least 5 Direct Reports

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df1 = employee.merge(employee, left_on= 'id', right_on='managerId')
    df2 = df1.groupby(['id_x','name_x'])['id_y'].count().reset_index()
    if len(df2[df2['id_y']>=5]['name_x']) == 0 and len(df1)>0:
        return pd.DataFrame([None], columns = ['name'])
    return df2[df2['id_y']>=5]['name_x'].to_frame().rename(columns={'name_x':'name'})


# Problem 2 : Sales Person 


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df1 = orders.merge(company, on='com_id')
    df1 = df1[df1.name=='RED'][['sales_id','com_id','order_id']]
    df2 = sales_person.merge(df1, on='sales_id',how='left')
    return df2[df2.order_id.isnull()]['name'].to_frame()