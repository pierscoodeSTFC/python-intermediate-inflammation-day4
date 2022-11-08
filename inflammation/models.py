"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""

import numpy as np

class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)


class Person:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Doctor(Person):
    """Doctor and stuff
    """
    def __init__(self, name: str):
        """_summary_
        """
        super().__init__(name)
        self.patients = []
    
    def add_patient(self, new_patient):
        # A crude check by name if this patient is already looked after
        # by this doctor before adding them
        for patient in self.patients:
            if patient.name == new_patient.name:
                return
        self.patients.append(new_patient)


class Patient(Person):
    """Patient with a name and observations.
    """
    def __init__(self, name: str):
        """_summary_
        """
        super().__init__(name)
        self.observations = []

    @property
    def last_observation(self):
        return self.observations[-1]

    def add_observations(self, value, day=None):
        """_summary_

        Args:
            value (_type_): _description_
            day (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if day is None:
            if self.observations:
                day = self.observations[-1].day + 1
            else:
                day = 0

        new_observation = Observation(day, value)
        self.observations.append(new_observation)
        return new_observation


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array for each day.

    :param data: A 2D data array with inflammation data (each row contains
                measurements for a single patient across all days).
    :returns: An array of mean values of measurements for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily maximum of a 2D inflammation data array for each day.

    :param data: A 2D data array with inflammation data (each row contains
                measurements for a single patient across all days).
    :returns: An array of max values of measurements for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily minimum of a 2D inflammation data array for each day.

    :param data: A 2D data array with inflammation data (each row contains
                measurements for a single patient across all days).
    :returns: An array of minimum values of measurements for each day.
    """
    return np.min(data, axis=0)
