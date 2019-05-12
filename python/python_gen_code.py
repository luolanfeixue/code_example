# -*- coding: utf-8 -*- 
#
# Author : hhl <dnrhhl@gmail.com>
#
# Time : 一 17  9 2018 15:07:24
#
#


sql = "alter table btcf_jd.dwd_brs_jd_online_log_item_d_i_d_a add partition (dt='{0}') location '/user/hive/warehouse/btcf_jd.db/dwd_brs_jd_online_log_item_d_i_d_all/dt={1}';"
dt8='20180101'
dt10='2018-01-01'
import datetime
begin = datetime.date(2017,8,27)
end = datetime.date(2018,9,15)
delta = datetime.timedelta(days=1)
b = begin
while b < end:
    dt8=b.strftime("%Y%m%d")
    dt10=b.strftime("%Y-%m-%d")
    b += delta
    print(sql.format(dt8,dt10))
