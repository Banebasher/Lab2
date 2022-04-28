def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    ave_temp = calc_average_temperature(num_list)
    max_min_list = calc_min_max_temperature(num_list)
    median_temp = calc_median_temperature(num_list)
    print(num_list)
    print(ave_temp)
    print(max_min_list)
    print(median_temp)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g.5,67,32)")

def get_user_input():
    numbers = input()
    numbers = numbers.split(",")
    numbers = [float(i) for i in numbers]
    return numbers
def calc_average_temperature(numbers):

    count = 0
    total = 0
    for i in numbers:
         count = count + 1
    for i in numbers:
        total = total + i
    average_temp = total/count
    return average_temp
def calc_median_temperature(numbers):
    numbers.sort()
    count = 0
    for i in numbers:
        count = count + 1
    index = (count-1)//2
    if (count%2):
        return numbers[index]
    else:
        return (numbers[index]+ numbers[index + 1])/2.0
def calc_min_max_temperature(numbers):
    max = 0

    for i in numbers:
        if i > max:
            max = i
    min = max
    for i in numbers:

      if i < min:
        min = i
    maxminlist = [max, min]
    return maxminlist







if __name__ == "__main__":
    main()
