import numpy as np

class classify:
    def model1(tunSet):
        rate = tunSet[0]
        start = tunSet[1]
        end = tunSet[2]
        npData = np.zeros(100)
    
        for i in range(st,end):
            npData[i] = (rate**(i-end))-1  
            
        sumValue = np.sum(npData)
        npRateData = npData / sumValue
        return npRateData

    def model2(tunSet):
        npData = np.zeros(100)
        start = tunSet[0]
        end = tunSet[1]
        head = tunSet[2]
        height = tunSet[3]

        for i in range(start,end+1):
            if i>head:
                a1 = height**(1/(-1*(end-head)))
                gx = a1**(i-end)-1
                npData[i] = gx
            elif i<=head:
                a2 = height**(1/(head-0))
                fx = a2**(i-0)-1
                npData[i] = fx

        sumValue = np.sum(npData)
        npRateData = npData / sumValue
            
        return npRateData

class probability:
    def model1(tunSet, year):
        valueList = np.zeros([100])
        c = ((tuningSet[0]**(100-tuningSet[1]))-1)

        for i in range(100):
            result1 = ((tuningSet[0]**(i-tuningSet[1]))-1)*tuningSet[2]*(1+(tuningSet[3]/1000000*(year+1950)-tuningSet[4]))/c
            valueList[i] = 0 if result1<0 else 1 if result1>1 else result1

        npRateData = np.around(npData*valueList)

        return npRateData

