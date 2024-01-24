#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fullname(first_name, last_name):
    return first_name + " " + last_name

def string_alternative(full_name):
    return full_name[::2]

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    full_name = fullname(first_name, last_name)
    print("Full name is :", full_name)

    result = string_alternative(full_name)
    print("Output:", result)

if __name__ == "__main__":
    main()


# In[2]:


import collections

def wordcount(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    word_count = {}
    for line in lines:
        words = line.split()
        word_count[line.strip()] = dict(collections.Counter(words))

    return word_count

def print_wordcount(word_count):
    for line, counts in word_count.items():
        print(line)
        print("Word_Count:")
        for word, count in counts.items():
            print(f"{word}: {count}")
        print()

word_count = wordcount('input.txt')

print_wordcount(word_count)

with open('output.txt', 'w') as f:
    for line, counts in word_count.items():
        f.write(line + '\n')
        f.write("Word_Count:\n")
        for word, count in counts.items():
            f.write(f"{word}: {count}\n")
        f.write('\n')


# In[3]:


#Nested Interactive loop.

def inches_to_centimeters(inches):
    return round(inches * 2.54, 2)

num_customers = int(input("Enter the number of customers: "))
heights_inches = []
heights_centimeters = []

for i in range(num_customers):
    height_inches = float(input(f"Enter height in inches for customer {i + 1}: "))
    heights_inches.append(height_inches)
    height_centimeters = inches_to_centimeters(height_inches)
    heights_centimeters.append(height_centimeters)

print(heights_centimeters)


# In[4]:


def convert_heights(heights_inches):
    return [inches * 2.54 for inches in heights_inches]

def main():
    num_customers = int(input("Enter the number of customers: "))

    heights_inches = [float(input(f"Enter height in inches for customer {i + 1}: ")) for i in range(num_customers)]

    heights_centimeters = convert_heights(heights_inches)

    print("Heights in Centimeters:", heights_centimeters)

if __name__ == "__main__":
    main()


# In[ ]:




