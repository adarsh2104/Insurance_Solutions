

class CommonFunctions:
    '''
    Class for grouping functions to perform common operations. 
    '''
    def serializer_error_parser(self,errors:dict):
        '''
        Parse the serializer generated dict type errors 
        into clean readable string without loosing critical attribute.
        '''

        error_list = []
        for field,error in errors.items():
            field_message = error[0] if error else ''
            error_message = field.capitalize() + ':' + field_message
            # Append the errors for each fields in "Field : Error message" format
            error_list.append(error_message)
        return ' \n '.join(error_list)    

