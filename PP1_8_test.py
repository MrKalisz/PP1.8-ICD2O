import os.path
import sys
import PP1_8

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	PP1_8.q1()
	captured = capsys.readouterr()
	assert captured.out == "False\nTrue\n"

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q2()
	captured = capsys.readouterr()
	assert captured.out == "Enter an integer: False\n"

def test_q3_1(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['15']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q3()
	captured = capsys.readouterr()
	assert captured.out == "Enter a number: False\n"

def test_q4_1(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['pizza', 'pop']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input food: Input drink: False\n"

def test_q5_1(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['3']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q5()
	captured = capsys.readouterr()
	assert captured.out == "Enter an integer: The integer 3 is False\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	PP1_8.q1()
	captured = capsys.readouterr()
	assert captured.out == "False\nTrue\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['1']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q2()
	captured = capsys.readouterr()
	assert captured.out == "Enter an integer: True\n"

def test_q3_2(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q3()
	captured = capsys.readouterr()
	assert captured.out == "Enter a number: True\n"

def test_q4_2(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['pop', 'pop']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input food: Input drink: True\n"

def test_q5_2(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-3']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q5()
	captured = capsys.readouterr()
	assert captured.out == "Enter an integer: The integer -3 is False\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	PP1_8.q1()
	captured = capsys.readouterr()
	assert captured.out == "False\nTrue\n"

def test_q2_3(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q2()
	captured = capsys.readouterr()
	assert captured.out == "Enter an integer: True\n"

def test_q3_3(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['5.5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q3()
	captured = capsys.readouterr()
	assert captured.out == "Enter a number: True\n"

def test_q4_3(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['burger', 'fries']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input food: Input drink: True\n"

def test_q5_3(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['6']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q5()
	captured = capsys.readouterr()
	assert captured.out == "Enter an integer: The integer 6 is True\n"

def test_q1_4(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	PP1_8.q1()
	captured = capsys.readouterr()
	assert captured.out == "False\nTrue\n"

def test_q2_4(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['99']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q2()
	captured = capsys.readouterr()
	assert captured.out == "Enter an integer: True\n"

def test_q3_4(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['10']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q3()
	captured = capsys.readouterr()
	assert captured.out == "Enter a number: True\n"

def test_q4_4(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['pop', 'pizza']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input food: Input drink: True\n"

def test_q5_4(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q5()
	captured = capsys.readouterr()
	assert captured.out == "Enter an integer: The integer 0 is True\n"

def test_q1_5(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	PP1_8.q1()
	captured = capsys.readouterr()
	assert captured.out == "False\nTrue\n"

def test_q2_5(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-1']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q2()
	captured = capsys.readouterr()
	assert captured.out == "Enter an integer: True\n"

def test_q3_5(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-1']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q3()
	captured = capsys.readouterr()
	assert captured.out == "Enter a number: False\n"

def test_q4_5(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['pizza', 'pizza']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input food: Input drink: True\n"

def test_q5_5(capsys):

	try:
		exists = os.path.exists("PP1_8.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-2']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_8.input = mock_input

	PP1_8.q5()
	captured = capsys.readouterr()
	assert captured.out == "Enter an integer: The integer -2 is True\n"

