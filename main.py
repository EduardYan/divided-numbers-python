#!/usr/bin/env python3

"""
This is a file for make a test
with python.
"""

from json import load, dumps
from textwrap import indent
from rich.panel import Panel
from rich.console import Console
# from sys import getsizeof


def get_numbers(type:str='normal'):
	"""
	Return a tuple
	withe two numberic values to use.

	Recive the type of numbers
	to return.

	"""

	type_numbers_availables = [
		'normal',
		'float',
	]

	# validating the type
	if type not in type_numbers_availables:
		raise TypeError(f'The type for return the number not is valid. Valid values {type_numbers_availables}')

	if type == type_numbers_availables[0]:
		n1 = 6
		n2 = 2

	if type == type_numbers_availables[1]:
		n1 = float(6)
		n2 = float(2)

	return n1, n2


def get_numbers_iter():
	"""
	Return a iterator with numbers.
	"""

	yield 5
	yield 2
	yield 3
	yield 12
	yield 200
	yield 25
	yield 30



def get_object_number(normal_number:int, divided:float, divisor:float) -> dict:
	"""
	Return the object
	with the keys 'normal_number' and 'divided' from
	parameters passed for parameter.
	"""


	return {
		'normal_number': normal_number,
		'divisor': divisor,
		'divided': divided
	}



def get_numbers_divide() -> list:
	"""
	Return a list
	with the values divide of the numbers.
	"""

	# to save the numbers divided objects
	numbers_divided = []

	to_divide = load(open('config.json'))['toDivide']
	for number in get_numbers_iter():
		try:
			divided = number / to_divide
			# getting the number object and adding
			object = get_object_number(number, divided, to_divide)

			numbers_divided.append(object)
			del number

		# errors catched
		except ValueError:
			print('The number to divide the numbers not is valid. Verify the file config.py')

		except TypeError:
			print('The number to divide the numbers not is valid. Verify the file config.py')


	return numbers_divided


def save_in_file(filename:str, list_numbers_objects:list) -> None:
	"""
	Save the list of numbers passed for parameter
	in a file with the filename passed for paraemeter.
	"""

	with open(filename, 'w') as f:
		# formating for save
		to_save = str(dumps({'numbers': list_numbers_objects}, indent=2))
		f.write(to_save)
		f.close()


def main():
	"""
	Principal function to execute.
	"""

	filename = load(open('config.json'))['filename']
	numbers_divided = get_numbers_divide()

	try:
		# saving
		save_in_file(filename, numbers_divided)
		console = Console()
		panel = Panel(f'[green]:thumbs_up: Saved in "{filename}"[/]', title  = '[bold blue]Save Numbers[/]')
		console.print(panel)
		
	except:
		print('Some problem to save the file.')


if __name__ == '__main__':
	main()
