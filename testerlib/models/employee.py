# -*- coding: utf-8 -*-

"""
    testerlib.models.employee
 
    This file was automatically generated for Stamplay by APIMATIC v2.0 ( https://apimatic.io ) on 08/03/2016
"""

from testerlib.models.base_model import BaseModel
from testerlib.models.person import Person
from testerlib.models.person import Person

class Employee(Person):

    """Implementation of the 'Employee' model.

    TODO: type model description here.
    NOTE: This class inherits from 'Person'.

    Attributes:
        boss (Person): TODO: type description here.
        department (string): TODO: type description here.
        dependents (list of Person): TODO: type description here.
        joining_day (Days): TODO: type description here.
        salary (int): TODO: type description here.
        working_days (list of Days): TODO: type description here.

    """

    def __init__(self, 
                 address = None,
                 age = None,
                 boss = None,
                 department = None,
                 dependents = None,
                 joining_day = 'Monday',
                 name = None,
                 salary = None,
                 uid = None,
                 working_days = None):
        """Constructor for the Employee class"""
        
        # Initialize members of the class
        self.boss = boss
        self.department = department
        self.dependents = dependents
        self.joining_day = joining_day
        self.salary = salary
        self.working_days = working_days

        # Call the constructor for the base class
        super(Employee, self).__init__(address,
                                       age,
                                       name,
                                       uid)

        # Create a mapping from Model property names to API property names
        self.names = {
            "address": "address",
            "age": "age",
            "boss": "boss",
            "department": "department",
            "dependents": "dependents",
            "joining_day": "joiningDay",
            "name": "name",
            "salary": "salary",
            "uid": "uid",
            "working_days": "workingDays",
        }

    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """

        if dictionary == None:
            return None
        else:	
            # Extract variables from the dictionary
            address = dictionary.get("address")
            age = dictionary.get("age")
            boss = Person.from_dictionary(dictionary.get("boss")) if dictionary.get("boss") else None
            department = dictionary.get("department")
            dependents = None
            if dictionary.get("dependents") != None:
                dependents = list()
                for structure in dictionary.get("dependents"):
                    dependents.append(Person.from_dictionary(structure))
            joining_day = dictionary.get("joiningDay") if dictionary.get("joiningDay") else 'Monday'
            name = dictionary.get("name")
            salary = dictionary.get("salary")
            uid = dictionary.get("uid")
            working_days = dictionary.get("workingDays")
            # Return an object of this model
            return cls(address,
                       age,
                       boss,
                       department,
                       dependents,
                       joining_day,
                       name,
                       salary,
                       uid,
                       working_days)
