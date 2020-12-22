import pymongo
from pymongo import MongoClient

def connectDB(collection):
    client = MongoClient('222.239.90.78:47017',
                         username='panpAdmin',
                         password='asd123!',
                         authSource='PANP',
                         authMechanism='SCRAM-SHA-256')
    return client['PANP'][collection]

class Project:
    def create(prjData):
        colPrj = connectDB('Project')
        colDI = connectDB('DataInfo')
        dataCount = colDI.find({'Type':'DataCount'},{'_id':0})[0]
        prjAttribute = {
            'name' : prjData.name,
            'id' : dataCount['ProjectCount'],
            'creator' : prjData.creator,
            'auth' : prjData.auth,
            'popAttribute' :prjData.popAttribute,
            'startYear' : prjData.startYear,
            'baseYear' : prjData.baseYear,
            'firstPop' : prjData.firstPop,
            'inputPop' : prjData.inputPop,
            'trainSet' : prjData.trainSet,
            'testSet' : prjData.testSet,
            'outputPopModel' : prjData.outputPopModel,
            'changePopAtModel' : prjData.changePopAtModel,
            'classifyPopModel' : prjData.classifyPopModel,
            'baseParameterSet' : prjData.baseParameterSet
        }
        dataCount['ProjectCount'] += 1
        colDI.update({'Type':'DataCount'}, dataCount, True)
        state = colPrj.update(prjAttribute, prjAttribute, True)
        
        return state
    
    def read(prjId):
        collection = connectDB('Project')
        data = collection.find({'id':prjId},{'_id':0})[0]
        return data
    
    def update(prjData):
        collection = connectDB('Project')
        prjAttribute = {
            'name' : prjData.name,
            'id' : prjData.id,
            'creator' : prjData.creator,
            'auth' : prjData.auth,
            'popAttribute' :prjData.popAttribute,
            'startYear' : prjData.startYear,
            'baseYear' : prjData.baseYear,
            'firstPop' : prjData.firstPop,
            'inputPop' : prjData.inputPop,
            'trainSet' : prjData.trainSet,
            'testSet' : prjData.testSet,
            'outputPopModel' : prjData.outputPopModel,
            'changePopAtModel' : prjData.changePopAtModel,
            'classifyPopModel' : prjData.classifyPopModel,
            'baseParameterSet' : prjData.baseParameterSet
        }
        
        state = collection.update({'id':prjData.id}, prjAttribute, True)
        return state
    
    def delete(prjId):
        collection = connectDB('Project')
        state = collection.remove({'id':prjId})
        return state


class DataTable:
    def create(dfData, dataName, creator, dataType):
        colDT = connectDB('DataTable')
        colDI = connectDB('DataInfo')
        dataCount = colDI.find({'Type':'DataCount'},{'_id':0})[0]
        dataTable = {
            'name' : dataName,
            'id' : dataCount['DataTableCount'],
            'creator' : creator,
            'auth' : creator,
            'type' : dataType,
            'data' : []
        }
        dataCount['DataTableCount'] += 1
        colDI.update({'Type':'DataCount'}, dataCount, True)
        
        dictData = dfData.T.to_dict()
        temp = []
        for i in range(len(dictData)):
            temp.append({str(key): str(value) for key, value in dictData[i].items()})
        dictData = temp
        for i in range(len(dfData)):
            dataTable['data'].append(dictData[i])
        state = colDT.update(dataTable, dataTable, True)
        return state
    
    def read(dataId):
        collection = connectDB('DataTable')
        data = collection.find({'id':dataId},{'_id':0})[0]
        return data
    
    def update(dataId, dfData, dataType):
        collection = connectDB('DataTable')
        dataTable = {
            'name' : '',
            'id' : 0,
            'creator' : 'unsik',
            'auth' : 'unsik',
            'type' : dataType,
            'data' : [{'row':0, 'column':0, 'value':0}]   
        }
        state = collection.update({'id':dataId}, dataTable, True)
        return state
    
    def delete(dataId):
        collection = connectDB('DataTable')
        state = collection.remove({'id':dataId})
        return state