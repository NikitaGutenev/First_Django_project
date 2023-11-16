class Year:
    regex = 'year-[0-9]{4}'

    def to_python(self, value):
        return int(value[5:])
    
    def to_url(self, value):
        return "%4s" % value
    