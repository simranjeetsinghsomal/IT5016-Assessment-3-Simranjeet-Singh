class Movie:
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year
        self.available = True

    def mark_as_rented(self):
        self.available = False

    def mark_as_available(self):
        self.available = True

    def __str__(self):
        return f" {self.title} ({self.year}) - {self.genre} - {'Available' if self.available else 'Rented'}"


class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_movies = []

    def rent_movie(self, movie):
        if movie.available:
            movie.mark_as_rented()
            self.rented_movies.append(movie)
            print(f"{self.name} rented {movie.title} ")
        else:
            print(f"{movie.title} is not available")

    def return_movie(self, movie):
        if movie in self.rented_movies:
            movie.mark_as_available()
            self.rented_movies.remove(movie)
            print(f"{self.name} returned {movie.title} ")
        else:
            print(f"{self.name} did not rent {movie.title}")

    def list_rented_movies(self):
        if self.rented_movies:
            print(f"{self.name}'s rented movies:")
            for movie in self.rented_movies:
                print(movie)
        else:
            print(f"{self.name} has no rented movies.")


class RentalStore:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def list_movies(self):
        if self.movies:
            print("Available Movies:")
            for movie in self.movies:
                print(movie)
        else:
            print("No movies available.")

    def find_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None


def menu():
    print("\nMovie Rental System Menu")
    print("1. List Available Movies")
    print("2. Rent a movie")
    print("3. Return a movie")
    print("4. List rented movies")
    print("5. Add a movie to Store")
    print("6. Exit")


def main():
    store = RentalStore()
    store.add_movie(Movie("Inception", "Sci-Fi", 2010))
    store.add_movie(Movie("The Matrix", "Action", 1999))
    store.add_movie(Movie("The Godfather", "Crime", 1972))

    customers = {
        "Alice": Customer("Alice"),
        "Bob": Customer("Bob")
    }

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            store.list_movies()
        elif choice == "2":
            customer_name = input("Enter your name: ")
            if customer_name in customers:
                customer = customers[customer_name]
                title = input("Enter the movie title: ")
                movie = store.find_movie(title)
                if movie:
                    customer.rent_movie(movie)
                else:
                    print("Movie not found.")
            else:
                print("Customer not found.")
        elif choice == "3":
            customer_name = input("Enter your name: ")
            if customer_name in customers:
                customer = customers[customer_name]
                title = input("Enter the movie title: ")
                movie = store.find_movie(title)
                if movie:
                    customer.return_movie(movie)
                else:
                    print("Movie not found.")
            else:
                print("Customer not found.")
        elif choice == "4":
            customer_name = input("Enter your name: ")
            if customer_name in customers:
                customer = customers[customer_name]
                customer.list_rented_movies()
            else:
                print("Customer not found.")
        elif choice == "5":
            title = input("Enter the movie title: ")
            genre = input("Enter the movie genre: ")
            year = int(input("Enter the movie year: "))
            store.add_movie(Movie(title, genre, year))
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()