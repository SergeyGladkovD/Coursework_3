import json


def load_data():
	"""Читает json файл."""
	with open('../data/operations.json', 'r', encoding='utf-8') as read_file:
		data = json.load(read_file)
		return data
