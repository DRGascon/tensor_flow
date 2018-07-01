################################################################################
# A script that plays around with transforming tensors
################################################################################

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

lin = tf.linspace(5., 12., 8)
reshape = tf.reshape(lin, [2,4])
squeeze = tf.squeeze(reshape)
reverse = tf.reverse(squeeze, [1])
sliced = tf.slice(reverse, [0,2], [2,2])
stack = tf.stack([lin,lin])
unstack = tf.unstack([lin,lin])

with tf.Session() as sess:
    print(sess.run(lin))
    print(sess.run(reshape))
    print(sess.run(squeeze))
    print(sess.run(reverse))
    print(sess.run(sliced))
    print(sess.run(stack))
    print(sess.run(unstack))
