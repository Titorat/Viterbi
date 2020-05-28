

# This function extracts the unique lists of states(It was for debugging purposes but I kept it. )
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    return unique_list
tempo = []

#This function takes the path for sets and set the not maximum states to X which is then used in the backtracing
#function
def pre_processing(path):
    print(path)
    limit = len(path['s1']) -1

    L1 = path['s1']
    L2 = path['s2']
    L3 = path['s3']

    M1 = L1[limit][0][0]
    M2 = L2[limit][0][0]
    M3 = L3[limit][0][0]
    
    Ms = list([(M1,'M1'),(M2,'M2'),(M3,'M3')])
    sorted_Ms = sorted(Ms)
    
    sorted_Ms.reverse()
    maxprob_Ms = []
    temp = 0

    for j in sorted_Ms:
        if j[0] >= temp:
            temp = j[0]
        else:
            if j[1] == 'M1':
                L1[limit] = 'X'
            elif j[1] == 'M2':
                L2[limit] = 'X'
            elif j[1] == 'M3': 
                L3[limit] = 'X'
    print([L1,L2,L3],limit)
    return back_tracking([L1,L2,L3],limit)

# This funciton backtraces the maximum paths of states
def back_tracking(lists,temp_str = '',counter_rec = 0):
    counter = counter_rec + 1
    level = len(lists[0])
    limit = level-1
    
    for c,i in enumerate(lists):
        # condition to stop recursion
        if lists == [['X'], ['X'], ['X']]:  
            print(temp_str)
            print('_____')
            tempo.append(temp_str[3:])
            return
        
        # initialize state of the maximum state in the last row
        if counter == 1:
            if c == 0:
                
                temp_str = 's1'
            elif c == 1:
                temp_str = 's2' 
            else:
                temp_str = 's3' 
        try:
            if i[limit]  == 'X':
                continue
        except:
            pass
        
                
        else:
            # if conditions to start the backtracing based on the found state in the path
            print('i[limit]')
            print(i[limit])

            j = i[limit][0]

            print()
            print(j)
            print()
            if j[1] == 's1':
                
                A = list(lists[1][:limit-1])
                A.append('X')
                B = list(lists[2][:limit-1])
                B.append('X')
                if level > 1:
                    back_tracking([lists[0][:limit],A,B],temp_str = j[1]+ ','+ temp_str,counter_rec=counter)
                else:
                    C = list(lists[0][:limit-1])
                    C.append('X')
                    back_tracking([C,A,B],temp_str = j[1]+ ','+ temp_str,counter_rec=counter)

                
                
            elif j[1] == 's2':
                A = list(lists[0][:limit-1])
                A.append('X')
                B = list(lists[2][:limit-1])
                B.append('X')
                if level > 1:
                    back_tracking([A,lists[1][:limit],B],temp_str = j[1]+ ','+temp_str,counter_rec=counter)
                else:
                    C = list(lists[1][:limit-1])
                    C.append('X')
                    back_tracking([C,A,B],temp_str = j[1]+ ','+ temp_str,counter_rec=counter)
            elif j[1] == 's3':
                A = list(lists[0][:limit-1])
                A.append('X')
                B = list(lists[1][:limit-1])
                B.append('X')
                if level > 1:
                    back_tracking([A,B,lists[2][:limit]],temp_str = j[1]+ ','+temp_str,counter_rec=counter)
                else:
                    C = list(lists[2][:limit-1])
                    C.append('X')
                    back_tracking([A,B,C],temp_str = j[1]+ ','+ temp_str,counter_rec=counter)
                 
    return (tempo)



def Viterbi(DNA,states,init_prob,trans_prob,emiss_prob):
    path = { s:[] for s in states} 
    curr_prob = {}
    # This for loop initializes the states
    for s in states:
        curr_prob[s] = init_prob[s]*emiss_prob['e'+s[1]+DNA[0]]
        
        
        
        path[s].append([(curr_prob[s],s)])
    
    # This for loop continue to build the path after the first initialization
    for i in range(1,len(DNA)):
        last_prob = curr_prob
        curr_prob = {}
        
        
        # c_s is for the current state
        # l_s is for the changing last state
        for c_s in states:
            X = []
            for last_state in states:
                Y = (last_prob[last_state]*trans_prob['P'+last_state[1]+c_s[1]]*emiss_prob['e'+c_s[1]+DNA[i]], last_state)
                X.append(Y)
            
            maxprob_list=[]
            sorted_list = sorted(list(X))
            sorted_list.reverse()
            temp = 0
            for j in list(sorted_list):
                if j[0] >= temp:
                    temp = j[0]
                    maxprob_list.append((j[0],j[1]))
                else:
                    continue
            curr_prob[c_s] = maxprob_list[0][0]
            path[c_s].append((maxprob_list))
            

                
                
    return pre_processing(path)



# The initial states and preprocessing the input
states = ('s1','s2','s3')
init_prob = input()
trans_prob = input()
emiss_prob = input()
DNA = input()

init_prob = list(map(float, init_prob.split(',')))
init_prob = {
    's1' : init_prob[0],
    's2' : init_prob[1],
    's3' : init_prob[2],
}


trans_prob = list(map(float, trans_prob.split(',')))


trans_prob = {
    'P11' : trans_prob[0],
    'P12' : trans_prob[1],
    'P13' : trans_prob[2],
    'P21' : trans_prob[3],
    'P22' : trans_prob[4],
    'P23' : trans_prob[5],
    'P31' : trans_prob[6],
    'P32' : trans_prob[7],
    'P33' : trans_prob[8],
   }


emiss_prob = list(map(float, emiss_prob.split(',')))

emiss_prob = {
    'e1A' : emiss_prob[0],
    'e1C' : emiss_prob[1],
    'e1G' : emiss_prob[2],
    'e1T' : emiss_prob[3],
    'e2A' : emiss_prob[4],
    'e2C' : emiss_prob[5],
    'e2G' : emiss_prob[6],
    'e2T' : emiss_prob[7],
    'e3A' : emiss_prob[8],
    'e3C' : emiss_prob[9],
    'e3G' : emiss_prob[10],
    'e3T' : emiss_prob[11],

   }


results = Viterbi(DNA,states,init_prob,trans_prob,emiss_prob)

z = results[0].split(',')
print(' '.join(z))
'''
0.1,0,0.9
0.3,0.2,0.5,0.4,0.6,0,0.1,0,0.9
0.2,0.3,0.3,0.2,0.25,0.25,0.3,0.2,0.25,0.25,0.25,0.25
AGG
s3 s3 s3
'''