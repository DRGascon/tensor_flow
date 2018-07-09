from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import os

a = tf.constant(2.5, name='first_tensor')
b = tf.constant(5.2, name='second_tensor')  
sum = a + b;

print(tf.get_default_graph().get_operations())
print(tf.get_default_graph().get_tensor_by_name('first_tensor:0'))

tf.train.write_graph(tf.get_default_graph(), os.getcwd(), 'graph.dat')
