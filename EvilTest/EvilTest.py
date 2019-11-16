#! /usr/bin/env python

import tensorflow as tf
import numpy as np
import os
import time
import datetime
from EvilTest import data_helpers
#from text_cnn import TextCNN
from tensorflow.contrib import learn
import csv
import sys
from konlpy.tag import Kkma 

class EvilTest:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


def test(keyword):
    # Parameters
    # ==================================================

    #tf.flags.DEFINE_string("checkpoint_dir", "./EvilTest/runs/1573754967/checkpoints/", "Data source for the positive data.")
    
    # Data Parameters
    tf.flags.DEFINE_string("positive_data_file", "./EvilTest/data/rt-polaritydata/rt-polarity.pos", "Data source for the positive data.")
    tf.flags.DEFINE_string("negative_data_file", "./EvilTest/data/rt-polaritydata/rt-polarity.neg", "Data source for the negative data.")

    # Eval Parameters
    tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
    tf.flags.DEFINE_string("checkpoint_dir", "./EvilTest/runs/1573754967/checkpoints/", "Checkpoint directory from training run")
    tf.flags.DEFINE_boolean("eval_train", False, "Evaluate on all training data")

    # Misc Parameters
    tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
    tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")
    FLAGS = tf.flags.FLAGS
    print("\nParameters:")
    for attr, value in sorted(FLAGS.__flags.items()):
        print("{}={}".format(attr.upper(), value))
    print("")

    #x_raw, y_test = data_helpers.load_data_and_labels(FLAGS.positive_data_file, FLAGS.negative_data_file)
    #print(x_raw)
    #print(y_test)
    x_raw = [keyword]
    y = [[1,0]]
    y_test = np.concatenate([y], 0)
    print(y_test)
    y_test = np.argmax(y_test, axis=1)

    kkma=Kkma() 
    x_raw=[" ".join(kkma.morphs(x2)) for x2 in x_raw]


    # Map data into vocabulary
    vocab_path = os.path.join(FLAGS.checkpoint_dir, "..", "vocab")
    vocab_processor = learn.preprocessing.VocabularyProcessor.restore(vocab_path)
    x_test = np.array(list(vocab_processor.transform(x_raw)))

    print("\nEvaluating...\n")

    # Evaluation
    # ==================================================
    checkpoint_file = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
    graph = tf.Graph()



    with graph.as_default():
        session_conf = tf.ConfigProto(
        allow_soft_placement=FLAGS.allow_soft_placement,
        log_device_placement=FLAGS.log_device_placement)
        sess = tf.Session(config=session_conf)
        with sess.as_default():
            # Load the saved meta graph and restore variables
            saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_file))
            saver.restore(sess, checkpoint_file)

            # Get the placeholders from the graph by name
            input_x = graph.get_operation_by_name("input_x").outputs[0]
            # input_y = graph.get_operation_by_name("input_y").outputs[0]
            dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]

            # Tensors we want to evaluate
            predictions = graph.get_operation_by_name("output/predictions").outputs[0]

            # Generate batches for one epoch
            batches = data_helpers.batch_iter(list(x_test), FLAGS.batch_size, 1, shuffle=False)

            # Collect the predictions here
            all_predictions = []

            for x_test_batch in batches:
                batch_predictions = sess.run(predictions, {input_x: x_test_batch, dropout_keep_prob: 1.0})
                print(batch_predictions)
                all_predictions = np.concatenate([all_predictions, batch_predictions])



    return "text"

