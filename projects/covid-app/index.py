# pylint: disable=no-value-for-parameter
import numpy as np
import pandas as pd
import streamlit as st
from data_process import load_data
import time

'''
# Covid 19 Stats Colombia
### casos covid 19
'''

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'
