#define the load map function
def load_map(file_path):
    #open the file
    infile = open(file_path,"r")
    #create the adjacent room dictionary
    adjacent_rooms = {}
    #go line by line
    for line in infile:
        #strip \n from the line
        line = line.strip()
        #split the line to get the key
        line = line.split(": ")
        #split the second half of the line to get a list of adjacent rooms
        line[1] = line[1].split(", ")
        #update the dictionary with the key and list of adjacent rooms as the value
        adjacent_rooms.update({line[0]:line[1]})
    #close the file
    infile.close()
    #return the adjacent rooms dictionary
    return(adjacent_rooms)

#define the simplify testimonry function
def simplify_testimony(chat,rooms):
    #define the possible colours
    colour = ["red", "blue", "green", "yellow", "brown", "pink", "orange"]
    #take the chat line and get rid of the commas
    chat = chat.replace(",","")
    #strip the chat line of the characters below
    chat = chat.strip(",\n.?")
    #create the simplified chat that we are going to return
    simplified_chat = ""
    #see if it is a statement or a vote
    if ":" in chat:
        #if it is a statement split the line into the speaker and the statement
        chat = chat.split(": ")
        #for each key in the adjacent room dictionary
        for key in rooms:
            #see if the room is in the statement
            if key in chat[1]:
                #create colours seen variable that we will use to create our simplified chat
                colour_seen = "none"
                #iterate through the colour list
                for i in range(len(colour)):
                    #check if the colour is in the statement
                    if colour[i] in chat[1]:
                        #set colour seen to the colour mentioned if there is one
                        colour_seen = colour[i]
                #if there is no colour seen we assume they are talking about themself
                if colour_seen != "none":
                    #create the simplified statement
                    simplified_chat = chat[0]+":",colour_seen,"in",key
                    #join the list together to create a string
                    simplified_chat =" ".join(simplified_chat) 
                #if there was a colour add it to the statement
                else:
                    #create the simplified statement
                    simplified_chat = chat[0]+":",chat[0],"in",key
                    #join the list together to create a string
                    simplified_chat =" ".join(simplified_chat)
    #if the statement is a vote
    elif "voted" in chat:
        #split the string into a list
        chat = chat.split(" ")
        #create our simplified chat
        simplified_chat = chat[0],"voted",chat[2]
        #join the list together to create a string
        simplified_chat =" ".join(simplified_chat)
    #return our simplified chat
    return simplified_chat

#create load chat log function
def load_chat_log(filename,rooms):
    #open file
    infile = open (filename,"r")
    #create chat log list
    chat_log = []
    #go through each line
    for line in infile:
        #get the simplified line
        simple_line = simplify_testimony(line, rooms)
        #see if returned value is an empty string
        if simple_line != "":
            #if not empty, append the simple line to the chat log list
            chat_log.append(simple_line)
    #close the file
    infile.close()
    #return the chat log function
    return chat_log
#define the tally vote function
def tally_votes(chat_log):
    #create our vote dictionary
    vote_dict = {
        "red":0,
        "blue":0,
        "green":0,
        "yellow":0,
        "brown":0,
        "pink":0,
        "orange":0,
        "skip": 0
    }
    #go through the chat log list
    for i in range(len(chat_log)):
        #see if the statement contains voted or not
        if "voted" in chat_log[i]:
            #split the statement
            split_line = chat_log[i].split(" ")
            #go colour by colour to tally votes
            for key in vote_dict:
                #check which colour is voted
                if split_line[2] == key:
                    #add to the tally
                    vote_dict[key] += 1
    #return the vote dictionary
    return vote_dict
#define the get paths function
def get_paths(chat_log):
    #create the path dictionary
    path_dict = {
        "red":[],
        "blue":[],
        "green":[],
        "yellow":[],
        "brown":[],
        "pink":[],
        "orange":[]
    }

    #iterate through the chat log
    for i in range(len(chat_log)):
        #split the chat log
        chat_log[i] = chat_log[i].split(" ")
        #strip the key of the colon
        chat_log[i][0] = chat_log[i][0].strip(":")
        #check if it is a self testimony
        if "in" in chat_log[i][2] and chat_log[i][0] == chat_log[i][1]:
            #go through each colour
            for key in path_dict:
                #if the speaker is equal to the key
                if chat_log[i][1] == key:
                    #create the location list
                    location = []
                    #check all the values after the in as that is the location
                    for j in range(3,(len(chat_log[i]))):
                        #append the list
                        location.append(chat_log[i][j])
                    #join the location list together
                    location = " ".join(location)
                    #append the location to the dictionary 
                    path_dict[key].append(location)
    #return the path dictionary
    return path_dict

#define the get sus path function
def get_sus_paths(path_dict,rooms):
    #suspect list
    sus_list = []
    #check through each colour
    for key in path_dict:
        #create a counter to see how many instances of lying there are
        sus_counter = 0
        #iterate through the list
        for i in range (len(path_dict[key])-1):
            #check if the next location in the adjacent room list
            if path_dict[key][i+1] in rooms[path_dict[key][i]]:
                #if true the return nothing
                pass
            else:
                #update the suspect counter
                sus_counter += 1
        #if the suspect counter is greater then 0
        if sus_counter > 0:
            #append the colour to the suspect list
            sus_list.append(key)
    #return the suspect list
    return sus_list

#define main
def main():
    #get map name
    map_name = input("Please enter the the map that you are playing on: ")
    #create filename
    filename = map_name+".txt"
    #get our simplified map
    simplified_map =load_map(filename)
    simplified_chat = load_chat_log("chatlog.txt",simplified_map)
    #call tally votes function
    tally_votes(simplified_chat)
    #cakk get sus paths function
    get_sus_paths(get_paths(simplified_chat),simplified_map)

#call main function
if __name__ == "__main__":
    main()
