"""
Program: ch9.py
Author: Casandra Roque
Last Date Modified: 07/08/2025

Creating the blueprint for rational object.
"""
class Rational:
    """
    Represents a rational number.
    """

    def __init__(self, numerator, denominator):
        """Setting the instance variables."""
        self.num = numerator
        self.den = denominator

    def __str__(self):
        """Returns the string rep for rational number."""
        return f"{self.num}/{self.den}"
    
    def __add__(self, other):
        """Adds the current object with another object."""
        newNum = self.num * other.den + other.num * self.den 
        newDen = self.den * other.den 
        return Rational(newNum, newDen)
    
    def __sub__(self, other):
        """Subtracts current with other"""
        newNum = self.num * other.den + other.num * self.den 
        newDen = self.den * other.den 
        return Rational(newNum, newDen)

    def __mul__(self, other):
        """Multiply current with other"""
        newNum = self.num * other.den * other.num * self.den
        newDen = self.den * other.den
        return Rational(newNum, newDen)
    
    def __div__(self, other):
        """Divide current with other"""
        newNum = self.num * other.den
        newDen = self.den * other.num 
        return Rational(newNum, newDen)