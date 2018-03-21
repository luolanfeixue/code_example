drop table if exists btcf.recommend_lda_result;
create table if not exists btcf.recommend_lda_result(
  pin  STRING COMMENT '',
  sku_ids STRING COMMENT '',
  ver double COMMENT '版本'
)
partitioned by(dt STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
stored as textfile;

