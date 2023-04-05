import pandas as pd
import numpy as np

from scipy.stats import chi2

chat_id = 654929803 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    s = np.std(x, ddof=1)
    chi_left = chi2.ppf((1+p)/2,n-1)
    chi_right = chi2.ppf((1-p)/2, n-1)
    return s*((n-1)/(chi_left*6))**.5,\
            s*((n-1)/(chi_right*6))**.5
