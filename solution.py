import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 931254925 # Ваш chat ID, не меняйте название переменной

def solution(...) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
     _, p_value = ttest_ind(x, y, permutations=5000, alternative='greater')
    alpha = 0.1
    return p_value < alpha
