import pandas as pd
import numpy as np
import matplotlib as plt
import json
import os
import sys
from pprint import pprint

table = pd.read_table('DJTTweets2017-06-17+00 - Copy.json')

print table.head()

#for line in table.Hashtags:
    #print line