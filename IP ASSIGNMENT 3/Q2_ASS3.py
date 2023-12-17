
f = open("sorted_data.txt", 'r').read()
lines = f.split("\n")
allrecords = []

for line in lines:
    spl = line.split(',')

    if(len(spl) >= 4):
        allrecords.append(spl)


allrecords = allrecords[1:]

allrecords.sort(key=lambda x: x[3])

dic = {}
format_data = "%H:%M:%S"


for record in allrecords:
    name = record[0].strip()
    entexit = record[1].strip()
    gate = int(record[2].strip())
    #time = datetime.strptime(record[3].strip(), format_data).time()
    time = record[3].strip()

    if name not in dic:
        dic[name] = {}
        dic[name]['gate'] = []
        dic[name]['entexit'] = []
        dic[name]['time'] = []

    dic[name]['gate'].append(gate)
    dic[name]['entexit'].append(entexit)
    dic[name]['time'].append(time)


def q1(dic, name, time, write=True):
    if(name not in dic):
        print("Name not found")
        return
    record = []
    format_data = "%H:%M:%S"
    #time = datetime.strptime(time.strip(), format_data).time()
    time = time.strip()

    entered = False
    exittime = None
    gateexit = -1
    for i in range(len(dic[name]['gate'])):
        gate = dic[name]['gate'][i]
        time = dic[name]['time'][i]
        entexit = dic[name]['entexit'][i]

        if(entexit == "ENTER" and not entered):
            entered = True
            if(gateexit != -1):
                record.append((gateexit, "EXIT", exittime))
                exittime = None
                gateexit = -1
            record.append((gate, entexit, time))
        elif(entexit == "EXIT"):
            entered = False
            exittime = time
            gateexit = gate
    if(gateexit != -1):
        record.append((gateexit, "EXIT", exittime))
        exittime = None
        entered = False
        gateexit = -1
    if(write):
        w = open(f"output_{name}_q1.txt", "w+")
        w.write(str(record))
        w.close()

    oncampus = False
    for i in range(len(record)-1):
        if(record[i][2] <= time < record[i+1][2]):

            if(record[i][1] == "ENTER"):
                oncampus = True
                break
            elif(record[i][1] == "EXIT"):
                oncampus = False
                break
        elif(record[i+1][2] == "ENTRY"):

            oncampus = True
    if(record[len(record)-1][2] <= time):
        if(record[len(record)-1][1] == "ENTER"):
            oncampus = True

        elif(record[len(record)-1][1] == "EXIT"):
            oncampus = False

    if(write):
        print(
            f"{name} is on campus" if oncampus else f"{name} is not present on campus")
    return record


def q2(dic, start, end):

    format_data = "%H:%M:%S"
    #start = datetime.strptime(start.strip(), format_data).time()
    #end = datetime.strptime(end.strip(), format_data).time()
    start = start.strip()
    end = end.strip()

    student_enter = set()
    student_exit = set()
    w = open("output_q2.txt", "w+")
    for key in dic:
        getrecords = q1(dic, key, "23:00:00", False)
        for record in getrecords:
            if(start <= record[2] <= end):
                w.write(
                    f"{key}, {record[1]}, {record[0]}, {record[2]}\n")
                if(record[1] == "ENTER"):

                    student_enter.add(key)
                elif(record[1] == "EXIT"):
                    student_exit.add(key)
    print(f"Students who entered: {list(student_enter)}")
    print(f"Students who exited: {list(student_exit)}")


def q3(dic, gate):
    enter = 0
    exit = 0
    for key in dic:
        getrecords = q1(dic, key, "23:00:00", False)
        for record in getrecords:
            if(record[0] == gate and record[1] == "ENTER"):
                enter += 1
            elif(record[0] == gate and record[1] == "EXIT"):
                exit += 1
    print(
        f"The number of times students used the gate {gate} for entering : {enter}")

    print(
        f"The number of times students used the gate {gate} for exiting : {exit}")


while True:
    print("1. Query 1")

    print("2. Query 2")

    print("3. Query 3")
    inp = input("Enter Choice: ")
    if(inp == ""):
        break
    choice = int(inp)

    if(choice == 1):
        name = input("Enter Name: ")
        time = input("Enter time in HH::MM::SS format (24 hour clock): ")
        q1(dic, name, time)
    elif(choice == 2):
        start = input(
            "Enter Start time in HH::MM::SS format (24 hour clock): ")
        end = input("Enter End time in HH::MM::SS format (24 hour clock): ")
        q2(dic, start, end)
    elif(choice == 3):
        q3(dic, int(input("Enter Gate number: ")))
