class Plugin:
    def __init__(self, *args, **kwargs):
        self.plugin_name = "example"
        print('[GENESIS] plugin Init ("one")')

    def execute(self, a, b):
        print("Ich wurde zur laufzeit geändert-1")
        result =  int(a) + int(b)
        print("return Result" + str(result))
        return {self.plugin_name : str(result)}

    def __del__(self):
        pass
