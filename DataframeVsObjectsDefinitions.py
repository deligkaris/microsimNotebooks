import pandas as pd
import numpy as np

from microsim.cohort_risk_model_repository import CohortRiskModelRepository
from microsim.alcohol_category import AlcoholCategory

class simplePerson:
    def __init__(self):
        for j in range(21):
            setattr(self, f"random{j}", np.random.uniform(size=20).tolist())

def meanOfList(x):
    return x["random"].apply(np.mean)

def meanOfListNTimes(x):
    for i in range(100):
        a = x["random"].apply(np.mean)
    return a

def meanOfListOb(x):
    setattr(x, "randomMean", np.mean(x.random))
    return x

def meanOfListObP(x):
    list(map(lambda y: setattr(y, "randomMean", np.mean(y.random)), x)) 
    return x

def meanOfListObPNTimes(x):
    for i in range(100):
        list(map(lambda y: setattr(y, "randomMean", np.mean(y.random)), x))
    return x     

def doNothingReturnArg(x):
    return x

def doNothingReturn0(x):
    return 0

def meanOfColumns(x):
    return pd.DataFrame.apply(x[[f"random{j}" for j in range(0,20)]],np.mean, axis=1)

def meanOfColumnsOb(x):
    setattr(x, "randomMean", np.mean([getattr(x, f"random{j}") for j in range(0,20)] ))         
    return x

def meanOfColumnsUsingPandas(x):
    return x[[f"random{j}" for j in range(0,20)]].mean(axis=1)

def advanceRiskFactors(x):

    rngStream = np.random.default_rng()

    rfs = ['sbp', 'dbp', 'a1c', 'hdl', 'ldl', 'trig', 'totChol', 'bmi', 'anyPhysicalActivity', 'afib', 'waist', 'alcoholPerWeek', 'creatinine']
    for rf in rfs:
        model = CohortRiskModelRepository().get_model(rf)
        riskFactorsDict = {}
        riskFactorsDict[rf + "Next"] = pd.DataFrame.apply(x, 
                                                      model.estimate_next_risk_vectorized,
                                                      axis="columns",
                                                      rng=rngStream)
    x = pd.concat([x.reset_index(drop=True), 
                       pd.DataFrame(riskFactorsDict).reset_index(drop=True)], 
                       axis='columns', ignore_index=False)

    return x

def advanceRiskFactorsOb(x, risk_model_repository, rng=None):

    x._sbp.append(
            x.apply_bounds("sbp", x.get_next_risk_factor("sbp", risk_model_repository, rng=rng))
        )

    x._dbp.append(
            x.apply_bounds("dbp", x.get_next_risk_factor("dbp", risk_model_repository, rng=rng))
        )
    x._a1c.append(x.get_next_risk_factor("a1c", risk_model_repository, rng=rng))
    x._hdl.append(x.get_next_risk_factor("hdl", risk_model_repository, rng=rng))
    x._totChol.append(x.get_next_risk_factor("totChol", risk_model_repository, rng=rng))
    x._bmi.append(x.get_next_risk_factor("bmi", risk_model_repository, rng=rng))
    x._ldl.append(x.get_next_risk_factor("ldl", risk_model_repository, rng=rng))
    x._trig.append(x.get_next_risk_factor("trig", risk_model_repository, rng=rng))
    x._waist.append(x.get_next_risk_factor("waist", risk_model_repository, rng=rng))
    x._anyPhysicalActivity.append(
            x.get_next_risk_factor("anyPhysicalActivity", risk_model_repository, rng=rng)
        )
    x._afib.append(x.get_next_risk_factor("afib", risk_model_repository, rng=rng))
    x._creatinine.append(x.get_next_risk_factor("creatinine", risk_model_repository, rng=rng))
    x._alcoholPerWeek.append(
            AlcoholCategory.get_category_for_consumption(
                x.get_next_risk_factor("alcoholPerWeek", risk_model_repository, rng=rng)
            )
        )

    return x

def advanceRiskFactorsObP(x):

    rngStream = np.random.default_rng()
    modelRepo = CohortRiskModelRepository()

    list(map( lambda y: advanceRiskFactorsOb(y, modelRepo, rngStream), x)) 

    return x
    
def advanceRiskFactorsObP2(x):

    rngStream = np.random.default_rng()
    modelRepo = CohortRiskModelRepository()
    models = {'sbp': modelRepo.get_model('sbp'), 
              'dbp': modelRepo.get_model('dbp'), 
              'a1c': modelRepo.get_model('a1c'),
              'hdl': modelRepo.get_model('hdl'), 
              'ldl': modelRepo.get_model('ldl'), 
              'trig': modelRepo.get_model('trig'),
              'totChol': modelRepo.get_model('totChol'),
              'bmi': modelRepo.get_model('bmi'), 
              'anyPhysicalActivity': modelRepo.get_model('anyPhysicalActivity'),
              'afib': modelRepo.get_model('afib'),
              'waist': modelRepo.get_model('waist'), 
              'alcoholPerWeek': modelRepo.get_model('alcoholPerWeek'), 
              'creatinine': modelRepo.get_model('creatinine')}

    list(map( lambda y: advanceRiskFactorsOb2(y, models, rngStream), x))

    return x

def advanceRiskFactorsOb2(x, models, rng=None):

    x._sbp.append(
            x.apply_bounds("sbp", models["sbp"].estimate_next_risk(x, rng=rng)))

    x._dbp.append(
            x.apply_bounds("dbp", models["dbp"].estimate_next_risk(x, rng=rng))
        )
    x._a1c.append(
            models["a1c"].estimate_next_risk(x, rng=rng))
    x._hdl.append(
            models["hdl"].estimate_next_risk(x, rng=rng))
    x._totChol.append(
            models["totChol"].estimate_next_risk(x, rng=rng))
    x._bmi.append(
            models["bmi"].estimate_next_risk(x, rng=rng))
    x._ldl.append(
            models["ldl"].estimate_next_risk(x, rng=rng))
    x._trig.append(
            models["trig"].estimate_next_risk(x, rng=rng))
    x._waist.append(
            models["waist"].estimate_next_risk(x, rng=rng))
    x._anyPhysicalActivity.append(
            models["anyPhysicalActivity"].estimate_next_risk(x, rng=rng))
    x._afib.append(
            models["afib"].estimate_next_risk(x, rng=rng))
    x._creatinine.append(
            models["creatinine"].estimate_next_risk(x, rng=rng))
    x._alcoholPerWeek.append(
            AlcoholCategory.get_category_for_consumption(
                models["alcoholPerWeek"].estimate_next_risk(x, rng=rng))
            )

    return x





