import yaml

with open('kimchi.yml') as f: r = yaml.safe_load(f)

print('Ingredients:')
for i in r['ingredients']:
    print('\t' + i)

print('Steps:')
for s in r['steps']:
    print(f'\t{s} - {r["steps"][s]}')