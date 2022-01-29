class CheckStrFunction:

    def __init__(self):
        pass

    def separate_arguments(self, function: str, allow_op: list = ['-', '+']) -> list:
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
        if not function[0] in allow_op:
            function = '+' + function
        accumulator = ""
        for i in range(len(function)):
            if i == 0:
                accumulator += function[0]
                continue

            if not function[i] in allow_op:
                accumulator = accumulator + function[i]
                if i == len(function)-1:
                    list_arguments.append(accumulator)
            else:
                list_arguments.append(accumulator)
                accumulator = function[i]
        # In case the term equal +0 or -0 or -0x ... etc
        list_arguments = [
            i for i in list_arguments if list_arguments[list_arguments.index(i)][1] != '0']
        return list_arguments

    def check_doubles(self, function: str, variable_in_use: str, list_operation_allow: list = ['-', '+']) -> bool:
        """
        this function check if in the term are doubles of variables or operaction symbols like 2xx3++2

        Args:
            term (str): term that will to check
            variable_in_use (str): variable use in the function
            list_operation_allow (list, optional): list of the operation symbols allow. Defaults to ['-','+'].

        Returns:
            bool: True if the term pass the proof or false if not
        """

        for i in range(len(function)):
            if i == 0:
                before_is_variable = function[i] == variable_in_use
                before_is_op = function[i] in list_operation_allow
                continue
            if function[i] == variable_in_use and before_is_variable:
                return False
            elif function[i] in list_operation_allow and before_is_op:
                return False
            before_is_variable = function[i] == variable_in_use
            before_is_op = function[i] in list_operation_allow
        return True

    def check_degree_range(self, list_argms: list, variable_in_use: str = 'x') -> bool:

        max_grade = 0
        max_grade = 0
        for i in list_argms:
            if variable_in_use in i:
                argument_separate = i.split(variable_in_use)
                if not len(argument_separate) == 1:
                    if len(argument_separate[1]) == 1 and (int(argument_separate[1]) > 0 and int(argument_separate[1]) < 6):
                        grade = int(argument_separate[1])
                    elif len(argument_separate[1]) == 0:
                        grade = 1
                    else:
                        return 0
                    if max_grade < grade:
                        max_grade = grade
        return max_grade

    def check_variable_in_use(self, string_function: str, list_allow_variable: list):
        """[summary]

        Args:
            term (str): [description]
            list_allow_variable (list): [description]

        Returns:
            str: [description]
        """
        print(string_function)

        variable_letter = ""
        for i in string_function:
            if i in list_allow_variable:
                if not variable_letter:
                    variable_letter = i
                    continue
                else:
                    if not i == variable_letter:
                        variable_letter = "nv"
                        return variable_letter
        return variable_letter
