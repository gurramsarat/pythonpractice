pr_marks=int(input("Enter the project marks: "))
in_marks=int(input("Enter the internal marks: "))
ex_marks=int(input("Enter the external marks: "))
if pr_marks>=50:
    print()
else:
    print("you have failed in Project Marks,  your marks should be greater than 50",pr_marks)
if in_marks>=50:
    print()
else:
    print("you have failed in Internal Marks, your marks should be greater than 50 ",in_marks )
if ex_marks>=50:
    print()
else:
    print("you have failed in External Marks,  your marks should be greater than 50 ",ex_marks)
#if pr_marks>=50 and in_marks>=50 and ex_marks>=50:
    #print()
#else:
    #print("As you have failed in your subjects,there is no grade provide for you ")
if pr_marks>=50:
    if in_marks>=50:
        if ex_marks>=50:
            total_score=(70/100)*pr_marks+(20/100)*ex_marks+(10/100)*in_marks
            print("Total score = ",total_score)
            if total_score>=90:
                print("A Grade")
            elif total_score>=75 and total_score<90:
                print("B Grade")
            else:
                print("C Grade")