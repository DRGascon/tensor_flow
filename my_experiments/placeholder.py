################################################################################
# A script that plays around with placholders in tensorflow
################################################################################

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

ph = tf.placeholder(tf.float32)
data_src = np.array([9., 8., 7.])
increment = tf.add(ph, 1.)

with tf.Session() as sess:
    res = sess.run(increment, feed_dict={ph: data_src})
    print(res)
