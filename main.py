#!/usr/bin/env python3

"""
This is a file for make a test
with python.
"""

from json import load, dumps 
from json.decoder import JSONDecodeError
from textwrap import indent
from rich.panel import Panel
from rich.console import Console
# from sys import getsizeof


def get_numbers():
	"""
	Return the list of numbers to use.
	"""

	numbers_list = CONFIG['numbers']
	return numbers_list



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

	to_divide = CONFIG['divisor']
	for number in get_numbers():
		try:
			divided = number / to_divide
			# getting the number object and adding
			object = get_object_number(number, divided, to_divide)

			numbers_divided.append(object)
			del number # not use more

		# errors catched
		except ValueError:
			console.print('[red bold]The number to divide the numbers not is valid. Verify the file config.json[/[')

		except TypeError:
			console.print('[red bold]The number to divide the numbers not is valid. Verify the file config.json[/]')


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

	# getting values to save
	filename = CONFIG['filename']
	numbers_divided = get_numbers_divide()

	try:
		# saving
		save_in_file(filename, numbers_divided)
		panel = Panel(f'[green]:thumbs_up: Saved in "{filename}"[/]', title  = '[bold blue]Save Numbers[/]')
		console.print(panel)
		
	except:
		console.print('[red bold]Some problem to save the file Verify the file of configuration.[/]')



if __name__ == '__main__':
	# getting console for show messages
	console = Console()
	try:
		# loading configuration
		CONFIG = load(open('./config.json'))
		# console to use for show message
		main()

	except JSONDecodeError:
		console.print('[red bold]Some problem with syntax or other for read the file of configuration.[/]')