import tensorflow as tf
from tensorflow import keras
import dask

# Import dataset from parquet using tensorflow dataset object
# Read in the jsonlines file from /home/timothy_holdsworth/Downloads/pubmed_noncommercial_10.jsonl
# The jsonlines file contains the abstracts of 10,000 PubMed articles
data_file = "/home/timothy_holdsworth/Downloads/pubmed_noncommercial_10.jsonl"
# jsonl_file = open(data_file, 'r')

# # Decode the JSONL file into a list of Python dictionaries
# data = keras.json_utils.decode_jsonlines(jsonl_file)

# # Close the JSONL file
# jsonl_file.close()
# import pdb; pdb.set_trace()


with open(data_file, "r") as f:
  lines = f.readlines()

import pdb; pdb.set_trace()
dataset = tf.data.Dataset.from_json_lines(lines)