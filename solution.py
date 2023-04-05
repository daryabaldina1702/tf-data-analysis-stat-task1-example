import pandas as pd
import numpy as np
from scipy.stats import lognorm


chat_id = 834411281 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Оцениваем параметры распределения
    params = lognorm.fit(x, floc=435)
    # Извлекаем параметр a
    a = np.log(params[2])
    return a # Ваш ответ
