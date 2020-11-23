
def mostVisitedNode(N, L):
    '''
    Parameters:
    N =  number of nodes in the circular array (int)
    L = nodes visited ( List[int] )
    -------------
    Returns :
    the node that was visited the most
    '''
    base_list = list(range(1,N+1))
    # N = 10 ---> base_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    path = []
    counts = [0]*N
    
    for i in range(len(L)-1):
        start = L[i]
        end = L[i+1]

        # First pass, include the start node
        if i == 0:
            if start > end:
                cur_path = base_list[start-1:]+ base_list[:end]
            else:
                cur_path = base_list[start-1:end]
            path += cur_path
        # All proceeding paths, exclude the start node
        else:
            if start >= end:
                cur_path = base_list[start:]+ base_list[:end]
            else:
                cur_path = base_list[start:end]
            path += cur_path
        
     #        L[0]-->L[1]-------------------->L[2] ------------------------>L[3]        
     # path = [3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
    
    for i in path:
        counts[i-1] += 1
    max_index = 0
    max_so_far = 0
    for i in range(len(counts)):
        if counts[i] >= max_so_far:
            max_so_far = counts[i]
            max_index = i + 1
    return max_index
if __name__ == '__main__':
    N = 10
    L = [3,5,3,3]
    print(mostVisitedNode(N,L))
    
