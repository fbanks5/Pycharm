pers_years = int(input())
pers_pounds = int(input())
pers_bpm = int(input())
minutes = int(input())

calories_burned = ((pers_years * 0.2757) + (pers_pounds * 0.03295) + (pers_bpm * 1.0781) - 75.4991) * minutes / 8.368

print(f'Calories: {calories_burned:.2f} calories')

