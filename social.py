class SS:

    def __init__(self, social):
        search_obj = re.search(r'^(?!219-09-9999|078-05-1120)(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}$',
                               social, flags=0)
        if search_obj is not None:
            self.social = social
        else:
            raise InvalidSocial

    def __str__(self):
        return self.social

    def __eq__(self, other):
        return self.social == other.social
