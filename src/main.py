from scripts.get_data import get_executed_transactions, leave_five_transactions, get_result


def main():
	items = get_executed_transactions()
	transactions = leave_five_transactions(items)
	get_result(transactions)


if __name__ == '__main__':
	main()
