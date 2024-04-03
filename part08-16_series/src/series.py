class Series:
    
    def __init__(self, title: str, num: float, lista: list):
        self.title = title
        self.num = num
        self.lista = lista
        self.counter = 0
        self.sums = 0
    
    def __str__(self):
        genres = ', '.join(self.lista)
        if self.counter == 0:
            return f"{self.title} ({self.num} seasons)\ngenres: {genres} \nno ratings"
        else: 
            return f"{self.title} ({self.num} seasons)\ngenres: {genres} \n{self.counter} ratings, average {self.sums/self.counter:.1f} points"
        
    def rate(self, rating: int):
        if rating >= 0:
            self.counter += 1
            self.sums += rating

def minimum_grade(rating: float, series_list: list):
    return [series for series in series_list if series.sums/series.counter >= rating]

def includes_genre(genre: str, series_list: list):
    return [series for series in series_list if genre in series.lista]



if __name__ =="__main__":
    
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
