import tensorflow as tf
import os
import time
from tensorflow.python.ops import resource_variable_ops as rr

graph = tf.Graph()
with graph.as_default():
    original_index_asset_path = tf.constant(os.path.join('test_index.assets'))
    index_asset_path = tf.Variable(original_index_asset_path, name='index_asset_path', trainable=False, collections=[])
    # index_asset_path = rr.ResourceVariable(original_index_asset_path, name='index_asset_path', trainable=False, collections=[])
    assign_index_asset_path = index_asset_path.assign(original_index_asset_path)

    ph_inputs = tf.placeholder(tf.int32, shape=[None])

    with tf.control_dependencies([index_asset_path, assign_index_asset_path]):
        table = tf.contrib.lookup.index_to_string_table_from_file(vocabulary_file=index_asset_path, default_value="UNKNOWN")
        results = table.lookup(tf.cast(ph_inputs, tf.int64))

    tf.add_to_collection(tf.GraphKeys.ASSET_FILEPATHS, original_index_asset_path)


sess = tf.InteractiveSession(graph=graph)

init_op = tf.group(tf.global_variables_initializer(), assign_index_asset_path, tf.tables_initializer())
sess.run(tf.global_variables_initializer())
sess.run(assign_index_asset_path)
sess.run(tf.tables_initializer())


test_results = sess.run(results, feed_dict={ph_inputs:[1, 2]})
print(test_results)


builder = tf.saved_model.builder.SavedModelBuilder(os.path.join('test_index_model', str(int(time.time()))))

model_signature = tf.saved_model.signature_def_utils.build_signature_def(
    inputs={
        "index": tf.saved_model.utils.build_tensor_info(ph_inputs),
    },
    outputs={
        "results": tf.saved_model.utils.build_tensor_info(results),
    },
    method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME)

builder.add_meta_graph_and_variables(
    sess, [tf.saved_model.tag_constants.SERVING],
    signature_def_map={
        tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: model_signature,
    },
    assets_collection=tf.get_collection(tf.GraphKeys.ASSET_FILEPATHS),
    main_op=init_op
)
builder.save()
