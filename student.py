"""
Program: ch9.py
Author: Casandra Roque
Last Date Modified: 07/08/2025

Creating the blueprint for student object.
"""

class Student: # class usually starts with an uppercase letter
    """
    Represents a student name with their scores for a course management app.
    """

    # creating a constructor
    def __init__(self, name, number): # parameter always includes self with class 
        """
        Class constructor: Creates an object using the class blueprint.
        Parameter: 
        * name - represents the student's name 
        * score - represents the student's list of scores
        """
        self.name = name
        self.scores = [0 for i in range(number)] # list comprehension

    # Accessor - getting information (returns the data) such as "s.getName()"
    # Mutator - change the state of the object such as "s.setScore(i, score)"

    # Accessor Methods
    def getName(self): 
        """
        Returns the student's name.
        """
        return self.name
    
    def getScore(self, i):
        """Returns the student's ith score, i must range 1 through the number of scores."""
        if i >= 1 and i <= len(self.scores):
            return self.scores[i - 1]
        else:
            return None
        
    def getAverage(self):
        """Returns student's average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns student's highest score."""
        return max(self.scores)
    
    # Mutator Methods

    def setScore(self, i, score):
        """Resets the student's ith score to score, i must range from 1 through number of scores."""
        if i >= 1 and i <= len(self.scores):
            self.scores[i - 1] = score
    
    # String Representation
    def __str__(self):
        """Returns a string rep of the student's info."""
        # Map: Converting all integer scores into strings
        # Join: We are joining all the values in the list with a space in between
        return f"Name: {self.name}\nScores: {" ".join(map(str, self.scores))}"
    
    def save(self, fileName = None):
        """Saves pickled student objecys to a file. The parameter allows user to change file names."""
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        with open(self.fileName, "wb") as fileObj:
            pickle.dump(self, fileObj)