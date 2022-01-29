from source.FunctionReadingX.Function_Reading import AlgebraicFunctionReading as afr

def test_validate_arg_error():
    try:
        afr(2,3,"k")
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_validate_kwarg_error():
    try:
        afr(nothing="y=23x-2")
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_validate_both_use_error():
    try:
        afr(2,str_function="y=23x-2")
        fail = False
    except:
        fail = True
    assert fail == True
        
def test_validate_multiply_kwarg_error():
    try:
        afr(dict={'y':2,'x':3},str_function="y=23x-2")
        fail = False
    except:
        fail = True
    assert fail == True
        
