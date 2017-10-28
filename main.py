#!/usr/bin/env python3

from __future__ import absolute_import, division, print_function

import os
import pickle
from six.moves import urllib

import tflearn
from tflearn.data_utils import *

# start of part 4 -----------------------


path = 'shakespeare_input.txt'
char_idx_file = 'char_idx.pickle'

max_len = 25

char_idx = None
if os.path.isfile(char_idx_file):
    print('Loading previous char_idx')
    char_idx = pickle.load(open(char_idx_file, 'rb'))

X, Y, char_idx = textfile_to_semi_redundant_sequences(
    path,
    seq_maxlen=max_len,
    redun_step=3,
    pre_defined_char_idx=char_idx,
)
pickle.dump(char_idx, open(char_idx_file, 'wb'))

# start of part 5-------------------------

g = tflearn.input_data([None, max_len, len(char_idx)])
g = tflearn.lstm(g, 128, return_seq=True)
g = tflearn.dropout(g, 0.5)
g = tflearn.lstm(g, 128, return_seq=True)
g = tflearn.dropout(g, 0.5)
g = tflearn.lstm(g, 128)
g = tflearn.dropout(g, 0.5)
g = tflearn.fully_connected(g, len(char_idx),
                            activation='softmax')
g = tflearn.regression(g, optimizer='adam',
                       loss='categorical_crossentropy',
                       learning_rate=0.001)

m = tflearn.SequenceGenerator(g, dictionary=char_idx,
                              seq_maxlen=max_len,
                              clip_gradients=5.0,
                              checkpoint_path='model_shakespeare')

for i in range(1):
    seed = random_sequence_from_textfile(path, max_len)
    m.fit(X,
          Y,
          validation_set=0.1,
          batch_size=128,
          n_epoch=1,
          run_id='shakespeare')
    print('-- TESTING')
    print('-- Test with temperature of 1.0 --')
    print(m.generate(600, temperature=1.0, seq_seed=seed))
    print('-- Test with temperature of 0.5 --')
    print(m.generate(600, temperature=0.5, seq_seed=seed))
