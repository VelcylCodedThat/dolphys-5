import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify, diff, integrate, solve, limit, series, Matrix
import cmath

def calculate_function_properties(func, x):
    x_symbol = symbols('x')
    func_symbol = sympify(func)
    
    # Domain
    domain = solve(func_symbol, x_symbol)
    
    # Range
    range_ = [func_symbol.subs(x_symbol, i) for i in domain]
    
    # X-intercepts
    x_intercepts = [i for i in domain if func_symbol.subs(x_symbol, i) == 0]
    
    # Y-intercepts
    y_intercepts = [func_symbol.subs(x_symbol, 0)]
    
    # Derivative
    derivative = diff(func_symbol, x_symbol)
    
    # Integral
    integral = integrate(func_symbol, x_symbol)
    
    # Asymptotes
    asymptotes = [limit(func_symbol, x_symbol, i) for i in [-float('inf'), float('inf')]]
    
    # Intervals of increase and decrease
    intervals_increase = solve(diff(func_symbol, x_symbol) > 0, x_symbol)
    intervals_decrease = solve(diff(func_symbol, x_symbol) < 0, x_symbol)
    
    # Critical points
    critical_points = solve(diff(func_symbol, x_symbol), x_symbol)
    
    # Extrema points
    extrema_points = solve(diff(diff(func_symbol, x_symbol), x_symbol), x_symbol)
    
    # Intervals of concavity
    intervals_concavity = solve(diff(diff(func_symbol, x_symbol), x_symbol) > 0, x_symbol)
    
    # Inflection points
    inflection_points = solve(diff(diff(func_symbol, x_symbol), x_symbol), x_symbol)
    
    # Limit
    limit_ = limit(func_symbol, x_symbol, float('inf'))
    
    # Taylor polynomial
    taylor_polynomial = series(func_symbol, x_symbol, 0, 10)
    
    # Graph
    try:
        plt.clf()  # Clear the canvas
        x_values = np.linspace(-10, 10, 400)
        y_values = [float(func_symbol.subs(x_symbol, i)) for i in x_values]
        plt.plot(x_values, y_values)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of the function')
        plt.grid(True)
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.show()
    except Exception as e:
        print(f"Error graphing: {str(e)}")
    
    return {
        'domain': domain,
        'range': range_,
        'x_intercepts': x_intercepts,
        'y_intercepts': y_intercepts,
        'derivative': derivative,
        'integral': integral,
        'asymptotes': asymptotes,
        'intervals_increase': intervals_increase,
        'intervals_decrease': intervals_decrease,
        'critical_points': critical_points,
        'extrema_points': extrema_points,
        'intervals_concavity': intervals_concavity,
        'inflection_points': inflection_points,
        'limit': limit_,
        'taylor_polynomial': taylor_polynomial,
        'equation': func_symbol
    }

def normal_math():
    print("Normal Math Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Logarithm")
    print("8. Trigonometry")
    print("9. Complex Number Operations")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The result is: {result}")
    elif choice == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print(f"The result is: {result}")
    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        print(f"The result is: {result}")
    elif choice == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 != 0:
            result = num1 / num2
            print(f"The result is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == 5:
        num = float(input("Enter the number: "))
        if num >= 0:
            result = num ** 0.5
            print(f"The result is: {result}")
        else:
            print("Error: Cannot calculate the square root of a negative number.")
    elif choice == 6:
        num1 = float(input("Enter the base: "))
        num2 = float(input("Enter the exponent: "))
        result = num1 ** num2
        print(f"The result is: {result}")
    elif choice == 7:
        num = float(input("Enter the number: "))
        base = float(input("Enter the base: "))
        if base > 0 and base != 1:
            result = np.log(num) / np.log(base)
            print(f"The result is: {result}")
        else:
            print("Error: The base must be positive and not equal to 1.")
    elif choice == 8:
        print("Trigonometry:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        
        trig_choice = int(input("Enter your choice: "))
        
        if trig_choice == 1:
            angle = float(input("Enter the angle in degrees: "))
            result = np.sin(np.radians(angle))
            print(f"The result is: {result}")
        elif trig_choice == 2:
            angle = float(input("Enter the angle in degrees: "))
            result = np.cos(np.radians(angle))
            print(f"The result is: {result}")
        elif trig_choice == 3:
            angle = float(input("Enter the angle in degrees: "))
            result = np.tan(np.radians(angle))
            print(f"The result is: {result}")
        else:
            print("Invalid choice. Please try again.")
    elif choice == 9:
        print("Complex Number Operations:")
        real1 = float(input("Enter the real part of the first complex number: "))
        imag1 = float(input("Enter the imaginary part of the first complex number: "))
        real2 = float(input("Enter the real part of the second complex number: "))
        imag2 = float(input("Enter the imaginary part of the second complex number: "))
        
        complex1 = complex(real1, imag1)
        complex2 = complex(real2, imag2)
        
        print(f"Addition: {complex1 + complex2}")
        print(f"Subtraction: {complex1 - complex2}")
        print(f"Multiplication: {complex1 * complex2}")
        print(f"Division: {complex1 / complex2}")
    else:
        print("Invalid choice. Please try again.")

def calculus():
    print("Calculus Operations:")
    print("1. Numerical Differentiation")
    print("2. Numerical Integration")
    print("3. Optimization")
    print("4. Motion Problems")
    
    calc_choice = int(input("Enter your choice: "))
    
    if calc_choice == 1:
        func = input("Enter the function (in the format 'x**2 + 3*x + 2'): ")
        x = float(input("Enter the point: "))
        h = float(input("Enter the step size: "))
        func_symbol = sympify(func)
        derivative = (func_symbol.subs('x', x + h) - func_symbol.subs('x', x)) / h
        print(f"The derivative at x = {x} is: {derivative}")
    elif calc_choice == 2:
        func = input("Enter the function (in the format 'x**2 + 3*x + 2'): ")
        a = float(input("Enter the lower limit: "))
        b = float(input("Enter the upper limit: "))
        n = int(input("Enter the number of subintervals: "))
        func_symbol = sympify(func)
        integral = 0
        dx = (b - a) / n
        for i in range(n):
            x = a + i * dx
            integral += func_symbol.subs('x', x) * dx
        print(f"The approximate value of the integral is: {integral}")
    elif calc_choice == 3:
        func = input("Enter the function (in the format 'x**2 + 3*x + 2'): ")
        x = symbols('x')
        func_symbol = sympify(func)
        constraint = input("Enter the constraint (in the format 'x >= 0'): ")
        constraint_symbol = sympify(constraint)
        result = solve((func_symbol, constraint_symbol), x)
        print(f"The optimal value is: {result}")
    elif calc_choice == 4:
        print("Motion Problems:")
        print("1. Distance and Displacement")
        print("2. Velocity and Acceleration")
        
        motion_choice = int(input("Enter your choice: "))
        
        if motion_choice == 1:
            s = input("Enter the position function (in the format 't**2 + 3*t + 2'): ")
            t = float(input("Enter the time: "))
            s_symbol = sympify(s)
            distance = s_symbol.subs('t', t)
            print(f"The distance at t = {t} is: {distance}")
        elif motion_choice == 2:
            v = input("Enter the velocity function (in the format 't**2 + 3*t + 2'): ")
            t = float(input("Enter the time: "))
            v_symbol = sympify(v)
            velocity = v_symbol.subs('t', t)
            print(f"The velocity at t = {t} is: {velocity}")
        else:
            print("Invalid choice. Please try again.")

def statistics():
    print("Statistics Operations:")
    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    print("4. Standard Deviation")
    
    stat_choice = int(input("Enter your choice: "))
    data = input("Enter the data (comma-separated): ")
    data = [float(i) for i in data.split(',')]
    
    if stat_choice == 1:
        mean = np.mean(data)
        print(f"The mean is: {mean}")
    elif stat_choice == 2:
        median = np.median(data)
        print(f"The median is: {median}")
    elif stat_choice == 3:
        mode = max(set(data), key=data.count)
        print(f"The mode is: {mode}")
    elif stat_choice == 4:
        std_dev = np.std(data)
        print(f"The standard deviation is: {std_dev}")
    else:
        print("Invalid choice. Please try again.")

def matrix_operations():
    print("Matrix Operations:")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Matrix Determinant")
    print("5. Matrix Inverse")
    
    matrix_choice = int(input("Enter your choice: "))
    
    if matrix_choice in [1, 2, 3]:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        print("Enter the first matrix:")
        matrix1 = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i + 1}: ").split()))
            matrix1.append(row)
        
        print("Enter the second matrix:")
        matrix2 = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i + 1}: ").split()))
            matrix2.append(row)
        
        mat1 = Matrix(matrix1)
        mat2 = Matrix(matrix2)
        
        if matrix_choice == 1:
            result = mat1 + mat2
            print(f"The result of addition is:\n{result}")
        elif matrix_choice == 2:
            result = mat1 - mat2
            print(f"The result of subtraction is:\n{result}")
        elif matrix_choice == 3:
            result = mat1 * mat2
            print(f"The result of multiplication is:\n{result}")
    
    elif matrix_choice == 4:
        rows = int(input("Enter the number of rows (and columns for square matrix): "))
        print("Enter the matrix:")
        matrix = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i + 1}: ").split()))
            matrix.append(row)
        
        mat = Matrix(matrix)
        determinant = mat.det()
        print(f"The determinant is: {determinant}")
    
    elif matrix_choice == 5:
        rows = int(input("Enter the number of rows (and columns for square matrix): "))
        print("Enter the matrix:")
        matrix = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i + 1}: ").split()))
            matrix.append(row)
        
        mat = Matrix(matrix)
        try:
            inverse = mat.inv()
            print(f"The inverse of the matrix is:\n{inverse}")
        except Exception as e:
            print(f"Error: {str(e)}. The matrix may not be invertible.")

def plot_generator():
    print("Plot Generator:")
    print("1. Dotplot")
    print("2. Boxplot")
    print("3. Histogram")
    
    plot_choice = int(input("Enter your choice: "))
    
    if plot_choice == 1:
        data = input("Enter the data (in the format '1, 2, 3, 4, 5'): ")
        data = [int(i) for i in data.split(',')]
        plt.clf()
        plt.scatter(range(len(data)), data)
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title('Dotplot')
        plt.grid(True)
        plt.show()
    elif plot_choice == 2:
        data = input("Enter the data (in the format '1, 2, 3, 4, 5'): ")
        data = [int(i) for i in data.split(',')]
        plt.clf()
        plt.boxplot(data)
        plt.title('Boxplot')
        plt.grid(True)
        plt.show()
    elif plot_choice == 3:
        data = input("Enter the data (in the format '1, 2, 3, 4, 5'): ")
        data = [int(i) for i in data.split(',')]
        plt.clf()
        plt.hist(data, bins=10)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Histogram')
        plt.grid(True)
        plt.show()
    else:
        print("Invalid choice. Please try again.")

def credits():
    print("Fully developed by Aditya Bhide.")
    print("Credit to the developer of matplotlib, Michael Droettboom, for the actual graphing interface.")

def main():
    while True:
        print("Dolphys Calculator")
        print("Made By Aditya Bhide")
        print("Version 2.4")
        print("-----------------------------")
        print("Calculator Menu:")
        print("1. Function Calculator")
        print("2. Normal Math Operations")
        print("3. Calculus")
        print("4. Statistics")
        print("5. Matrix Operations")
        print("6. Plot Generator")
        print("7. Exit")
        print("8. Credits")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            func = input("Enter the function (in the format 'x**2 + 3*x + 2'): ")
            x = symbols('x')
            properties = calculate_function_properties(func, x)
            print("Properties of the function:")
            for key, value in properties.items():
                print(f"{key.capitalize()}: {value}")
            print(f"Equation: y = {properties['equation']}")
        elif choice == 2:
            normal_math()
        elif choice == 3:
            calculus()
        elif choice == 4:
            statistics()
        elif choice == 5:
            matrix_operations()
        elif choice == 6:
            plot_generator()
        elif choice == 7:
            print("Exiting...")
            break
        elif choice == 8:
            credits()
            continue
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()