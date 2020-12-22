import manageDB

{
    'name' : 'unsik',
    'id' : '132',
    'creator' : 'unsik',
    'auth' : 'unsik',
    'popAttribute' :{
        'list' : {'성별':['남','여'], '연령':list(range(0,100))},
        'num' : 2,
        'cases' : 2
    },
    'startYear' : 1955,
    'baseYear' : 2018,
    'firstPop' : {'id':24, 'num':2},
    'inputPop' : {'data':[{'id':10, 'startYear':1953, 'endYear':2018}], 'num':1},
    'trainSet' : {'data':[{'id':11, 'startYear':2000, 'endYear':2018}], 'num':1},
    'testSet' : {'data':[{'id':12, 'startYear':1953, 'endYear':2018}], 'num':1},
    'outputPopModel' : {'data':[{'id':3,'sequence':0, 'condition':[{'성별':'남'}]},{'id':10,'sequence':1},{'id':42,'sequence':2}], 'num':3},
    'changePopAtModel' : {'data':[{'id':2,'sequence':0},{'id':23,'sequence':1},{'id':64,'sequence':2}], 'num':3},
    'classifyPopModel' : {'data':[{'id':4,'sequence':0},{'id':52,'sequence':1},{'id':76,'sequence':2}], 'num':3},
    'baseParameterSet' : {'data':[{'id':3, 'value':[]}], 'num':1}
}

class Basic:
    def __init__(self, creator):
        self.name = 'none'
        self.id = 0
        self.creator = creator
        self.auth = self.creator
        self.popAttribute = {
            'list' : [{'성별':['남','여']},{'연령':list(range(0,100))}],
            'num' : 2,
            'cases' : 2
        }
        self.startYear = 0
        self.baseYear = 0
        self.firstPop = {'id':Null}
        self.inputPop = {'data':[], 'num':0}
        self.trainSet = {'data':[], 'num':0}
        self.testSet = {'data':[], 'num':0}
        self.outputPopModel = []
        self.changePopAtModel = []
        self.classifyPopModel = []
        self.baseParameterSet = []
    
    def addPopAttribute()
    def insertFirstPop(self, id):
        self.firstPop['id'] = id
    
    def insertInputPop(self, id, startYear, endYear):
        self.inputPop['data'].append({'id':id, 'startYear':startYear, 'endYear':endYear})
        self.inputPop['num'] = len(self.inputPop['data'])
    
    def insertTrainSet(self, id, startYear, endYear):
        self.trainSet['data'].append({'id':id, 'startYear':startYear, 'endYear':endYear})
        self.trainSet['num'] = len(self.trainSet['data'])
    
    def insertTestSet(self, id, startYear, endYear):
        self.testSet['data'].append({'id':id, 'startYear':startYear, 'endYear':endYear})
        self.testSet['num'] = len(self.testSet['data'])

    def insertOutputPopModel(self, id, )
        self.outputPopModel['data'].append()