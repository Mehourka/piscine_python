import sys

def isEven(num):
	return num % 2 == 0

def throw(e):
	print("AssertionError: ", e)
	exit(1)


def main():
	args = sys.argv

	if len(args) <= 1:
		exit(0)

	if len(args) > 2:
		throw("more than one argument is provided")

	try:
		number = int(args[1])
	except ValueError:
		throw("argument is not an integer")


	if isEven(number):
		print("I'm Even.")
	else:
		print("I'm Odd.")


if __name__ == "__main__":
	main()