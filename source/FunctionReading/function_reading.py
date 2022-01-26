# %%


class AlgebraicFunctionReading:

    """
        This class is for working with algebraic function, validate and break down the attributes of the function
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        #   args:
            2 args refers to a lineal funtion example: (2,3) = fx = 2x + 3\n
            3 args refers to a cuadratic funtion example: (2,3,4) = fx = 2x2 + 3x + 4\n
            therefor the more arguments increase the degree of the function

        #   Keyword arguments:
        #  lineal example:
            string_function -- string ot the function example: "fx=2x+30"

            diccionary_function -- dictionary of the function example: {xc=2,c=30}  c -> constant

            list_function -- list of the function example: =[2,30]

        # cuadratic example:
            string_function -- string ot the function example: "fx=x2+2x+4"

            diccionary_function -- dictionary of the function example: {x2=1,xc=2,c=30}  c -> constant

            list_function -- list of the function example: =[1,2,30]
        """
        # ---- default attribute ----
        self.list_function = []
        self.dict_function = {}
        self.str_function = ""
        self.degree = 0
        self.variable_letter = ''
        self.separate_argum = []
        self.constant_value = 0
        self.__allow_variable = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm',
                                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'q', 'w', 'x', 'y', 'z']
        self.__verify_arg_kwargs(args, kwargs)

    def __verify_arg_kwargs(self, args, kwargs):
        """
            This funtion verify the args or the Kwargs and send error if some validation fail
        """
        kwargs_allows = ['str_function',
                         'dict_function', 'list_function']
        if args and kwargs:
            raise Exception(self.__sed_errors(4))
        if args:
            if not all(isinstance(n, (int, float)) for n in list(args)):
                raise Exception(self.__sed_errors(
                    3, f"Your arguments:\033[1m {args}"))
            self.degree = len(args)-1
            self.list_function = list(args)
        else:
            if not len(kwargs) == 1:
                raise Exception(self.__send_errors(
                    2, f"and You put\033[1m {len(kwargs)}:{list(kwargs.keys())}"))
            else:
                if not list(kwargs.keys())[0] in kwargs_allows:
                    raise Exception(self.__send_errors(
                        1, f"And you use\033[1m {list(kwargs.keys())[0]}"))
                index = kwargs_allows.index(list(kwargs.keys())[0])

                if index == 2:  # list validation
                    if not type(list(kwargs.values())[0]) == list:
                        raise Exception(self.__send_errors(
                            5, f", Expected \033[1m <class 'list'> \033[0;91m Obtained \033[1m {type(list(kwargs.values())[0])}"))
                    if not all(isinstance(n, (int, float)) for n in list(kwargs.values())[0]):
                        raise Exception(self.__send_errors(
                            3, f"Your arguments:\033[1m {args}"))
                    self.degree = len(list(kwargs.values())[0])
                    if not len(list(kwargs.values())[0]) > 1 and len(list(kwargs.values())[0]) < 5:
                        raise Exception(self.__send_errors(
                            6, f"The degree of the function received: \033[1m {self.degree}"))
                    self.list_function = list(list(kwargs.values())[0])

                elif index == 1:  # dict
                    if not type(list(kwargs.values())[0]) == dict:
                        raise Exception(self.__send_errors(
                            5, f", Expected \033[1m <class 'dict'> \033[0;91m Obtained \033[1m {type(list(kwargs.values())[0])}"))
                    if not list(kwargs.values())[0]:
                        raise Exception(self.__send_errors(
                            7, f"Your argument: \033[1m {kwargs}"))
                    self.__validate_dict_function(list(kwargs.values())[0])
                    self.dict_function = list(kwargs)[0]

                else:  # str
                    if not type(list(kwargs.values())[0]) == str:
                        raise Exception(self.__send_errors(
                            5, f", Expected \033[1m <class 'str'> \033[0;91m Obtained \033[1m {type(list(kwargs.values())[0])}"))
                    self.__validate_str_function(
                        kwargs[list(kwargs.keys())[0]])

    def __send_errors(self, n_error, extra_message=""):
        """
        This function is to send different error, in the process. \n
        Errors:\n
        1 - Only Allowed this representation of a funtion - string_function - diccionary_function - list_function -\n
        2 - Only Allowed one representacion of a funtion\n
        3 - Only Allowed numbers (int and float) as arg\n
        4 - Only can use args o kwargs(to access the others method of representation of a function) , but can't use both at same time\n
        5 - The type of the data is not what was expected\n
        6 - The range of the degree allow is 1 to 5\n
        7 - The name of variable need be unique\n
        8 - Can use all abecedary letter as variable except c or k (constant variable)\n
        9 - The only keys allow is the letter along or with a numer that represent the degree example: x2,x3,u2... etc\n
        10 - List function need have format like f(x)=2x2-x+23
        11 - The function  must be simplified
        Args:
            name_e (int): Number of error
            extra_message (str): Extra message with the error.
        """
        error = {
            1: "Only Allowed these representation of a function - string_function - diccionary_function - list_function -",
            2: "Only Allowed 1 representacion of a function ",
            3: "Only Allowed numbers (int and float) as arg ",
            4: "Only can use args o kwargs(to access the others method of representation of a function) , but can't use both at same time ",
            5: "The type of the data is not what was expected ",
            6: "The range of the degree allow is 1 to 5 ",
            7: "Not empty values allow ",
            8: "Can use all abecedary letter as variable except c or k (constant variable) ",
            9: "The only keys allow is the letter along or with a numer that represent the degree example: x2,x3,u2... etc ",
            10: "Error in the str function format ",
            11: "The function  must be simplified ",
            12: "Only admit one variable "
        }
        if error.get(n_error):
            return '\033[91m' + error.get(n_error) + extra_message + '\033[0m'
        else:
            return print("Error not found")

    def __validate_dict_function(self, function: dict):
        """
        This funtion validate if the dictionary function pass is correct and complies with the rules
        1. The constant pass have key name = c or k
        2. Can use all abecedary letter as variable example:
        x2 = 2, z = -1 , c = 1 (2x**2-1z+1)

        Args:
            dict (dict): dictionary that will test
        """
        letter_variable = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm',
                           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'q', 'w', 'x', 'y', 'z']
        list_key = list(function.keys())
        # Validated the first letter is a allow letter_variable
        # TODO: Admit ony one variable
        try:
            list_key_first = [i[0].lower() for i in list_key]
        except:
            raise Exception(self.__send_errors(
                8, f"Your variable \033[1m {list_key}"))
        have_allow_variable = all(
            letter in letter_variable for letter in list_key_first)
        if not have_allow_variable:
            raise Exception(self.__send_errors(
                8, f"Your variable name \033[1m {list_key}"))
        # Validated that the second char is a number or not and the len is not more thant 2
        for i in list_key:
            print(len(i))
            if not len(i) < 3:
                raise Exception(self.__send_errors(
                    9, f"Your variable \033[1m {list_key}"))
            if not len(i) == 1:
                try:
                    test_int = int(i[1])
                except:
                    raise Exception(self.__send_errors(
                        9, f"Your variable \033[1m {list_key}"))
                # Validate that the second number is more than 0 and less than 6
                if test_int < 0 or test_int > 5:
                    raise Exception(self.__send_errors(
                        6, f"Your variable degree \033[1m {i[0]} = {i[1]}"))
        # Validate value is number
        if not all(isinstance(n, (int, float)) for n in list(function.values)):
            raise Exception(self.__send_errors(
                3, f"The values of your variable: \033[1m {i[0]} = {i[1]}"))

    def __validate_str_function(self, function: str):
        """
        This funtion validate if the string function pass is correct and complies with the rules
        only allow one variable, the max degree is 5 
        Args:
            list (list): list that will test
        """

        def separate_arguments(term: str, allow_op: list = ['-', '+']) -> list:
            """
            This function separate a string function in it arguments and add to list

            Args:
                term (str): the string function to be separated
                allow_op (list, optional): list of the operaction symbol that use to separate the string. Defaults to ['-','+']

            Returns:
                list: list with each arguments
            """

            # check if the first letter have subtract or add symbol, if not put default add
            list_arguments = []
            if not term[0] in allow_op:
                term = '+' + term
            accumulator = ""
            for i in range(len(term)):
                if i == 0:
                    accumulator += term[0]
                    continue
                if not term[i] in allow_op:
                    accumulator = accumulator + term[i]
                    if i == len(term)-1:
                        list_arguments.append(accumulator)
                else:
                    list_arguments.append(accumulator)
                    accumulator = term[i]
            # In case the term equal +0 or -0 or -0x ... etc
            list_arguments = [
                i for i in list_arguments if list_arguments[list_arguments.index(i)][1] != '0']
            return list_arguments

        list_allow_symbol = ['+', '-']
        # divide the function in equal symbol (check if this symbol exist)
        if not '=' in function:
            raise Exception(self.__send_errors(
                10, f"your input string function: {function}"))
        terms = function.split("=")
        if not len(terms) == 2:
            raise Exception(self.__send_errors(
                10, f"your input string function: {function}"))
        term_r = terms[1]
        # check if the initial and the last character of the second argument of the function is not a symbol (except + and -)
        if (not term_r[0].isnumeric() and term_r[0] not in list_allow_symbol) or (not term_r[-1].isnumeric() and term_r[-1] not in self.__allow_variable):
            raise Exception(self.__send_errors(
                10, f"your input string function: {function}"))
        # search if have variable or is a constant funciton (if exist save what letter use)
        for i in term_r:
            if i in self.__allow_variable:
                if not self.variable_letter:
                    self.variable_letter = i
                    continue
                else:
                    if not i == self.variable_letter:
                        raise Exception(self.__send_errors(
                            12, f"your input string function: {function}"))
        before_is_num = term_r[0].isnumeric()
        # TODO: check error in the logic
        for i in range(len(term_r)):
            if i == 0:
                continue
            if not term_r[i].isnumeric():
                if not term_r[i] in list_allow_symbol and not term_r[i] == self.variable_letter:
                    raise Exception(self.__send_errors(
                        11, f"your input string function: {function}"))
                # check dont repeat symbol like 2++3-4
                if not before_is_num and not term_r[i-1] == self.variable_letter:
                    raise Exception(self.__send_errors(
                        10, f"your input string function: {function}"))
                if term_r[i] == self.variable_letter:
                    before_is_num = False
                    continue
                else:  # means that repeat a symbol like ++ or --
                    raise Exception(self.__send_errors(
                        10, f"your input string function: {function}"))
            before_is_num = True
        self.separate_argum = separate_arguments(term_r)
        # TODO: check the highest degree of the variable
        # TODO: make test
        pass
# %%
new = AlgebraicFunctionReading(str_function="y=2x+0x2-0x-0")
