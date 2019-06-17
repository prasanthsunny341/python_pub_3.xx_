# pblm2 xyzcompany data
emp_id = [100, 199, 299, 399, 499, 599, 699, 799, 899]
emp_designation = ["CEO","CMO","DeliveryManager","projectManager","Teamlead","developer","tester","DBA","Datascientist"]
emp_salary =[10000,8000,5000,1000,750,100,50,200,5500]

class MNCcompany:
    def __init__(self, emp_id,emp_designation,emp_salary,Glassdore_Emp_prediction):
        self.emp_id = emp_id
        self.emp_designation = emp_designation
        self.emp_salary = emp_salary
        self.Glassdore_Emp_prediction = Glassdore_Emp_prediction
    def employee(emp_ids,emp_designations,emp_salarys):
         #self.emp_id = [100, 199, 299, 399, 499, 599, 699, 799, 899]
        print("Employee id's  of MNCcompany:",sorted(emp_ids))
        print("Designation of Employee:",sorted(emp_designations))
        print("Salary of Employee:",sorted(emp_salarys))
    def Glassdore_Emp_prediction(emp_salarys):
            if (max(emp_salary)):
                print("CEO is the highest salary holder  of MNCcomapny")
            else:
                print("first if loop Bug Fix it now")
            if (min(emp_salary)):
                print("OOPS developer is the lowest earning profession in MNCcompany")
            else:
                print("second if loop bug fix it now")

MNCcompany.employee(emp_id,emp_designation,emp_salary)
"""Usee if/elif to deal with conditions
as per Glassdoor salary review , predict and assign the respective salary's to the respective designation  and
#note:I never care about emp_ids """
#Highest salary is CEO as per Glassdoor review
maximum_salary =  max(emp_salary)
print("employee with  maximum_salary of",maximum_salary,"k$" )
MNCcompany.Glassdore_Emp_prediction(emp_salary)
