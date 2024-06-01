import csv

def get_data(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)

    return data

def get_population(country):
  lab = list(country.keys())
  label = list(filter(lambda label: '0' in label, lab))

  data={}

  for item in label:
    data[item[0:4]] = country[item]
  
  labels = list(data.keys())
  val = list(data.values())
  values = list(map(lambda i: int(i), val))
  return labels, values

def population_by_country(data, country):
  return data
