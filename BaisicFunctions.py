def rate_course(ratings):

    interestRating = int(input("Enter your topic interest rating [0 - 100]"))
    difficultyRating = int(input("Enter your difficulty estimation rating [0 - 100]"))
    instructorRating = int(input("Enter your instructor assessment rating [0 - 100]"))
    course_rating = interestRating + difficultyRating + instructorRating
    return course_rating


def main():
    print("Course Evaluation Program")
    print("-------------------------")
    ratings = ["topic interest", "difficulty estimation", "instructor assessment"]
    course = input("Enter course to evaluate (e.g. CSCI 127): ")
    course_rating = rate_course(ratings)
    print(course, "rating: ", course_rating)

    if course_rating >= 70:
        print("Highly recommended!")
    elif course_rating >= 30:
        print("Neutral recommendation")
    else:
        print("Not recommended!")


# ---------------------------------------

main()