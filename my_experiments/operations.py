################################################################################
# A script that plays around with performing operations in tensorflow
################################################################################

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

lin = tf.linspace(1., 5., 5)
add = tf.add(lin, lin)
sub = tf.subtract(add, lin)

with tf.Session() as sess:
    print(sess.run(add))
    print(sess.run(sub))
