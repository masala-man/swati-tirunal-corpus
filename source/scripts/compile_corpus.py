import os
import csv
import copy
import json
output_file = "./corpus.json"

template = {
	"meta": {
		"name": "",
		"type": "",
		"language": "",
		"ragam": "",
		"talam": ""
	},
	"sahityam": {
		"pallavi": [],
		"anupallavi": [],
		"charanam": []
	}
}

corpus = []

sahi_fields = ["PALLAVI", "ANUPALLAVI", "CHARANAM"]
meta_fields = ["RAGAM", "TALAM", "TYPE", "LANGUAGE"]
meta_index = []

for metafield in meta_fields:
	with open(f"../meta/{metafield.lower()}.csv") as f:
		metacorp = {}
		red = csv.reader(f)
		for n,row in enumerate(red):
			metacorp[n] = row[1]
		meta_index.append(metacorp)

with open('../meta/index.csv', 'r') as indf:
	index_reader = csv.reader(indf)
	for composition in index_reader:
		current_template = copy.deepcopy(template)
		if os.path.exists(f'../texts/{composition[0]}.txt'):
			current_template['meta']['name'] = composition[1]
			for n, metafield in enumerate(meta_fields):
				current_template['meta'][metafield.lower()] = meta_index[n][int(composition[n+2])]

			with open(f'../texts/{composition[0]}.txt', 'r') as textfile:
				text = textfile.read()
			for token in text.split("$"):
				for item in ([f"{x}\n" for x in sahi_fields]):
					if token[:len(item)] == item:
						token = token[len(item):]
						lines = token.split("\n")
						lines = list(filter(None, lines))
						for sahi_field in sahi_fields:
							if item == f"{sahi_field}\n":
								current_template['sahityam'][sahi_field.lower()].append(lines)
						#scrape translation
			corpus.append(current_template)

with open('../../dataset/corpus.json', 'w') as corpus_file:
    corpus_file.write(json.dumps(corpus,ensure_ascii=False))
