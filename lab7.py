
def minmpg(): #function defined for finding user's minimum mpg
    while True:
        mpg = int(input('Enter the minimum mpg ==> ')) #asks user for minimum mpg
        if mpg <= 0: #minimum mpg can't be less than 0
            print('Fuel economy must be greater than 0')
        elif mpg > 100: #minimum mpg can't be greater than 100
            print('Fuel economy must be less than 100')
        elif mpg > 0 and mpg < 100: #if minimum mpg is 1-99, value is stored and returned for future reference
            return mpg
            break
        else:
            print('You must enter a number for the fuel economy') #any other input would be invalid
        print()
    
def userinputfile(): #function defined for asking user for the input file they would like to write/read from
    while True:
        try:
            print()
            filename1 = input('Enter the name of the input vehicle file ==> ') #asks user for the name of the input file they want to open
            f1 = open(filename1, 'w+')
            for line in f1:
                line.split('\t')
                lineread = f1.readline()
            print(lineread)
            f1.close()
            break
        
        except FileNotFoundError:
            print(f'Could not find file {filename1}')
        except IOError:
            print(f'Could not open file {filename1}')

            

'''def useroutputfile(): #function defined for asking user for the output file they would like to write/read to
    while True:
        try:
        print()
            filename2 = input('Enter the name of the file to output to ==> ') #asks user for the name of the output file they want to open
            f2 = open(filename2, 'w')
            for line in f2:
                line.split('\t)
                print(file)
            f2.close()
               
            

        except IOError:
            print(f'There is an IO error {filename2}')'''



print('Lab Week 7')
print()
minmpg()
userinputfile()
