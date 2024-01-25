from datetime import datetime
from utils.json_read import load_data


def get_executed_transactions():
	"""Создает и сортирует список словарей"""
	data = load_data()
	items = [item for item in data if item.get('state') == "EXECUTED"]
	items.sort(key=lambda x: x.get('date'), reverse=True)
	return items


def leave_five_transactions(items):
	"""Оставляет в списке 5 транзакций"""
	transactions = items[:5]
	return transactions


def get_result(items):
	"""Выводит результат."""
	for i in items:
		old_format = '%Y-%m-%d'
		new_format = '%d-%m-%Y'
		bad_transactions_date = i['date'].split('T')
		transactions_date = bad_transactions_date[0]
		date = datetime.strptime(transactions_date, old_format)
		result = date.strftime(new_format)
		print(f'{result} {i["description"]}')
		if i["description"] != "Открытие вклада":
			if 'Maestro' in i['from']:
				print(i["from"][:7], i["from"][-16:-12], i["from"][-12:-10] + '** ****', i["from"][-4:], end='')
			elif 'MasterCard' in i['from']:
				print(i["from"][:10], i["from"][-16:-12], i["from"][-12:-10] + '** ****', i["from"][-4:], end='')
			elif 'Счет' in i['from']:
				print(i["from"][:4], i["from"][-16:-12], i["from"][-12:-10] + '** ****', i["from"][-4:], end='')
			elif 'Visa Classic' in i['from']:
				print(i["from"][:12], i["from"][-16:-12], i["from"][-12:-10] + '** ****', i["from"][-4:], end='')
			elif 'Visa Gold' in i['from']:
				print(i["from"][:10], i["from"][-16:-12], i["from"][-12:-10] + '** ****', i["from"][-4:], end='')
			elif 'Visa Platinum' in i['from']:
				print(i["from"][:14], i["from"][-16:-12], i["from"][-12:-10] + '** ****', i["from"][-4:], end='')
		print(f' -> {i["to"][:5]}**{i["to"][-4:]}\n{i['operationAmount']['amount']} руб.')
		print()
