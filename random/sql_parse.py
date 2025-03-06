from sql_metadata import Parser

sql_string = """
-- single line comment
/* comment block */
select column1 as col1, 
column2 as col2 
from mybigtable t1 
inner join myothertable t2 
on t1.column1 = t2.column2 
order by col1 
"""

print(Parser(sql_string).columns_aliases_dict)