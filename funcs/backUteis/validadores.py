class Validadores:
    def valid_int1(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int
            return False
        return 0 <= value <= 9
    def valid_int2(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 99
    def valid_int4(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 9999
    def valid_int8(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 99999999
    def valid_int12(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 999999999999
    def valid_float8(self, text):
        if text == "":
            return True
        try:
            value = float(text)
        except ValueError:
            return False
        return len(text) < 9
    def valid_int6(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 999999
    def valid_float4(self, text):
        if text == "":
            return True
        try:
            value = float(text)
        except ValueError:
            return False
        return len(text) < 5
    def valid_float9(self, text):
        if text == "":
            return True
        try:
            value = float(text)
        except ValueError:
            return False
        return len(text) < 10
