# -*- coding: utf-8 -*- 
# # Author : hhl <dnrhhl@gmail.com> #
# Time : 四 09  5 2019 14:53:18
#
#

# 执行不返回值
os.system(
    """
    hive -d yst_day={0} -d now_month_last_day={1} -f fact_true_gd.sql
    """.format(yst_day,now_month_last_day)
    )


# 执行返回值 readlines 返回所有行的具体值
now_sum = os.popen(
    """
    hive -d yst_day={0} -d now_month_last_day={1} -f now_sum.sql
    """.format(yst_day,now_month_last_day)
    ).readlines()[0].replace('\n','')

# 执行返回IO类型的类
data_io = os.popen(
      """
      hive -e "
      set hive.cli.print.header=true;
      set hive.resultset.use.unique.column.names=false;
      select * from blzc_app.credit_crpl_repywillns_predict_feature where dt='{0}';"
      """.format(dt)
      )
data = pd.read_csv(data_io,header=0,sep = "\t",index_col=['product_id','pin'])
data_io.close()
