from indexa.core import *
def test_rank(): assert rank('python rag',[Evidence('a','python rag',.5),Evidence('b','sql',1)])[0].source_id=='a'
