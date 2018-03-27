-- 删除分区
ALTER TABLE table_name DROP IF EXISTS PARTITION (dt='20180308')

--添加列
ALTER TABLE table_name ADD COLUMNS (col_name STRING); 


--更改列
CREATE TABLE test_change (a int, b int, c int);
--will change column a's name to a1, a's data type to string, and put it after column b. 
--The new table's structure is: b int, a1 string, c inti
ALTER TABLE test_change CHANGE a a1 STRING AFTER b; 
--will change column b's name to b1, and put it as the first column. 
--The new table's structure is: b1 int, a string, c int
ALTER TABLE test_change CHANGE b b1 INT FIRST;

--更改表的存储格式
alter table btcf.recommend_lda_order_result SET FILEFORMAT textfile;