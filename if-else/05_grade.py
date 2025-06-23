score = int (input("Enter your score : "))
'''
>90 A very Good !!!
>80 B Goog
>70 C Normal 
>60 F Fool !!!
'''
if score >= 90:
    grade = "A"
    comment = "Very Good !!!"
elif score >= 80:
    grade = "B"
    comment ="Good"
elif  score>=70:
    grade = "C"
    comment="Normal"
elif  score>=60:
    grade = "D"
    comment="Pass"
elif score>=50:
    grade = "F"
    comment="Fool"
    
print(f"คะแนน :{score}")
print(f"ได้เกรด :{grade}")
print(f"ความเห็น :{comment}")

    