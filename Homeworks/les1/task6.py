run_start = int(input("Сколько вы пробегаете километров в день ?"))
run_finish = int(input("Сколько вы хотите пробегать километров в день ?"))
days = 1

while run_start < run_finish:
    run_start = run_start + (run_start * 0.1)
    days += 1
else:
    print("На " + str(days) + " день вы достигните результата — не менее " + str(run_finish) + " км.")
