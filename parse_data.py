import csv

with open ('data/scrubbed.csv', newline='') as f:
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

	for row in reader:
		print (row)

	sorted_tuples = (sorted(d.items(), key=lambda x:x[1]))
	# print (sorted(d.items(), key=lambda x:x[1]))

	sightings = 0

	for key, value in d.items():
		sightings += value

	print ('total sightings: {}'. format(sightings))

	craft_frequency = []

	for tup in sorted_tuples:
		craft_frequency.append([tup[0], tup[1]])

	print (craft_frequency)

	with open ('data/craft_frequency.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow (['craft_type', 'count'])
		writer.writerows(craft_frequency)

with open ('data/scrubbed.csv', newline='') as f:
	reader = csv.reader(f)

	header = reader.__next__()
	# print (header)

	d = {}

	for row in reader:
		if row[3] == '':
			pass
		elif row[3] not in d:
			d[row[3]] = 1
		else:
			temp = d[row[3]]
			temp += 1
			d[row[3]] = temp

	for row in reader:
		print (row)

	sorted_tuples = (sorted(d.items(), key=lambda x:x[1]))
	# print (sorted(d.items(), key=lambda x:x[1]))

	country_frequency = []

	for tup in sorted_tuples:
		country_frequency.append([tup[0], tup[1]])

	print (country_frequency)

	with open ('data/country_frequency.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow (['country', 'count'])
		writer.writerows(country_frequency)