import csv

def read_csv_file(filename):
    """
    This function will open and read a csv file(sep=',')
    IN : name of the file to process
    OUT : list of list of strings: [["1","M","BALZAN","Thomas","thomas.balzan@ipsa.fr","ANG2"],..]
          ex for courses.csv : ["Mathematique","Aeronautique",...]
    """
    import os
    ##################################################
    #open and read file contents
    ##################################################
    data = []
    print("Current working directory : ", os.path.basename(os.path.abspath(os.curdir)))
    try :
        
        print("Open the file :",filename)

        # Loop over file rows to create list of list of strings
        with open(f'./data/{filename}',encoding = 'utf-8') as csvfile:
            rows = csv.reader(csvfile)
            for i in rows:
                data.append(i)
                
        if filename == "courses.csv":
            return data[0]
        return data
    
    except :
        print("1-Failed to open file for reading.")
        return


    return  data


def append_csv_file(contents, filename):
    """
    This function will open and write a csv file(sep=',')
    IN : contents to write in the file, name of csv file
    OUT : altered csv file
    """

 
    #try :
    with open(f'./data/{filename}', 'a', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
        
            # Write data to csv file
            writer.writerow(contents)

def write_csv_file(contents, filename):
    """
    This function will open and write a csv file(sep=',')
    IN : contents to write in the file, name of csv file
    OUT : 
    """


    try :
        with open(f'./data/{filename}', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
        
            # Write data to csv file
            for row in contents:

                writer.writerow(row)
    except :
        print("2-Failed to open file for writing.")
        return