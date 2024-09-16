
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def gradingsystem():
    result = ""
    if request.method == 'POST':
        try:
            #Variables
            grade = float(request.form['grade'])
            passing_grade = 75
            weight_prelim = 0.20
            weight_midterm = 0.30
            weight_final = 0.50
            #an if statement that will configure the number only(grades) from 0 to 100.
            if grade < 0 or grade > 100:
                result = "The grade must be between 0 to 100."
                return result
            #Formula in order to compute the Grades from Prelim up to Finals
            prelim = passing_grade - grade * weight_prelim / (weight_midterm + weight_final)
            midterm = ((weight_midterm + grade) - prelim) - weight_final
            #An if-else statement that will determine the result of the midterm and prelim formula
            if  passing_grade <= prelim + midterm:
                result = "You Passed, Congratulations!"
            else:
                result = "You didn't meet the required passing Grade"
        except ValueError:
            result = "The grade you entered is not a valid number. It must be a number."
    #html site that came from flask that will show the input and output of the structure of the code.
    return render_template_string('''
        <!doctype html>
        <title>Grade Calculation</title>
        <h1>Grade Calculation</h1>
        <p>Welcome! This Program will determine if you're going to pass or not.</p>
        <form method="post">
            Enter your Prelim grade: <input type="text" name="grade">
            <input type="submit" value="Submit">
        </form>
        <p>{{ result }}</p>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


#// Python code from the scratch //

#grade = input("Please enter your grade: ")
#passing_grade = 75
#weight_prelim = 0.20
#weight_midterm = 0.30
#weight_final = 0.50

#try:
#    grade = float(grade)  # Convert the age input to an integer
#    print(f"You type, {grade}  in the Prelim Grade.")
#    #print(f"overall grade: {(passing_grade-grade*weight_prelim)/(weight_midterm+ weight_final)}")
#    prelim = passing_grade-grade*weight_prelim/(weight_midterm+ weight_final)
#    midterm = ((weight_midterm+grade)-prelim)-(weight_final)
#    
#    print(f"Midterm and Finals ={midterm+prelim}")
#
#
#except ValueError:
#    print("The age you entered is not a valid number.")
#
#
#if prelim+midterm>passing_grade:
#        print("You Passed")
#else:
#        print("You didnt meet the required passing Grade")"