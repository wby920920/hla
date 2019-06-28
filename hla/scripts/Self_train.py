from __future__ import absolute_import

import argparse

from train import train_2013
from eval import test

# print("="*80)
# print("Train new model on [bdata.20130222.mhci.txt]")
# print("="*80)
# print("\n")
#
# train_2013()
#
# print("="*80)
# print("Finish Training...Model saved as best_model_2013.keras")
# print("="*80)
# print("\n")

#print("=" * 80)
#print("Eval model on [weekly_data_all_rm_duplicate.txt]")
#print("Model to eval: best_model_2013.keras")
#print("=" * 80)
#print("\n")

#test()

#print("=" * 80)
#print("Finish Eval.")
#print("Check results in folder [weekly_result_nonredundant_sep_iedbid].")
#print("=" * 80)
#print("\n")
x = 1
d = {(x, x+1): x }
t = (5,6)
print(type(t))
print(d)