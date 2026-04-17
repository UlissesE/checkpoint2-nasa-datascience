import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("KC1.csv")

print(df.shape)
print(df.head(10))

LOC_TOTAL = df["LOC_TOTAL"]

print(
    """
================
 BASE LOC TOTAL
================
      """)
print(LOC_TOTAL.head(10))

print(
    """
====================
 MEDIA POPULACIONAL  
====================
""")

media_populacioal = LOC_TOTAL.mean()

print(f"Media: {media_populacioal}")
