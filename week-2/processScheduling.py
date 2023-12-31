#Given the arrivalTime , burstTime
#write code for FCFS,SJF,PS,RR(tq=4)
#output waiting time and turnaroundtime for each provess 
#average waiting time and average turnaround time 

class process:

     def __init__(self, name,arrivalTime,burstTime,priority):
        self.name = name
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.priority=priority
        self.waitTime = 0 #WT = TAT - BT
        self.turnAroundTime = 0 #TAT = CT - AT

#  self.process_id = process_id
#         self.arrival_time = arrival_time
#         self.burst_time = burst_time
#         self.priority = priority
#         self.waiting_time = 0
#         self.turnaround_time = 0
processes = []
num_processes = int(input("Enter the number of processes: "))

# Getting user input
for i in range(num_processes):
    arrivalTime = int(input(f"Enter arrival time for process {i + 1}: "))
    burstTime = int(input(f"Enter burst time for process {i + 1}: "))
    priority = int(input(f"Enter priority time for process {i + 1}: "))
    processes.append(process(i+1, arrivalTime, burstTime,priority))

# for p in processes:
#     print(f"Process {p.name}:")
#     print(f"  Arrival Time: {p.arrivalTime}")
#     print(f"  Burst Time: {p.burstTime}")
#     print(f"  Wait Time: {p.waitTime}")
#     print(f"  Turnaround Time: {p.turnAroundTime}")
#     print()

#sort processes based on ascending order
def sort_processes_by_arrival_time(processes):
    return sorted(processes, key=lambda x: x.arrivalTime)

def sort_processes_by_burst_time(processes):
    return sorted(processes, key=lambda x: x.burstTime)

def FCFS(processes):
    total_waiting_time_FCFS = 0
    total_turnaround_time_FCFS = 0
    current_time = 0
    for process in processes:
        process.waitTime = current_time - process.arrivalTime
        process.turnAroundTime = process.waitTime + process.burstTime
        current_time += process.burstTime
        total_waiting_time_FCFS += process.waitTime
        total_turnaround_time_FCFS += process.turnAroundTime

    print("total waiting time for FCFS:",total_waiting_time_FCFS)
    print("total turnaround time time for FCFS:",total_turnaround_time_FCFS)
    average_waiting_time = total_waiting_time_FCFS / len(processes)
    average_turnaround_time = total_turnaround_time_FCFS / len(processes)

    print("Average waiting time for FCFS:", average_waiting_time)
    print("Average turnaround time for FCFS:", average_turnaround_time)

    return total_waiting_time_FCFS, total_turnaround_time_FCFS 


def SJF(processes):
    sorted_processes = sort_processes_by_arrival_time(processes)
    time = 0
    completed = []

    while sorted_processes:
        # Find the first process that has arrived and not yet completed
        eligible_processes = [p for p in sorted_processes if p.arrivalTime <= time]
        if eligible_processes:
            shortest_job = min(eligible_processes, key=lambda x: x.burstTime)
            sorted_processes.remove(shortest_job)
            completed.append(shortest_job)
            time += shortest_job.burstTime
            shortest_job.completionTime = time
            shortest_job.turnAroundTime = shortest_job.completionTime - shortest_job.arrivalTime
            shortest_job.waitTime = shortest_job.turnAroundTime - shortest_job.burstTime
        else:
            # If no eligible process is found, move time to the arrival time of the next process
            next_arrival_time = min(p.arrivalTime for p in sorted_processes)
            time = next_arrival_time

    completed.sort(key=lambda x: x.name)
    
    total_waiting_time_SJF=0
    total_turnaround_time_SJF=0
    for p in sorted_processes:
        total_waiting_time_SJF+=p.waitTime
        total_turnaround_time_SJF+=p.turnAroundTime
    print("total waiting time for SJF:",total_waiting_time_SJF)
    print("total turnaround time time for SJF:",total_turnaround_time_SJF)
    return completed

# # Sort processes by priority  
# def sort_processes_by_priority(processes):
#     return sorted(processes, key=lambda x: x.priority, reverse=True)

# def PS(processes):
#     sorted_processes = sort_processes_by_priority(processes) 
#     completed = []
#     time = 0
    
#     while sorted_processes:
#         # Find process with highest priority that has arrived
#         highest_priority_process = None
#         for p in sorted_processes:
#             if p.arrivalTime <= time and (highest_priority_process == None or p.priority > highest_priority_process.priority):
#                 highest_priority_process = p
                
#         if highest_priority_process:
#             sorted_processes.remove(highest_priority_process)
#             completed.append(highest_priority_process)
#             time += highest_priority_process.burstTime
#             highest_priority_process.completionTime = time 
#             highest_priority_process.turnAroundTime = highest_priority_process.completionTime - highest_priority_process.arrivalTime
#             highest_priority_process.waitTime = highest_priority_process.turnAroundTime - highest_priority_process.burstTime
#         else:
#             next_arrival_time = min(p.arrivalTime for p in sorted_processes)
#             time = next_arrival_time
    
#     return completed

processss=[] 
p1=process(1,0,24,1)
p2=process(2,4,3,2)
p3=process(3,5,3,3)
p4=process(4,6,12,4)
processss.append(p1)
processss.append(p2)
processss.append(p3)
processss.append(p4)

process_FCFS=FCFS(processes)
# process_SJF=SJF(processss)
# process_PS=PS(processes)

# for p in process_FCFS:
#     print(f"Process {p.name}:")
#     print(f"  Arrival Time: {p.arrivalTime}")
#     print(f"  Burst Time: {p.burstTime}")
#     print(f"  Wait Time: {p.waitTime}")
#     print(f"  Turnaround Time: {p.turnAroundTime}")
#     print()


