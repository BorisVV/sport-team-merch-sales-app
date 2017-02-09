
''' This function are to get information and have less code written for each
    of the for loops or queries '''

from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func, alias

engine = create_engine('sqlite:///merchandise_sales.db', echo=False)
Session = sessionmaker(bind = engine)




def get_all_fromTable(table):
    for items in Session().query(table):
        print(items)

def get_sum_sold_items(table1):
    sum_session = Session()
    sum_sold = sum_session.query(func.sum(table1.quantity_sold)).filter_by(dates_id = 2)

    print(sum_sold)
    for i in sum_sold:
        print(i)
    sum_session.close()

Session().close()



# This is to check if the table has any data or rows in it.
def count_rows(table):
    zero_rows = True
    rows_count = Session().query(table).count()
    if rows_count == 0:
        return zero_rows
    else:
        return zero_rows == False
