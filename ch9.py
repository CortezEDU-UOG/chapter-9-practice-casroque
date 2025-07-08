"""
Program: ch9.py
Author: Casandra Roque
Last Date Modified: 07/08/2025

This code is a course management application that represents info of students in course.
"""

from student import Student
from rational import Rational

def main():
    s = Student("Maria", 5)
    print(s)
    s.setScore(1,100)
    print(s)
    print(s.getHighScore())
    print(s.getAverage())
    print(s.getScore(1))
    print(s.getName())

def rationalMain():
    """Main function to test the Rational class"""
    oneHalf = Rational(1, 2)
    oneSixth = Rational(1, 6)
    print(oneHalf)
    # print(oneHalf + oneSixth)

if __name__ == "__main__":
    main()
    rationalMain()