student_dict = {
    "student": ["Craig", "John", "Charles", "Scott"],
    "score": [56, 76, 98, 84]
}

# looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

import pandas as pd

student_df = pd.DataFrame(student_dict)
# print(student_df)

# loop through the df (by column)
# for (key, value) in student_df.items():
#     print(value)

# loop through the df by rows
for (index, row) in student_df.iterrows():
    if row.student == "John":
        print(row.score)