from math import sqrt

class utilsDB:
    def getPoints(self,result):
        
        def getCenter(lst):
            pointOne = lst[0]
            pointTwo = lst[2]
            
            x,y = (round((pointOne[0] + pointTwo[0])/2,2),round((pointOne[1] + pointTwo[1])/2,2))
            
            return [x,y]
    
        def getDistanceOfTwoPoint(pointOne, pointTwo):
            difX = (pointTwo[0] - pointOne[0]) ** 2
            difY = (pointTwo[1] - pointOne[1]) ** 2
            res = difX + difY
            res = sqrt(res)
            return round(res,2)
        
        lst = []
        target = 0
        for x in range(len(result)):
            lst.append(getCenter(result[x][0]))
            if result[x][1] == 'Distance':
                target = x
        targetPoint = lst[target]
        dic = {}
        for x in range(len(lst)):
            dic[getDistanceOfTwoPoint(lst[x],targetPoint)] = x
        del dic[0.0]
        val = dic[min(dic.keys())]
        
        print(f'this is res: {result[val][1]}')
        return result[val][1]
        
        

    


    
    def convertMetric(self, var):
        meterVar = list(var)
        print(meterVar)
        num = ''
        metric = ''
        for x in var:
            if x.isnumeric() or x == '.':
                num += x
            if x.isalpha():
                metric += x
        if metric == 'mi':
            return [num, 'miles']
        else:
            return [round(int(num)/1610,2),'miles']
    

        
    
#    def getPoints(self,result):
        """
            #distance_index = lst.index('Distance')
            #shortLst = lst[distance_index:]
            #return shortLst[int(len(shortLst)/2)]
            if 'Achievements' in result:
                achi = result.index('Achievements')
                last_index = achi + 5
                newResult = result[:last_index]
                #print(newResult)
                dic = zip(newResult[-8:-4],newResult[-4:])
                dic = dict(dic)
            else:
                dic = zip(result[-6:-3],result[-3:])
                dic = dict(dic)
                
            return dic['Distance']
        
        lst = []
        target = 0
        for x in range(len(result)):
            lst.append(getCenter(result[x][0]))
            if result[x][1] == 'Distance':
                target = x
        """
        
