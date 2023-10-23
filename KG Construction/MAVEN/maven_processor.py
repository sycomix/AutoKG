import json
import random
with open('datas/maven_valid.jsonl', 'r', encoding='utf-8') as data:
    lines = data.readlines()
valid = []
for line in lines:
    dict = json.loads(line)
    events = dict['events']
    content = dict["content"]
    # each sentence
    for i in range(len(content)):
        ins = {"sentence": content[i]["sentence"], "events": []}
        for eve in events:
            for men in eve["mention"]:
                if i == men["sent_id"]:
                    ins_i = {"Event_type": eve["type"], "trigger_word": men["trigger_word"]}
                    ins["events"].append(ins_i)
                    break
        if len(ins["events"]) != 0:
            valid.append(ins)

all_list_sampled = random.sample(valid,40)

with open('datas/maven_sample.jsonl', 'w', encoding='utf-8') as f:
    for line in all_list_sampled:
        f.write(json.dumps(line))
        f.write("\n")
f.close()