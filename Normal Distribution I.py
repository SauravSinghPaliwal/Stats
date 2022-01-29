import numpy as np
from scipy import stats
import scipy

scipy.stats.norm(20, 2).cdf(19.5)

scipy.stats.norm(20, 2).cdf(22) - scipy.stats.norm(20, 2).cdf(20)
