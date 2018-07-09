from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

a = tf.constant(2.5)
b = tf.constant(4.5)

total = a + b

tf.summary.scalar("a", a)
tf.summary.scalar("b", b)
tf.summary.scalar("total", total)


# Merge them all
merged_op = tf.summary.merge_all()

with tf.Session() as sess:
    _, summary = sess.run([total, merged_op])
    writer =tf.summary.FileWriter("log", graph=tf.get_default_graph())
    writer.add_summary(summary)
    writer.close()
    

