from source.FunctionReading.function_reading import AlgebraicFunctionReading as afr

def test_error_symbol():
    try:
        afr(str_function="y=2x/4*")
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_error_symbol_repeat():
    try:
        afr(str_function="y=--3x++3:")
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_not_equal_symbol():
    try:
        afr(str_function="3x+3")
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_repeat_equal_symbol():
    try:
        afr(str_function="y=3=x+3")
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_error_use_symbol():
    try:
        afr(str_function="y=3x+3+")
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_error_degree_cero():
    try: # fix
        afr(str_function="y=32x2+3x0")
        fail = False
    except:
        fail = True
    assert fail == True

def test_error_degree_max():
    try: # fix
        afr(str_function="y=32x6+3x5-3x4+x")
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_error_format_variable():
    try: 
        afr(str_function="y=x4x3+3x5")
        fail = False
    except:
        fail = True
    assert fail == True
    
def test_pass_without_variable():
    try:
        afr(str_function="y=-3")
        fail = False
    except:
        fail = True
    assert fail == False
    
def test_pass_only_variable():
    try: 
        afr(str_function="y=-3x")
        fail = False
    except:
        fail = True
    assert fail == False
    
def test_pass_correct_format():
    try: #not pass
        afr(str_function="y=+2x5-2x4+x3-2x2+x+0")
        fail = False
    except:
        fail = True
    assert fail == False
    
def test_error_double_variabel():
    try: #not pass
        afr(str_function="y=+2xx5-2x")
        fail = False
    except:
        fail = True
    assert fail == False
    
def test_fix_cero_position():
    target = [['+2x']]
    try: #not pass
        new = afr(str_function="y=2x+0x2-0x-0")
        result = new.separate_argum
    except:
        result = True
    assert target == result
    
def test_get_arguments():
    target = [['+2x5'],['-2x4'],['+x3'],['-2x2'],['+x']]
    try: #not pass
        new = afr(str_function="y=2x5-2x4+x3-2x2+x+0")
        result = new.separate_argum
    except:
        resutl = False
    assert target == result
