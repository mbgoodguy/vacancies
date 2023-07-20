import csv
import json

DATA_ADS = 'data/ads.csv'
JSON_ADS = 'ads/ads.json'
DATA_CAT = 'data/categories.csv'
JSON_CAT = 'ads/categories.json'


def convert_from_csv_to_json(csvfilename, model_name, jsonFilename, is_published_column=None):
    result = []
    with open(csvfilename, encoding='utf-8') as csv_f:

        for row in csv.DictReader(csv_f):
            to_add = {'model': model_name, 'pk': int(row['Id'] if 'Id' in row else row['id'])}
            if 'Id' in row:
                del row['Id']
            else:
                del row['id']

            if is_published_column and is_published_column in row:
                if row[is_published_column] == 'TRUE':
                    row[is_published_column] = True
                else:
                    row[is_published_column] = False

            if 'price' in row:
                row['price'] = int(row['price'])
            to_add['fields'] = row
            result.append(to_add)

    with open(jsonFilename, 'w', encoding='utf-8') as jsf:
        jsf.write(json.dumps(result, ensure_ascii=False))


convert_from_csv_to_json(DATA_ADS, 'ads.ad', JSON_ADS, 'is_published')
convert_from_csv_to_json(DATA_CAT, 'ads.category', JSON_CAT)
