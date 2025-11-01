with open(r"C:\Users\CATHERIN\Desktop\Aut_Project\AI Engineer Test Leaf\myAIEngProject\PythonLearning\ClassLessons\week3\reports.txt", "a") as file:
    file.write("\nTestcase4 - Passed")
    file.write("\nTestcase5 - Passed")

with open(r"C:\Users\CATHERIN\Desktop\Aut_Project\AI Engineer Test Leaf\myAIEngProject\PythonLearning\ClassLessons\week3\reports.txt", "r") as file:
    pass_count =0
    failed_count =0

    for line in file:
        #print(line.strip())
        if line.count("Passed"):
            pass_count +=1
        else:
            failed_count +=1

    totalcases = pass_count + failed_count
    print(f"totalcases: {totalcases}")
    print(f"passed: {pass_count}")
    print(f"failed: {failed_count}")
