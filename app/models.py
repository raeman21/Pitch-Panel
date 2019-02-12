class Pitch:
    '''
   Pitch class to define Pitch Objects
    '''

    all_pitches = []

    def __init__(self,author,title,content,date_posted):
        self.author = author
        self.title = title
        self.content = content
        self.date_posted = date_posted


    def save_pitch(self):
       Pitch.all_pitches.append(self)

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(cls,id):

        response = []

        for pitch in cls.all_pitches:
            if pitch.movie_id == id:
                response.append(pitch)

        return response