################################################################################
# A script that plays around with performing operations in tensorflow
################################################################################

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

tensorA = tf.constant([1.5, 2.5, 3.5])
variableA = tf.Variable(tensorA)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

