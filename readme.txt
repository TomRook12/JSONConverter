#JSON Reader for Concept2 Erg race data files

AIM:
Read a JSON File created by the Concept2 erg race data files and export them to CSV,

Problem:
The JSON file contains alot of data, whilst useful this data is not required to produce results. Excel does not easily read these files as you would hope, the information is stored in nested dictionaries and would be easily accesible by a simple python programme.

V1:
The program can read and test one JSON file at a time
Can process set fields to  simplify and clean the data
Can output a CSV file for the read JSON file

V2:
Make this work with kivy
