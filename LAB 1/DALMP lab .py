#!/usr/bin/env python
# coding: utf-8

# In[1]:


file= open("D:\\CHRIST UNIVERSITY\\DALMP\\bank.csv","r")
data = file.readlines()


# In[2]:


def header():
 headers = data[0].strip().split(',')
 print(headers)
header()


# In[3]:


def marital(data):
    m=0
    s=0
    d=0
    for item in data:
        count=item.split(";")
        marital=count[2].strip('"')
        if marital=="married":
            m+=1
        elif marital=="divorced":
            d+=1
        else:
            s+=1
    print("The count of married people: ",m)
    print("The count of single people: ",s)
    print("The count of divorced people: ",d)


# 

# In[4]:


marital(data)


# In[10]:


def prepare_age_histogram(data):
    # Prepare a histogram for age
    ages = []
    for line in data[1:]:
        customer = line.strip().split(';')
        age = int(customer[0])  
        ages.append(age)

    age_classes = {}
    for age in ages:
        age_class = age // 10 * 10
        if age_class in age_classes:
            age_classes[age_class] += 1
        else:
            age_classes[age_class] = 1

    print("Histogram for age:")
    for age_class, count in age_classes.items():
        print(f"{age_class}-{age_class + 9}: {'|' * count}")


# In[11]:


prepare_age_histogram(data)


# In[ ]:




