import random
import json

def parse_tsv_line(line):
    """
    Parses a single line from the TSV file and converts it into the desired JSON object.
    """
    parts = line.strip().split('\t')
    news_id = parts[0]
    category = parts[1]  
    topic = parts[2]  
    title = parts[3]  
    content = parts[4]  
    
    return {"news_id": news_id, "category": category, "topic": topic, "title": title, "content": content}

def convert_tsv_to_json(tsv_file_path):
    """
    Reads a TSV file and converts each line to the desired JSON object.
    """
    json_objects = []  # List to hold all converted objects
    
    with open(tsv_file_path, 'r') as file:
        for line in file:
            json_object = parse_tsv_line(line)
            json_objects.append(json_object)
    
    return json_objects

# Example usage
tsv_file_path = '../mind_st/MINDsmall_train/news.tsv'
json_objects = convert_tsv_to_json(tsv_file_path)

# # Optionally, print or save the JSON objects
# for obj in json_objects:
#     print(json.dumps(obj, indent=4))

with open('news.json', 'w') as file:
  json.dump(json_objects, file)


# print(parse_tsv_line("6	U69606	11/15/2019 1:24:44 PM	N879 N19591 N63054 N53033 N54088 N34140 N14952 N21503 N43142 N37394 N4607	N29862-0 N48740-0 N11390-0 N5472-0 N53572-0 N24802-1 N6400-0 N29091-0 N19611-0 N55237-0 N31958-1"))


