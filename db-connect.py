import numpy as np
import pandas as pd
import scipy
from sqlalchemy import create_engine
from sqlalchemy.exc import ResourceClosedError

def RecSysConnect(schema='recsys'):
    conn_str = "mysql+pymysql://recsys:RecommenderSystems2017@localhost/{schema}?charset=utf8&use_unicode=1".format(schema=schema)
    engine = create_engine(conn_str, pool_recycle=1800)
    return engine

#e = RecSysConnect()