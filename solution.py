import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 931254925 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_value = permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis), 
                 vectorized=True, 
                 n_resamples=5000,
                 alternative='greater').pvalue
    alpha = 0.1
    return p_value < alpha
