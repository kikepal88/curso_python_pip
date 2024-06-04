import utils
import charts
import pandas as pd

def run():
  # data = utils.get_data('data.csv')
  # data = list(filter(lambda item : item['Continent'] == 'South America', data))

  # countries = list(map(lambda x: x['Country/Territory'], data))
  # percentages = list(map(lambda x: x['World Population Percentage'], data))
  # charts.generate_pie_chart(countries, percentages)

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = utils.get_data('data.csv')
  country = input('Type country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    labels, values = utils.get_population(result[0])

    charts.generate_bar_chart(country, labels, values)

if __name__ == '__main__':
  run()