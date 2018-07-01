################################################################################
# A script that plays around with creating differen tensors
################################################################################

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

# Creating range tensors
lin = tf.linspace(5., 9., 5)
rang = tf.range(3., 7., delta=0.5)
neg_rang = tf.range(7., 3., delta=-0.5)

# Creating tensors with the same values
zero_tens = tf.zeros([3,3])
one_tens = tf.ones([4,4])
fill_tens = tf.fill([2,3], 15)

# Creating tensors with random values
random_normal = tf.random_normal([5,2], mean=5.0, stddev=1)
trunc_random = tf.truncated_normal([5,2], mean=5.0, stddev=1)
unif_random  = tf.random_uniform([5,2], minval=0, maxval=5)
shuffle = tf.random_shuffle(unif_random)

with tf.Session() as sess:
    print(sess.run(lin))
    print(sess.run(rang))
    print(sess.run(neg_rang))
    print(sess.run(zero_tens))
    print(sess.run(one_tens))
    print(sess.run(fill_tens))
    print(sess.run(random_normal))
    print(sess.run(trunc_random))
    print(sess.run(unif_random))
    print(sess.run(shuffle))
