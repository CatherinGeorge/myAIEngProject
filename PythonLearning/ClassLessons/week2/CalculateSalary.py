def CalculateSalary(basic, hra, da, bonus=0):
    totalsalary = basic+hra+da+bonus
    return totalsalary
calculatesalary_withoutbonus = CalculateSalary(25000, 10000, 5000)
calculatesalray_withbonus = CalculateSalary(25000, 10000, 5000, 2000)
print(calculatesalary_withoutbonus)
print(calculatesalray_withbonus)
