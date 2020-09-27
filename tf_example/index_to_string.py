import tensorflow as tf
sess=tf.Session()
mapping_string = tf.constant(["emerson", "lake", "palmer"])
indices1 = tf.constant([0,1,2], tf.int64)
indices2 = tf.constant([0,2], tf.int64)
indices3 = tf.constant([1], tf.int64)
table = tf.contrib.lookup.index_to_string_table_from_tensor(
    mapping_string)
values1 = table.lookup(indices1)
values2 = table.lookup(indices2)
values3 = table.lookup(indices3)
sess.run(tf.tables_initializer())

print('mapping:', sess.run(mapping_string))

print('1',sess.run(indices1))
print('1 v;',sess.run(values1))
print(sess.run(indices2))
print(sess.run(values2))
print(sess.run(indices3))
print(sess.run(values3))
