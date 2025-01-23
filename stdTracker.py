#!/usr/bin/env python3
#ss will be replaced with the file, this class sorts all of the information in the std document into relevant dictionaries
def file_view(ss):  
    '''
    This module is designed to take in an existing STD database and return 
    three key value pair dictionary each one with the disease as the key 
    and the value variaing from the symptoms, the location on the body
    and a link to more information on the disease.
    '''
    #opens file
    fileRead = open(ss, "r") 
    info = ''
    symptoms = {}
    location = {}
    more = {}
    key = ''
    value = ''
    #puts the values into dictionaries that consist of the symptoms, location, and more information
    
    for line in fileRead:
        line = line.lower()
        line = line.split(':')
        symptoms[line[0]] = line[1]
        location[line[0]] = line[2]
        more[line[0]] = line[3]
    return symptoms, location, more

def Symptoms(symptoms, isymptoms): 
    '''
    this module cross references all of the symptoms the patient is feeling with
    possible symptoms of diseases and returns the possible diseases. 
    '''
    #list of possible diseases based on the syptoms
    pdisease = []
    #isymptoms is a list of the different symptoms the person is feeling
    for i in isymptoms:     
        for j in symptoms:
            if i in symptoms.get(j):
                pdisease.append(j)
    return pdisease

def Location(location, ilocation):
    '''
    this module cross references all of the locations the person feels the disease with the possible 
    locations diseases could be present on the body.
    '''
    #list of possible diseases for the  location
    pdisease = []
    #ilocation is a list of the different locations the person is feeling pain    
    for j in ilocation:     
        for i in location:
            if j in i:
                pdisease.append(i)
    return pdisease


def main():
    '''
    This function serves as the one that brings the rest togethor and it tests combines lthe result
    of the Symptoms and Location functions together, as well as calls upon the file_view function to 
    sort through the STD database
    '''
    while True:
        # the user inputs all of the symptoms they are feeling
        temp = 0
        isymptoms = []
        while temp == 0:
            cat =  input("Hello click e to end or, please list all symptoms that you are feeling, write them in one by one and press enter between ")
            if cat == 'e':
                temp = 1
            else:
                isymptoms.append(cat)
        
        # the user inputs where they are feeling those symptoms
        temp = 0
        ilocation = []
        while temp == 0:
            cat =  input("Hello click e to end or, please list all locations that you are feeling symptoms, write them in one by one and press enter between ")
            if cat == 'e':
                temp = 1
            else:
                ilocation.append(cat)
        #calles on the first function and parses the infomration on the database
        symptoms, location, more = file_view("STD.txt")
        pdiseaseS = Symptoms(symptoms, isymptoms)
        #this calles the two other functions, Symtoms and Locations and cross references the possible disease based on the symptoms and locations
        if len(ilocation) > 1:
            pdiseaseL = Location(location, ilocation)
            common_list = set(pdiseaseS).intersection(pdiseaseL)
            print("\n Your possible diseases are:")
            for i in common_list:
                print('\n'+i + more.get(i))
        else: 
            print("\n Your ppossible diseases are: ")
            for i in pdiseaseS:
                print('\n' + i + more.get(i))
                
        ext = input("Type e to exit or click enter to continue ")
        if ext == 'e':
            return
main()
