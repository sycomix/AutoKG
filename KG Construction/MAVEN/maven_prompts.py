import json

with open('datas/maven_valid.jsonl', 'r', encoding='utf-8') as type_data:
    type_lines =  type_data.readlines()
all_event = []
for li in type_lines:
    dict = json.loads(li)
    events = dict['events']
    all_event.extend(eve["type"] for eve in events)
all_event_set = set(all_event)
all_event = list(all_event_set)

with open('datas/maven_sample.jsonl', 'r', encoding='utf-8') as data:
    lines = data.readlines()
num = 1
with open('prompts/maven-1-shot-prompt.txt', 'w',encoding='utf-8') as f:
    for line in lines:
        ans_list = []
        dict = json.loads(line)
        content = dict['sentence']
        events = dict['events']
        event_list = [i["Event_type"] for i in events]
        f.write(str(num))
        num=num+1
        f.write("\n")

        # 0-shot
        prompt = (
            f"The list of event types: {all_event}"
            + "\nGive a sentence: "
            + content
            + "\nWhat types of events are included in this sentence? Please return the most likely answer according to the list of event types above. Require the answer in the form: Event type"
        )

        # 1-shot
        prompt = (
            f"The list of event types: {all_event}"
            + "\nWhat types of events are included in the following sentence? Please return the most likely answer according to the list of event types above. Require the answer in the form: Event type"
            + "\nExample: "
            + "\nGive a sentence: Unprepared for the attack, the Swedish attempted to save their ships by cutting their anchor ropes and to flee."
            + "\nEvent type: "
            + "Removing, Rescuing, Escaping, Attack, Self_motion "
            + "\n\nGive a sentence: "
            + content
            + "\nEvent type: "
            + "\n"
        )

        f.write(prompt)
        f.write("\n\nMAVEN:\n")
        for i in events:
            f.write(str(i)+"\n")
        f.write("\n\n")
f.close()