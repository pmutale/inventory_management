class TokenConverter:
    regex = "[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}]"

    @staticmethod
    def to_python(value):
        return str(value)

    @staticmethod
    def to_url(value):
        return str(value)
