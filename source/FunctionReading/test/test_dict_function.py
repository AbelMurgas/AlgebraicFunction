from source.FunctionReading.function_reading import AlgebraicFunctionReading as afr

def test_error_symbol():
    try:
        afr(list_function={'-':2})
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_error_str_number():
    try:
        afr(list_function={'x':'2'})
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_error_list_max():
    try: # no pass
        afr(list_function={'x6':3,'x4':4})
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_error_list_min():
    try: # no pass
        afr(list_function={})
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_error_values_empty():
    try: # no pass
        afr(list_function={'x2':' ','x':2})
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_pass_list_min():
    try: # no pass
        afr(list_function={'x':1})
        fail = False
    except:
        fail = True
    assert fail == False
        
def test_pass_list_max():
    try:
        afr(list_function={'x5':1,'x4':1,'x3':4,'x2':-2,'x':1,'c':2})
        fail = False
    except:
        fail = True
    assert fail == False