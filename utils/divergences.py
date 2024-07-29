import math
from typing import Dict


def kl_divergence(p: Dict[str, float], q: Dict[str, float]) -> float:
    """
    Compute the Kullback-Leibler divergence between two discrete probability distributions.
    
    :param p: Dict representing the first probability distribution
    :param q: Dict representing the second probability distribution
    :return: The KL divergence value
    """
    kl_div = 0.0
    alpha = 0.001
    
    p_hat : Dict[str, float] = {}
    q_hat : Dict[str, float] = {}
    
    # print(p)
    
    # print('--------')
    
    # print(q)

    for key in set(p.keys()) | set(q.keys()):        
        p_hat[key] = (1 - alpha) * p.get(key, 0) + alpha * q.get(key, 0)
        q_hat[key] = (1 - alpha) * q.get(key, 0) + alpha * p.get(key, 0)
            
    
    # Compute KL divergence for keys present in both distributions
    for key in p_hat:
        if p_hat[key] == 0 or q_hat[key] == 0: continue
        kl_div += p_hat[key] * math.log(p_hat[key] / q_hat[key], 2)
    
    return kl_div


def js_divergence(p: Dict[str, float], q: Dict[str, float]) -> float:
    
    # Create the average distribution m
    m = {}
    for key in set(p.keys()) | set(q.keys()):
        m[key] = (p.get(key, 0) + q.get(key, 0)) / 2

    # Compute JSD using KL divergence
    jsd = 0.5 * kl_divergence(p, m) + 0.5 * kl_divergence(q, m)
    
    return jsd

def js_metric(p: Dict[str, float], q: Dict[str, float]) -> float:
    return math.pow(js_divergence(p, q), 0.5)
