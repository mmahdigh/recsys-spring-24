import json
import math
import random

from divergences import kl_divergence, js_divergence, js_metric
from rank_aware import calculate_relative_weight
import statistics


behaviors = []
news = []

with open('behaviors.json') as f:
   behaviors = json.load(f)
   

with open('news.json') as f:
   news = json.load(f)
   
   
def convert_to_probabilities(data):
  total_count = max(sum(data.values()), 1)
  probabilities = {key: value / total_count for key, value in data.items()}
  return probabilities



def find_news_item(id):
    try:
      return next(item for item in news if item.get('news_id') == id)
    except StopIteration:
      print("Couldn't find this id:", id)
      return None
  
def initialize_topic_dist():
  topics = {}
  
  for item in news:
    if item['topic'] not in topics:
      topics[item['topic']] = 0
  
  return topics
      
  

def get_user_impressions(uid):
  impressions = [obj for obj in behaviors if obj["uid"] == uid]
  return impressions


def get_user_topic_distribution(uid):
  impressions = get_user_impressions(uid)
  
  all_history_news = []
  
  for impression in impressions:
    length = len(impression['hist_strings'])
    rank_aware = [{"nid": value, "weight": calculate_relative_weight(index)} for index, value in enumerate(impression['hist_strings'])]
    all_history_news.extend(rank_aware)
    
  history_distribution = initialize_topic_dist()
  
  # print("uid", uid, all_history_news)
  # print("***********")
  
  for item in all_history_news:
    if (item['nid'] == ''): continue
    metadata = find_news_item(item['nid'])
    history_distribution[metadata['topic']] = history_distribution[metadata['topic']] + item['weight']
    
    
  # ----------------
  
  all_recom_news = []
  
  for impression in impressions:
    length = len(impression['recoms_strings'])
    rank_aware = [{"nid": value[:-2], "weight": calculate_relative_weight(index)} for index, value in enumerate(impression['recoms_strings'])]
    all_recom_news.extend(rank_aware)
    
  # all_recom_news = [recom[:-2] for recom in all_recom_news]
      
  recom_distribution = initialize_topic_dist()
  
  for item in all_recom_news:
    metadata = find_news_item(item['nid'])
    recom_distribution[metadata['topic']] = recom_distribution[metadata['topic']] + item['weight']
  
    
  
    
  return (convert_to_probabilities(history_distribution), convert_to_probabilities(recom_distribution))

def get_user_sample(users, percent):
  result = []
  for user in users:
    if (random.random() * 100 < percent):
      result.append(user)
      
  return result; 
    
    
def aggregate_all_users():
  users_set = set()
  for item in behaviors:
    users_set.add(item['uid'])
    
  # users = list(users_set)
  
  sample = get_user_sample(users_set, 0.1)
  
  print("# of users:", len(users_set))  
  print("chosen ones:", len(sample))  
    
  count = 0
  js_metrics = []
  for uid in sample:
    print("Progress", round(count / len(sample) * 100, 2), "%")
    dist1, dist2 = get_user_topic_distribution(uid)
    val = js_metric(dist1, dist2)
    js_metrics.append(val)
    count = count + 1
    
  return(statistics.mean(js_metrics))
    

    
    
print(aggregate_all_users())

  

  