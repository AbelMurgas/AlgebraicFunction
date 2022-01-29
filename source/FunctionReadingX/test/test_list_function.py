from source.FunctionReadingX.Function_Reading import AlgebraicFunctionReading as afr

def test_error_symbol():
    try:
        afr(list_function=[2,2.5,-2,'/'])
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_error_str_number():
    try:
        afr(list_function=['2.2','2'])
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_error_list_max():
    try: # no pass
        afr(list_function=[2,-1,2,4,5,0,10])
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_error_list_min():
    try: # no pass
        afr(list_function=[])
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_pass_list_min():
    try:
        afr(list_function=[2])
        fail = False
    except:
        fail = True
    assert fail == False
        
def test_pass_list_max():
    try:
        afr(list_function=[2,-1,2,4,5,0])
        fail = False
    except:
        fail = True
    assert fail == False