#!/usr/bin/env python
# coding: utf-8

# In[1]:


#first project - student information


# In[1]:


import csv

def write_into_csv(info_list):
    with open("student_info.csv","a",newline="") as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact Number", "Email-Id"])
        
        writer.writerow(info_list)

if __name__=="__main__":
    
        condition=True
        student_no=1
        
        while(condition):
            student_info = input("Enter student information for student #{} in the following format(Name Age Contact_no Email_Id): ".format(student_no))
            #print("Entered information: "+ student_info)
    
            student_info_list= student_info.split(' ')
            #print("Entered split up info is "+ str(student_info_list))
            
            print("\nThe entered information is-\nName: {}\nAge: {}\nContact_no: {}\nEmail_Id: {}"
                  .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
            
            choice_check= input("Is this information correct? (yes/no): ")
            
            if choice_check == "yes":
                write_into_csv(student_info_list)
      
                condition_check= input("Enter (yes/no) if you want to print information for another student: ")
                if condition_check=="yes":
                    condition=True
                    student_no= student_no + 1
                elif condition_check=="no":
                    condition=False
            elif choice_check == "no":
                print("\nPlease re-enter the vaules!")


# In[ ]:




