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
max_per_day = 14 # hard max for each officer per day
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
    weeks_hours_worked = sum([len(sublist) for sublist in hours_worked[officer].values()])
    todays_hours_worked = len(hours_worked[officer][day])
    week_constraint = max_per_week - weeks_hours_worked
    day_constraint = max_per_day - todays_hours_worked

    if min_hours_per_shift > week_constraint:
        return 0
    if min(hours_needed, min_hours_per_shift) > day_constraint:
        return 0
    
    last_hour_worked = last_two_days_last_hour_worked(officer, day, current_hour)
    if last_hour_worked is not None:
        hour_lapse = current_hour - last_hour_worked
        if hour_lapse >= most_rec_consecutive[officer]:
            consec_hours_only = max_hours
        elif ((hour_lapse == 0) & (most_rec_consecutive[officer] < max_hours)):
            consec_hours_only = max_hours - most_rec_consecutive[officer]
        else:
            return 0
    else:
        consec_hours_only = max_hours
    
    if day_constraint >= hours_needed:
        return min(week_constraint, consec_hours_only)
    else:
        return min(week_constraint, day_constraint, consec_hours_only)

# main code chere
# track which officers are included in schedule
min_personnel = -(-24*7 // 40)
included = peronnel[0:min_personnel]

def assign_hours(day, max_hours):
    prev_day = days_to_cover[days_to_cover.index(day) - 1]
    for officer in included:
        # if hours_to_cover[day] <= 0:
        #     break
        current_hour = hours_in_day - hours_to_cover[day]
        hours_to_work = hours_can_work(officer, day, current_hour, max_hours)
        if hours_to_work == 0:
            continue
        if ((hours_to_work > 0) & (hours_to_work <= hours_to_cover[day])):
            if max(hours_worked[officer][day], default = None) == current_hour or (max(hours_worked[officer][prev_day], default = None) == 24 & current_hour == 0):
                most_rec_consecutive[officer] = most_rec_consecutive[officer] + hours_to_work
            else:
                most_rec_consecutive[officer] = hours_to_work
            for hour in range(hours_to_work):
                hours_worked[officer][day].append(current_hour + hour + 1)
            hours_to_cover[day] = hours_to_cover[day] - hours_to_work
            # greedy part is here.  start over once an assignment is made
            break
        if ((hours_to_work > 0) & (hours_to_work > hours_to_cover[day])):
            if max(hours_worked[officer][day], default = None) == current_hour or (max(hours_worked[officer][prev_day], default = None) == 24 & current_hour == 0):
                most_rec_consecutive[officer] = most_rec_consecutive[officer] + hours_to_cover[day]
            else:
                most_rec_consecutive[officer] = hours_to_cover[day]
            for hour in range(hours_to_cover[day]):
                hours_worked[officer][day].append(current_hour + hour + 1)
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
        if hours_worked == start_sched:
            included.append(peronnel[min_personnel])
            min_personnel = min_personnel + 1

results_df = pd.DataFrame(hours_worked)

# 24-hour coverage check per day
sum([results_df[x].str.len() for x in results_df.columns]) == 24
# check max hours per week
[sum(results_df[x].str.len())<= 40 for x in results_df.columns] 
# check max hours per day
[results_df[x].str.len()<= 14 for x in results_df.columns] 

# calculate cost - make more dynamic in the future
fixed_cost = sum([1000 for i in included])
variable_cost = sum([sum(results_df[x].str.len())*15 for x in results_df.columns])
total_cost = fixed_cost + variable_cost

# any visualizations?
# results_melted = pd.melt(results_df, id_vars='Method Used'
#                         , var_name="Result Type", value_vars=["Number of Stops", "Total Driving Time"]
#                         , value_name="Values")

# sns.set(style="darkgrid")
# ax = sns.barplot(x="Result Type", y="Values", hue = "Method Used", data=results_melted)
# for col in ax.patches:
#     height = col.get_height()
#     ax.text(col.get_x()+col.get_width()/2., height + 1.5,
#             int(height), ha="center") 
# plt.show()
