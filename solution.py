import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 931254925 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
     _, p_value = ttest_ind(x, y, permutations=5000, equal_var=False, alternative='less')
    alpha = 0.1
    return p_value < alpha
