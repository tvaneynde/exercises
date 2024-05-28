class MusicalNote:
    def __init__(self, name, pitch):
        self.name = name
        self.pitch = pitch

    @property
    def name(self):
        return self.__name

    @property
    def pitch(self):
        return self.__pitch
