import csv

with open ('scrubbed.csv', newline='') as f:
	reader = csv.reader(f)

	header = reader.__next__()
	# print (header)

	d = {}

	for row in reader:
		if row[4] == '':
			pass
		elif row[4] not in d:
			d[row[4]] = 1
		else:
			temp = d[row[4]]
			temp += 1
			d[row[4]] = temp

	sorted_tuples = (sorted(d.items(), key=lambda x:x[1]))
	# print (sorted(d.items(), key=lambda x:x[1]))

	sightings = 0

	for key, value in d.items():
		sightings += value

	print ('total sightings: {}'. format(sightings))

	_list = []

	for tup in sorted_tuples:
		_list.append([tup[0], tup[1]])

	print (_list)

	with open ('craft_frequency.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow (['craft_type', 'count'])
		writer.writerows(_list)
