##################### Challenges Faced and Solutions I found during the Project #####################

PROBLEM 
- While implementing load_user_database(self) and save_user_info(user_info), when appending json strings to file I was not able 
to read from it because json strings were badly formatted:

BAD Example: 
 {"2e7d16e4cec1c0e561d9d70b239977bda8cc414fc42a8782790583379e1b553e": ["Lucas", "de Oliveira", []]}{"94a2082acd1d4c5074f09fa95fb6b916768ef5a8557739928531e1ac1db29fd5": ["Lucas", "de Oliveira", []]}

GOOD Example:
[
    {"2e7d16e4cec1c0e561d9d70b239977bda8cc414fc42a8782790583379e1b553e": ["Lucas", "de Oliveira", []]},{"94a2082acd1d4c5074f09fa95fb6b916768ef5a8557739928531e1ac1db29fd5": ["Lucas", "de Oliveira", []]}
]

to get GOOD Example I would have to load existing content from file to a python list and then append new data to it. Even though this is a small personal project, loading the whole file every time I want to add a new user feels inefficient.

SOLUTION:
- file.write(json.dumps(user_info) + "\n")
    - writing to file using json.dumps() and adding a new string

-  for line in file:
                    my_list.append(json.loads(line.strip()))

    - When reading, reading one line at a time