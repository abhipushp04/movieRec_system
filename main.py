from movie_recommender import MovieRecommender

def print_movie_list(movies):
    """Helper function to print formatted movie information"""
    for i, (title, rating, count) in enumerate(movies, 1):
        print(f"{i}. {title}")
        print(f"   Rating: {rating}/5.0 ({count} ratings)")
        print()

def main():
    # Initialize the recommender
    recommender = MovieRecommender()
    
    while True:
        print("\n=== Movie Recommendation System ===")
        print("1. Show Top 10 Movies")
        print("2. Find Movies by Starting Letter")
        print("3. Get Random Movie Recommendation")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            print("\n=== Top 10 Rated Movies ===\n")
            top_movies = recommender.get_top_10_movies()
            print_movie_list(top_movies)

        elif choice == '2':
            letter = input("\nEnter starting letter: ")
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a single letter.")
                continue
                
            print(f"\n=== Top Movies Starting With '{letter.upper()}' ===\n")
            letter_movies = recommender.get_movies_by_letter(letter)
            
            if not letter_movies:
                print(f"No movies found starting with '{letter}'")
            else:
                print_movie_list(letter_movies)

        elif choice == '3':
            print("\n=== Random Movie Recommendation ===\n")
            movie = recommender.get_random_movie()
            print_movie_list([movie])

        elif choice == '4':
            print("\nThank you for using the Movie Recommender!")
            break
            
        else:
            print("\nInvalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()