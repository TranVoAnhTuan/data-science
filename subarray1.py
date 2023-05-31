# Ha Noi Tower
def ha_noi_tower(n, from_rod, to_rod, aux_rod): 
    if n == 1: 
        print("Move disk 1 from rod",from_rod,"to rod",to_rod) 
        return
    ha_noi_tower(n-1, from_rod, aux_rod, to_rod) 
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod) 
    ha_noi_tower(n-1, aux_rod, to_rod, from_rod) 
          
# Driver code 
n = 4 # Number of disks 
ha_noi_tower(n,'A','C','B') # A, B and C are the rods