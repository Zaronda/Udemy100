#print("Print('what shall i print?')")
student_dict = {
	"student": ["Angela", "James", "Lily"],
	"score": [56, 76, 85]
}

# can loop through easily
for (key, value) in student_dict.items():
	print(value)
	
    # import pandas as pd
import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# loop thru dataframe
#for (key, value) in student_data_frame.items():
#	print(value)

# loop thru rows using inbuilt loop in pandas
for (index, row) in student_data_frame.iterrows():
	print(row.student)
	