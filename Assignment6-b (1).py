#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.


# In[2]:


import json
states= dict()
n=int(input("How many states are there:"))
for i in range(n):
    state = input("Enter name of the state:")
    capital= input("Enter name of the capital:")
    states[state]=capital
print("created dictionary is: ",states)
with open("states.json","w") as f:
    json.dump(states,f,indent=4)
    print("json file is created")
    


# In[ ]:




