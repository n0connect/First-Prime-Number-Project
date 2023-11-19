"""
    Finds prime numbers up to the given user_number.

    Parameters:
        user_number (int): The maximum number to check for prime numbers.

    Returns:
        list: A list of prime numbers found up to user_number.
    """
false_input = True
is_first_run = True
process_bar_run = True
part_of_processes: int = 0
prime_number_temp: int = 2
prime_numbers: list = [2]
time_quantitation: float = 499984999 + 0.8
time_result: float


def time_calculation(calculation_number):
    global time_result
    time_result = ((calculation_number - 2) * (calculation_number - 1) - 2) / (4 * time_quantitation)
    if time_result < 0:
        time_result = 0
    return time_result


def find_prime_numbers(user_number, start_number) -> int | str:
    global process_bar_run

    if start_number is None or start_number == 1 or start_number == 0:
        process_bar_run = False
        return 'prime_numbers'

    for number in range(start_number, user_number + 1):
        if number % 2 != 0:
            for modCheck in range(3, int(number * 0.5) + 1, 2):
                if number % modCheck == 0:
                    break
            else:
                prime_numbers.append(number)
                return number


def processes_bar(last_number: int, now_number: int) -> bool | int:
    global is_first_run, part_of_processes
    global process_bar_run
    loading_bar_text = "##"
    if now_number is None:
        process_bar_run = False
        return process_bar_run

    if is_first_run:
        print(f"\rCreating File   0_0 | Estimated Time: {time_calculation(user_selected_number): .2f} sn | {time_calculation(user_selected_number)/60: .1f} dk")
        part_of_processes = int(last_number / 10)
        if part_of_processes < 1:
            part_of_processes = 1

    is_first_run = False

    if 1 <= now_number // part_of_processes:
        part_of_processes *= 1.3062014  # Root of F(x)=r^9 -10r +9 , x1~ -1.30612, x2~ 1.02612, x3~1
        part_of_processes = int(part_of_processes)
        print(f'{loading_bar_text}', end='')
        # print(f'[{loading_bar_text: _^10}] Creating file...')

    if now_number >= last_number:
        process_bar_run = False
        return process_bar_run

    now_number = now_number + 1
    return now_number


while false_input:
    try:
        user_selected_number = int(input(f'Select a number: '))
        if user_selected_number <= 2:
            print('Please, enter a number greater than 2')
        else:
            false_input = False
            # prime_number_temp: int = processes_bar(user_selected_number, prime_number_temp)

    except ValueError as ve:
        print(f'Please, enter an integer, Error is: {ve}')
    except Exception as ex:
        print(f'Exception Error is: {ex}')

if not false_input:
    while process_bar_run:
        prime_number_temp: int = find_prime_numbers(user_selected_number, prime_number_temp)
        prime_number_temp: int = processes_bar(user_selected_number, prime_number_temp)

try:
    with open('prime_numbers_output.txt', 'w') as file:
        for prime in prime_numbers:
            file.write(f'{prime} is prime\n')
        print(f"\nSUCCESSFULLY CREATED FILE\n{len(prime_numbers)} prime numbers are listed.")
except Exception as ex:
    print(f'File operation error: {ex}')
