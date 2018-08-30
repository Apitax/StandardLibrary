

class Delegator:
    def __init__(self, command: Command):
        self.command = command
        
    def delegate(self):
        command = self.command.command
        lib = command[0]
        method = command[1]
        
        parameters = {}
        for i, parameter in enumerate(command[2:]):
            try:
                peek = command[3 + i]
                if(peek[:1] == '-'):
                    parameters[self.removeDashes(parameter)] = True
                else:
                    parameters[self.removeDashes(parameter)] = peek
            except:
                parameters[self.removeDashes(parameter)] = True
        
        instance = None
        
        if(lib == 'string'):
            from scriptaxstd.flow.String import String
            instance = String()
        elif(lib == 'math'):
            from scriptaxstd.flow.Math import Math
            instance = Math()
        elif(lib == 'path'):
            from scriptaxstd.flow.Path import Path
            instance = Path()
        elif(lib == 'file'):
            from scriptaxstd.flow.File import File
            instance = Math()
        elif(lib == 'time'):
            from scriptaxstd.flow.Time import Time
            instance = Time()
        elif(lib == 'binary'):
            from scriptaxstd.flow.Binary import Binary
            instance = Binary()
        
        if(not instance):
            print('INVALID LIBRARY')
        else:
            try:
                return getattr(instance, method)(**parameters)
            except:
                print('LIBRARY: ' + lib + ' DOES NOT CONTAIN METHOD: ' + method)
                return None
                    
    def removeDashes(self, passage):
        while passage[:1] == '-':
            passage = passage[:1]
        return passage