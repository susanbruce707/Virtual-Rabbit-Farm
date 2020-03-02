# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 08:15:15 2020.
class to create a virtul rabbit with DOB time stamp.
make a dictionary of rabbit attributes.
diplay information about rabbit.
class rabbit requires 5 arguments:
name, fur_colour, eye_colour, sex, breed; all types string.
@author: susan.
"""

from datetime import datetime
import csv_mod
class Rabbit():
    """
    Virtual rabbit class.
    methods load_rabbits, save_rabbits, list_rabbits, create_rabbit, display_rabbit.
    """
    num_eyes = 2  # <- Class variables.
    num_legs = 4
    num_ears = 2
    num_tails = 1
    num_of_rabbits = 0
    rab_dic = dict([])
    obj_dic = {}
    def __init__(self, name='Rabbit', # <- Instance method.
                 fur_colour='unknown',
                 eye_colour='unknown',
                 sex='unsexed',
                 breed='unknown',
                 dob=None,
                 tob=None
                 ):

        self.name = name  # <- Instance variables.
        self.fur_colour = fur_colour
        self.eye_colour = eye_colour
        self.sex = sex
        self.breed = breed
        self.dob = dob
        self.tob = tob
        Rabbit.num_of_rabbits += 1

    @classmethod
    def load_rabbits(cls):
        """
        update dictionary rab_dic from csv file.
        create instances for each entry and
        update object dictionary rab_obj.
        """
        cls.rab_dic = csv_mod.rd_csv('rabbits.csv') # update dictionary from csv file.
        k = len(list(cls.rab_dic.keys())) # measure length of dictionary.
        for num in range(k): # loop through dictionary.
            r_v = list(cls.rab_dic[num].values()) # make list of dictionary values.
            r_0, r_1, r_2, r_3, r_4, r_5, r_6 = r_v # unpak values of dictionary.
            Rabbit.obj_dic[num] = Rabbit(r_0, r_1, r_2, r_3, r_4, r_5, r_6)
        return cls.rab_dic, Rabbit.obj_dic # return rabbit dictionary and object dictionary.

    @classmethod
    def save_rabbits(cls):
        """
        create and save CSV file from dictionary rab_dic.
        """
        csv_mod.wrt_csv('rabbits.csv', cls.rab_dic) # save rabbit dictionary as csv file.

    @classmethod
    def list_rabbits(cls):
        """
        list rabbits in dictionary rab_dic.
        """
        for key in cls.rab_dic:
            print("number of rabbit", key, "name", cls.rab_dic[key]['name'])

    @classmethod
    def create_rabbit(cls): # <- Class method.
        """
        create instance of rabbit class
        give date and time stamp.
        update dictionarys rab_dic and rab_obj.
        """
        l_n = len(cls.rab_dic)
        cls.rab_dic[l_n] = {}
        now = datetime.now()
        dic_keys = ('name', 'fur_colour', 'eye_colour', 'sex', 'breed')
        for key in dic_keys:
            cls.rab_dic[l_n][key] = input(key+' >')
        r_5 = cls.rab_dic[l_n]['dob'] = now.strftime("%d/%m/%Y")
        r_6 = cls.rab_dic[l_n]['tob'] = now.strftime("%X")
        r_0, r_1, r_2, r_3, r_4, r_5, r_6 = cls.rab_dic[l_n].values()
        _x = len(Rabbit.obj_dic)
        _t = {}
        _t[_x] = cls(r_0, r_1, r_2, r_3, r_4, r_5, r_6)
        Rabbit.obj_dic.setdefault(_x, _t[_x])

    def display_rabbit(self): # <- Regular method.
        """
        display formated instance of rabbit object.
        """
        return ("\n{0.name} is a {0.sex} rabbit"
                " and has {0.fur_colour} fur and "
                "{0.eye_colour} eyes, {0.name} is "
                "of the {0.breed} breed of rabbits.\n"
                "{0.name}'s DOB is {0.dob} at {0.tob}\n").format(self)
################################################.
