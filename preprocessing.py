import argparse
import json
import validators

# first argument is filepath to data file
parser = argparse.ArgumentParser()
parser.add_argument('filepath')
args = parser.parse_args()

# read file
with open(args.filepath, 'r') as f:
    data = json.load(f)

# Note: This is discord data
# process all the sentences

p_data = []
words = []
for msg in data:
    if msg.strip() == "":
            continue
    # if it is a codeblock
    elif msg[0:3] == "```" or msg[-3:] == '```':
        continue
    # if it is a link
    elif validators.url(msg):
            continue
    
    # if its a mention
    if msg[0:2] == "<@":
        continue    

    if len(msg) <= 1:
        continue    

    p_data.append(msg)

    words_ = msg.split(" ")
    words.extend(words_)

print(p_data, words)

# print statistics on p_data
print(f"Data Size {len(p_data)}")

# no. of unique words
print(f"Unique words {len(set(words))}")

# save to file in ./data/processed/ with the same filename as a text file
with open(f"./data/processed/{(args.filepath.split('/')[-1]).split('.')[0]}.txt", 'w') as f:
    f.write("\n".join(p_data))