#Conversion of input into float as base
bill_amount = float(input("What is your total bill amount?"))

#str() not required - but helps with organization
service_level = str(input("Level of service? ('good', 'fair', 'bad') "))
if service_level == "good":

    #bill_amount input is converted to float -> tip_amount = float too
    #think of it as float * float
    tip_amount = .20 * bill_amount

elif service_level == "fair":
    tip_amount = .15 * bill_amount
elif service_level == "bad":
    tip_amount = .10 * bill_amount

#now total_bill_amount -> float
total_bill_amount = tip_amount + bill_amount

#in order to even out types, it is necessary for split to be float
split = float(input("Split how many ways?"))
split_amount = total_bill_amount / split    

#notice the "$" in the "$%.2f"
print("Tip amount: "+ "$%.2f " % tip_amount)
    
print("Total amount: " + "$%.2f" % total_bill_amount)
print("Amount per person " + "$%.2f" % split_amount)