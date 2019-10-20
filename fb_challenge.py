import pandas as pd
import numpy as np

f = open("files.txt")
for i in f:
	df = pd.read_csv(str(i).strip())
	df.head()
	break