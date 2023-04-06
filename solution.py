import pandas as pd
import numpy as np

from scipy.stats import chi2

chat_id = 654929803 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    s_squared = 1/(n-1) * sum(x**2)
    alpha = 1 - p
    chi_left = chi2.ppf(q=1 - alpha/2, df=2*n-2)
    chi_right = chi2.ppf(q=alpha/2, df=2*n-2)
    return ((2*n-2)*s_squared/(chi_left*6))**.5,\
            ((2*n-2)*s_squared/(chi_right*6))**.5
