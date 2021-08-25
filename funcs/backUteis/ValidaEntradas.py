
class ValidaEntradas:
    def validaEntradas(self):
        ### Naming input validators
        self.vcmd8 = (self.janela.register(self.valid_int8), "%P")
        self.vcmd6 = (self.janela.register(self.valid_int6), "%P")
        self.vcmd4 = (self.janela.register(self.valid_int4), "%P")
        self.vcmd2 = (self.janela.register(self.valid_int2), "%P")
        self.vcmd12 = (self.janela.register(self.valid_int12), "%P")
        self.vcmd8float = (self.janela.register(self.valid_float8), "%P")
        self.vcmd9float = (self.janela.register(self.valid_float9), "%P")
        self.vcmd4float = (self.janela.register(self.valid_float4), "%P")
