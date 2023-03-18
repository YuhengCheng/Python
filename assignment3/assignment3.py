
#define the read motion function
def read_motion(location_name):
    #get the filename
    filename = location_name + ".motion.txt"
    #open the file in read
    infile = open (filename,"r")
    #create our motion list
    motion_check =[]
    #read the file line by line
    for line in infile:
        #strip the line of \n
        line = line.strip()
        #split the elements in each line
        split_line = line.split(",")
        #check if motion is detected
        if "detected" in split_line:
            #see if the the room is already in the list
            if split_line[0] in motion_check:
                #if it is pass
                pass
            #append to our list if location is not in list
            else:
                motion_check.append(split_line[0])
    #close the file
    infile.close()
    #return the motion list
    return motion_check

#define read emf function
def read_emf(location_name):
    #get file name
    filename = location_name + ".emf.txt"
    #open file in read
    infile = open (filename,"r")
    #create list that we will return
    abnormal_emf = []
    #create list that we will manipulate 
    emf_check = []
    #our counter for index
    emf_check_index = 0
    #read the file line by line
    for line in infile:
        #strip the line of \n
        line = line.strip()
        #check if the the line is a positive integer
        if line.isdigit():
            #if true then add it to the total and increase our counter which keeps track of values
            emf_check[emf_check_index-1][1] += int(line)
            emf_check[emf_check_index-1][2] +=1
        else:
            #else append a list with the room name, a sum and a # of values to calculate average
            emf_check.append([line,0,0])
            #increase our index counter
            emf_check_index += 1
    #close file
    infile.close()       
    #check room averages
    for i in range (len(emf_check)):
        #check if average is greater than 3
         if emf_check[i][1]/emf_check[i][2] > 3:
             #append room to the list that we will return
            abnormal_emf.append(emf_check[i][0])
    #return our abnormal emf room list
    return abnormal_emf
    
#define our valid temp function
def is_valid_temp(val):
    #strip our value of - and /n
    val = val.strip('-')
    #split our value so we can use isdigit()
    val =val.split(".")
    #see if first element in line is an int or not
    if val[0].isdigit():
        #return true if true
        return True
    #return false if not
    else:
        return False
#define read_temp fucntion
def read_temp(location_name):
    #get filename
    filename = location_name + ".temp.txt"
    #open file
    infile = open (filename,"r")
    #create list that we are going to return
    abnormal_temp = []
    #create list that we will manipulate in the function
    temp_check = []
    #create counter for indexing
    temp_index = 0
    #read line by line
    for line in infile:
        #strip line of /n
        line = line.strip()
        #call the valid_temp function to see if value is a temperature
        if is_valid_temp(line):
            #if the value is less than 0 
            if float(line) < 0:
                #add 1 to the counter which we sure to see # of consecutive negative temperatures
                temp_check[temp_index-1][1] +=1
            #if the value is greater than 0
            else:
                #reset our negative temp counter
                temp_check[temp_index-1][1] = 0
            #if there is 5 consecutive negative temperatures increase our abnormal indicator
            if temp_check[temp_index-1][1] == 5:
                temp_check[temp_index-1][2] +=1
        #if not a valid temperature
        else:  
            #append room list with line as index[0], a negative temp counter and an abnormal activity indicator
            temp_check.append([line,0,0])
            #increase the index counter by 1
            temp_index +=1
    #close file
    infile.close()
    #check each room to see if there is abnormal activity
    for i in range(temp_index-1):
        #check if our indicator counter is greater than 0
        if temp_check[i][2] >0:
            #append abnormal room to our return list if true
            abnormal_temp.append(temp_check[i][0])
    #return abnormal temperature activity list
    return abnormal_temp

#define generate_report function
def generate_report(location,motion,emf,temp):
    #get file name
    filename = "ghost_report."+location+".txt"
    #open file or create if it does not exist
    infile = open (filename, "w")
    #write title on txt file
    infile.write("==Raven Ghost Hunting Society Haunting Report==\n")
    #indicate location on txt file
    infile.write("Location: {0}\n".format(location))
    #check if there is any abnormal motions in rooms
    if len(motion) > 0:
        #if there is motion we check combinations to determine what monster it is
        for i in range(len(motion)):
            #all 3 we have poltergeist
            if motion[i] in emf and motion[i] in temp:
                infile.write("Poltergeist in{}\n".format(motion[i]))
            #motion emf we have oni
            elif motion[i] in emf:
                infile.write("Oni in {}\n".format(motion[i]))
            #motion and temp we have banshee
            elif motion[i] in temp:
                infile.write("Banshee in {}\n".format(motion[i]))
    #check if we have abnormal emf if we do not have motion
    elif len(emf) > 0:
        #check every instance of emf abnormality 
        for i in range(len(emf)):
            #see if there is abnormal temp in the same room
            if emf[i] in temp:
                #if temp and emf it is a phantom
                infile.write("Phantom in {}\n".format(emf[i]))
    
    #nothing happened means there was nothing
    else:
        infile.write("Nothing Supernatural")
    #close file from write
    infile.close()

#define main
def main():
    #get location
    location = input("Please enter the location that you are looking for info for: ")
    #call the generate report function
    generate_report(location,read_motion(location),read_emf(location),read_temp(location))

#call main function
if __name__ == "__main__":
    main()