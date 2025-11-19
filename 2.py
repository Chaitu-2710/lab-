a) Statistics Library
 The statistics library in Python provides functions for mathematical
 statistics calculations, like mean, median, mode, variance, and standard
 deviation.
 Functions :
❖ mean(): Returns the arithmetic mean of data.
❖ median(): Returns the median (middle value) of data.
❖ mode(): Returns the most common data point.
❖ variance(): Calculates the variance of the data.
❖ stdev(): Calculates the standard deviation of data.
 Program :
 import statistics
 data = [10, 20, 30, 40, 50]
 2
Downloaded by Raviteja Yedavelli (yedavelliraviteja@gmail.com)
lOMoARcPSD|51861384
 print("Mean:", statistics.mean(data))
 print("Median:", statistics.median(data))
 print("Mode:", statistics.mode([1, 2, 2, 3]))
 print("Variance:", statistics.variance(data))
 print("Standard Deviation:", statistics.stdev(data))
 Output :
 Mean: 30
 Median: 30
 Mode: 2
 Variance: 250
 Standard Deviation: 15.811388300841896
 b) Math Library:
 The math library provides functions for performing basic mathematical
 operations such as logarithms, trigonometry, factorials, powers, and
 constants like pi.
 Functions :
❖ sqrt(): Returns the square root of a number.
❖ log(): Returns the natural logarithm (log base e).
❖ pow(): Returns the value of x raised to the power y.
❖ factorial(): Returns the factorial of a number.
❖ sin(), cos(), tan(): Trigonometric functions.
 Program :
 import math
 print("Square root of 25:", math.sqrt(25))
 print("Log of 100:", math.log(100))
 angle = math.pi / 4
 print("Sine of 45 degrees:", math.sin(angle))
 print("Cosine of 45 degrees:", math.cos(angle))
 print("Pi value:", math.pi)
 Output :
 Square root of 25: 5.0
 Log of 100: 4.605170185988092
 Sine of 45 degrees: 0.7071067811865475
 Cosine of 45 degrees: 0.7071067811865476
 Pi value: 3.141592653589793
 3
Downloaded by Raviteja Yedavelli (yedavelliraviteja@gmail.com)
lOMoARcPSD|51861384
 c) NumPy Library:
 NumPy (Numerical Python) is a powerful library for performing
 numerical and matrix operations. It provides support for large
 multi-dimensional arrays and matrices, along with a collection of
 mathematical functions to operate on these arrays.
 Features :
❖ Arrays: Supports multi-dimensional arrays (1D, 2D, etc.).
❖ Linear Algebra: Matrix operations, determinants, eigenvalues,
 etc.
❖ Random Sampling: Provides methods to generate random
 numbers.
 Program :
 import numpy as np
 array1 = np.array([1, 2, 3, 4, 5])
 print("1D Array:", array1)
 array2 = np.array([[1, 2, 3], [4, 5, 6]])
 print("2D Array:\n", array2)
 print("Sum of array1:", np.sum(array1)) # 15
 print("Mean of array2:", np.mean(array2)) # 3.5
 matrix1 = np.array([[1, 2], [3, 4]])
 matrix2 = np.array([[5, 6], [7, 8]])
 print("Matrix multiplication:\n", np.dot(matrix1, matrix2))
 Output :
 1D Array: [1 2 3 4 5]
 2D Array:
 [[1 2 3]
 [4 5 6]]
 Sum of array1: 15
 Mean of array2: 3.5
 Matrix multiplication:
 [[19 22]
 [43 50]]
 d) SciPy Library:
 SciPy (Scientific Python) builds on NumPy and provides additional tools
 for scientific computing. It is commonly used for optimization,
 integration, interpolation, eigenvalue problems, and statistics.
 4
Downloaded by Raviteja Yedavelli (yedavelliraviteja@gmail.com)
lOMoARcPSD|51861384
 Features :
❖ Optimization: Functions for minimizing or maximizing.
❖ Linear Algebra: Solving linear systems, eigenvalues.
❖ Signal Processing: FFT, filtering.
❖ Statistics: PDF, CDF, statistical tests.
 Program :
 from scipy import stats
 import numpy as np
 data = np.random.normal(0, 1, 1000)
 mean, variance = stats.norm.fit(data)
 print("Mean of the data:", mean)
 print("Variance of the data:", variance)
 t_statistic, p_value = stats.ttest_1samp(data, 0)
 print("T-test statistic:", t_statistic)
 print("P-value:", p_value)
 Output :
 Mean of the data: 0.020227221229950007
 Variance of the data: 1.0132553470704482
 T-test statistic: 0.6309574379565216


Statistics library
Python statistics module provides the functions to mathematical statistics of numeric data.
The four functions are common in statistics library:
1. mean() - average value
2. median() - middle value
3. mode() - most often value
4. standard deviation - spread of value
Mean() function
The mean() function is used to calculate the arithmetic mean of the numbers in the list.
Example
import statistics
# list of positive integer numbers
datasets = [5, 2, 7, 4, 2, 6, 8]
x = statistics.mean(datasets)
# Printing the mean
print("Mean is :", x)
Median() function
The median() function is used to return the middle value of the numeric data in the list.
Example
import statistics
# list of positive integer numbers
datasets = [5, 2, 7, 4, 2, 6, 8]
x = statistics.mean(datasets)
3
Machine learning
Dept of CSE , SNTI, Hyd
# Printing the median
print("Median is :", x)
Mode() function:
The mode() function returns the most common data that occurs in the list.
Example
import statistics
# list of positive integer numbers
datasets = [2, 4, 7, 7, 2, 2, 3, 6, 6, 8]
x = statistics.mode(datasets)
# Printing the mode
print("Mode is :", x)
stdev() function
The stdev() function is used to calculate the standard deviation on a given sample which is
available in the form of the list.
Example
import statistics
# list of positive integer numbers
datasets = [1,0,1,1,1,1]
x = statistics.stdev(datasets)
# Printing the mode
print("Standard deviation is :", x)
Maths library:
 Math Module is an in-built Python library made to simplify mathematical tasks in
Python.
 It consists of various mathematical constants and functions that can be used after
importing the math module.

Example
import math
print("Demonstrating ceil() function")
#Round a number upward to its nearest integer
print(math.ceil(2.1))
print(math.ceil(1.4))
print(math.ceil(-5.3))
print("Demonstrating factorial() function")
#Return factorial of a number
print(math.factorial(2))
print(math.factorial(4))
print(math.factorial(6))
5
Machine learning
Dept of CSE , SNTI, Hyd
print("Demonstrating floor() function")
#Round numbers to the nearest integer
print(math.floor(2.6))
print(math.floor(1.2))
print(math.floor(3.2))
print("Demonstrating gcd() function")
#find the greatest common divisor of the two integers
print(math.gcd(3,6))
print(math.gcd(1,2))
print(math.gcd(3,9))
print("Demonstrating isnan() function")
#check whether the number is Not A Number (NaN) or not
print(math.isnan(12))
print(math.isnan(-2))
print(math.isnan(math.nan))
print("Demonstrating sqrt() function")
#calculating squareroot of a value
print(math.sqrt(10))
print(math.sqrt(3))
print(math.sqrt(9))
Numpy :
 Numpy is Numerical Python
 NumPy(Numerical Python) is a fundamental library for Python numerical computing.
 It provides efficient multi-dimensional array objects and various mathematical functions
for handling large datasets making it a critical tool for professionals in fields that require
heavy computation.
6
Machine learning
Dept of CSE , SNTI, Hyd
Example
import numpy as np
# Creating a 1D array
x = np.array([1, 2, 3])
# Creating a 2D array
y = np.array([[1, 2], [3, 4]])
# Creating a 3D array
z = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(x)
print(y)
print(z)
Create a NumPy ndarray Object
NumPy is used to work with arrays. The array object in NumPy is called ndarray.
We can create a NumPy ndarray object by using the array() function.
Example
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
SciPy module:
 SciPy stands for Scientific Python.
 It provides more utility functions for optimization, stats and signal processing.
 Like NumPy, SciPy is open source so we can use it freely.
 SciPy was created by NumPy's creator Travis Olliphant.
Once SciPy is installed, import the SciPy module(s) you want to use in your applications by
adding the
from scipy import module statement:
Eg : from scipy import constants
#importing constants module from Scipy
7
Machine learning
Dept of CSE , SNTI, Hyd
Example
from scipy import stats
a= [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(a)
print(x)
Example
import numpy
a= [86,87,88,86,87,85,86]
x = numpy.std(a)
print(x)

     
 P-value: 0.5282126755151515
