#define cocktail sort
def cocktailsort(a):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(a)-2):
            #compare the 2 distances
            if a[i] > a[i+1]:
                #swap
                a[i],a[i+1] = a[i+1],a[i]
                swapped = True
        #break loop if done swapping
        if swapped == False:
            break
        #iterate backwards to see if the values are correct
        for i in range(len(a)-2, -1):
            #compare distances
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                swapped = True
    #return list of tuples
    return a
#create function to accept values
def closest_enemies(hero_position,enemy_positions):
    #iterate through all the values to calculate euclidian distances
    for i in range(len(enemy_positions)):
        enemy_positions[i]= (((enemy_positions[i][0]-hero_position[0])**2)+((enemy_positions[i][1]-hero_position[1])**2))**(1/2)
    #cocktail sort
    enemy_positions = cocktailsort(enemy_positions)
    #print the sorted distances
    print(enemy_positions)
#define main
def main():
    hero = (0,0)
    #2.8284271247461903,5.656854249492381,8.48528137423857
    enemy = [(4,4),(2,2),(6,6)]
    #0,4,6
    enemy = [(0,0),(0,6),(-4,0)]
    closest_enemies(hero,enemy)

#call main
if __name__ == "__main__":
    main()