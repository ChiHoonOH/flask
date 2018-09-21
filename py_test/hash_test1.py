def solution(participant, completion):
    if((len(completion)==len(participant)-1) and (1<=len(completion)<=100000)):
        participant_dict={}
        for part in participant:
            
            element = participant_dict.get(part)
            if element == None:
                participant_dict[part] = 1
            else:
                participant_dict[part] += 1
        
        return participant_dict

print(solution(['멍','하하','하하'],['민규','가은']))
    