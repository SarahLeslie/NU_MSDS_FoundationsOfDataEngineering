# Gen data, git --  
# (do 24/7, 
# max 8 per day and 40 per week, 
# extra $5 processing charge for each person paid, 
# min 4 hour shift?)

# IMPORTS REQUIRED PACKAGES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import copy

# GENERATES THE PROBLEM
# time needing coverage
hours_in_day = 24
days_to_cover = ['0_mon', '1_tue', '2_wed', '3_thu', '4_fri', '5_sat', '6_sun']

# personnel
peronnel = ['officer1', 'officer2', 'officer3', 'officer4', 'officer5', 'officer6']

# tracking  data structures
hours_to_cover = {}
for day in days_to_cover:
    hours_to_cover[day] = hours_in_day

hours_worked = {}
for officer in peronnel:
    hours_worked[officer] = {}
    for day in days_to_cover:
        hours_worked[officer][day] = []

most_rec_consecutive = {}
for officer in peronnel:
    most_rec_consecutive[officer] = 0

# costs
base_hourly_wage = 15 # dollars
overtime_hourly_wage = 15 + 5 # dollars
onboarding_cost = 1000 # dollars for each officer you have to pay that week

# overtime
consecutive_before_overtime = 8 # consecutive hours before overtime kicks in

# hard constraints
max_per_week = 40 # hard max for each officer per week
max_per_day = 12 # hard max for each officer per day
min_hours_per_shift = 4
max_consecutive = 14 # maximum consecutive hours an officer can work
# officers need a minimum time off equal to the the length of their last shift

# GREEDY ALGORITHM
def last_two_days_last_hour_worked(officer, day, current_hour):
    last_hour_worked = max(hours_worked[officer][day], default = None)
    if last_hour_worked == None:
        prev_day = days_to_cover[days_to_cover.index(day)-1]
        if max(hours_worked[officer][prev_day], default = None) is not None:
            last_hour_worked = max(hours_worked[officer][prev_day]) - hours_in_day
    return last_hour_worked

# at any given time, how many hours can an officer work (before overtime)?
def hours_can_work(officer, day, current_hour, max_hours):
    hours_needed = 24 - current_hour
    if (sum([len(sublist) for sublist in hours_worked[officer].values()]) + min_hours_per_shift) > max_per_week:
        return 0
    if (len(hours_worked[officer][day]) + min(hours_needed, min_hours_per_shift)) > max_per_day:
        return 0
    last_hour_worked = last_two_days_last_hour_worked(officer, day, current_hour)
    if ((last_hour_worked is None) or (current_hour - last_hour_worked)) >= most_rec_consecutive[officer]:
        return min(max_per_week - sum([len(sublist) for sublist in hours_worked[officer].values()]), max_hours)
    else:
        return 0

# main code chere
# track which officers are included in schedule
min_personnel = -(-24*7 // 40)
included = peronnel[0:min_personnel]

def assign_hours(day, max_hours):
    for officer in included:
        if hours_to_cover[day] > 0:
            break
        current_hour = hours_in_day - hours_to_cover[day]
        hours_to_work = hours_can_work(officer, day, current_hour, max_hours)
        #hours_to_work = hours_can_work(officer, day, current_hour, consecutive_before_overtime)
        if hours_to_work > 0 & hours_to_work <= hours_to_cover[day]:
            for hour in range(hours_to_work):
                hours_worked[officer][day].append(current_hour + hour + 1)
            most_rec_consecutive[officer] = hours_to_work
            hours_to_cover[day] = hours_to_cover[day] - hours_to_work
            # greedy part is here.  start over once an assignment is made
            break
        if hours_to_work > 0 & hours_to_work > hours_to_cover[day]:
            for hour in range(hours_to_cover[day]):
                hours_worked[officer][day].append(current_hour + hour + 1)
            most_rec_consecutive[officer] = hours_to_cover[day]
            hours_to_work = hours_to_work - hours_to_cover[day]
            hours_to_cover[day] = 0
            if day != '6_sun':
                next_day = days_to_cover[days_to_cover.index(day) + 1]
                for hour in range(hours_to_work):
                    hours_worked[officer][next_day].append(hour + 1)
                most_rec_consecutive[officer] = most_rec_consecutive[officer] + hours_to_work
                hours_to_cover[next_day] = hours_to_cover[next_day] - hours_to_work
            # greedy part is here.  start over once an assignment is made
            break

# cycle through 'cases' from most desirable to least desirable
for day in days_to_cover:
    while hours_to_cover[day] > 0:
        # greedy part is here.  keep assigning the first available officer.
        start_sched = copy.deepcopy(hours_worked)
        assign_hours(day, consecutive_before_overtime)
        if hours_worked == start_sched:
            assign_hours(day, max_consecutive)
        # if hours_worked == start_sched:
        #     included.append(peronnel[min_personnel])
        #     min_personnel = min_personnel + 1

day = '0_mon'
while hours_to_cover[day] > 0:
    # greedy part is here.  keep assigning the first available officer.
    start_sched = copy.deepcopy(hours_worked)
    assign_hours(day, consecutive_before_overtime)
    if hours_worked == start_sched:
        assign_hours(day, max_consecutive)
    # if hours_worked == start_sched:
    #     included.append(peronnel[min_personnel])
    #     min_personnel = min_personnel + 1

results_df = pd.DataFrame(hours_worked)

results_df[['officer4', 'officer5', 'officer6']]

# testing BFS
breadth_first_search('NYC', 'Los Angeles')

# RESULTS CAPTURE
# instantiates list to capture time test results
results = []
bfs = breadth_first_search('NYC', 'Los Angeles')
d = dijkstras('NYC', 'Los Angeles')
results.append({'Method Used':'Breadth-First Search'
                ,'Path':bfs[0]
                ,'Total Driving Time':bfs[1]
                ,'Number of Stops':bfs[2]})
results.append({'Method Used':'Dijkstra\'s Algorithm'
                ,'Path':d[0]
                ,'Total Driving Time':d[1]
                ,'Number of Stops':d[2]})

# organizes results into pandas dataframe for easier exploration
results_df = pd.DataFrame(results)
results_melted = pd.melt(results_df, id_vars='Method Used'
                        , var_name="Result Type", value_vars=["Number of Stops", "Total Driving Time"]
                        , value_name="Values")

sns.set(style="darkgrid")
ax = sns.barplot(x="Result Type", y="Values", hue = "Method Used", data=results_melted)
for col in ax.patches:
    height = col.get_height()
    ax.text(col.get_x()+col.get_width()/2., height + 1.5,
            int(height), ha="center") 
plt.show()
