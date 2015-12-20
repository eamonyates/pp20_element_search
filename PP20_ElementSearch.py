import random, math


random_list = random.sample(range(1000), 100)


def element_search(list=random_list):

	ordered_list = sorted(random_list)
	user_number = int(input("Enter a number you would like to search for in the list: "))

	while len(ordered_list) != 1:

		ordered_list_midpoint = int(math.ceil(len(ordered_list) / 2))

		if ordered_list[ordered_list_midpoint] < user_number:
			ordered_list = ordered_list[ordered_list_midpoint:]
		elif ordered_list[ordered_list_midpoint] > user_number:
			ordered_list = ordered_list[:ordered_list_midpoint]
		else:
			print (str(user_number) + " is in the list")
			break

	else:

		if ordered_list[0] == user_number:
			print (str(user_number) + " is in the list")
		else:
			print (str(user_number) + " is not in this list")


if __name__ == "__main__":
	element_search()
