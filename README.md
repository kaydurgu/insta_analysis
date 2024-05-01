# Instagram Profile Analyzer

This project is a Django-based web application that allows users to analyze Instagram profiles by providing a username. It utilizes the Instagram API to gather information about the specified user and presents various analytics and insights about their profile.

**This project was developed as a part of the Thesis diploma work, situational task 2.**


## System Architecture

The system architecture is based on the Django web framework and Django REST framework for creating RESTful APIs. It consists of the following components:

2. **Backend**: The backend is built using Django, which handles user requests, interacts with the Instagram API, and processes data.
3. **Database**: SQLite is used as the default database in Django for storing user information and analytics data.
4. **Instagram API**: The application interacts with the Instagram API to fetch data such as user profile information, followers, following, posts, etc.

## Data Models

The application includes the following Django models for storing and managing data:

1. **InstagramUser**: Represents an Instagram user with their username.
2. **InstagramUserProfile**: Stores detailed profile information such as profile picture link, country, biography, follower count, following count, etc.
3. **InstagramUserPosts**: Stores information related to user posts including the count of posts, most liked post, and most commented post.
4. **InstagramUserFriends**: Manages information about the user's friends including those who are not followed back, not following back, and mutual followers.

## API Endpoints

The application exposes the following API endpoints for interacting with the system:

- `GET /all_checked_users/`: Retrieve a list of all users who have been analyzed.
- `GET /check/`: Retrieve a list of all analysis requests.
- `POST /check/`: Submit a new analysis request for a specific Instagram user.
- `GET /check/{user}/followers`: Retrieve the list of followers for a specified user.
- `GET /check/{user}/following`: Retrieve the list of users followed by the specified user.
- `GET /check/{user}/info`: Retrieve detailed information about the specified user's profile.
- `GET /check/{user}/most_commented_post`: Retrieve the most commented post of the specified user.
- `GET /check/{user}/most_liked_post`: Retrieve the most liked post of the specified user.
- `GET /check/{user}/mutual_following`: Retrieve the list of mutual following the specified user .
- `GET /check/{user}/not_followed_back`: Retrieve the list of users who are not followed back by the specified user.
- `GET /check/{user}/not_following_back`: Retrieve the list of users whom the specified user is not following back.
- `GET /check/{user}/most_liking_friend`: Retrieve the username of the friend who liked the most posts of the specified user.
- `GET /check/{user}/most_commenting_friend`: Retrieve the username of the friend who commented the most posts of the specified user.
- `GET /check/{user}/posts`: Retrieve posts info made by the specified user.

## Implementation Details

- **Caching**: Caching mechanisms are implemented to reduce the number of API calls to the Instagram API and improve performance.
- **Error Handling**: Proper error handling is implemented to gracefully manage exceptions and provide informative error messages to users.
- **Documentation**: API documentation is generated using Swagger/OpenAPI for easy reference and usage of endpoints.

## Screenshots and Video Demonstration

[Video Demonstration](https://drive.google.com/drive/u/0/folders/1CAEaqrNKoDaMBcWxZbluy9pv_HquZ1q3)

API all enpoints

![Image Description](https://github.com/kaydurgu/insta_analysis/blob/main/imgs/Screenshot_11.png)

- `GET /check/{user}/info`: Retrieve detailed information about the specified user's profile.

![Image Description](https://github.com/kaydurgu/insta_analysis/blob/main/imgs/Screenshot_12.png)

- `GET /check/{user}/followers`: Retrieve the list of followers for a specified user.

![Image Description](https://github.com/kaydurgu/insta_analysis/blob/main/imgs/Screenshot_13.png)

- `GET /check/{user}/following`: Retrieve the list of users followed by the specified user.

![Image Description](https://github.com/kaydurgu/insta_analysis/blob/main/imgs/Screenshot_14.png)

- `GET /check/{user}/most_commented_post`: Retrieve the most commented post of the specified user.

![Image Description](https://github.com/kaydurgu/insta_analysis/blob/main/imgs/Screenshot_15.png)

- `GET /check/{user}/most_liked_post`: Retrieve the most liked post of the specified user.

![Image Description](https://github.com/kaydurgu/insta_analysis/blob/main/imgs/Screenshot_16.png)

- `GET /check/{user}/mutual_following`: Retrieve the list of mutual following the specified user .
![Image Description](https://github.com/kaydurgu/insta_analysis/blob/main/imgs/Screenshot_17.png)


- `GET /check/{user}/not_followed_back`: Retrieve the list of users who are not followed back by the specified user.
![Image Description](https://github.com/kaydurgu/insta_analysis/blob/main/imgs/Screenshot_18.png)

- `GET /check/{user}/not_following_back`: Retrieve the list of users whom the specified user is not following back.
![Image Description](https://github.com/kaydurgu/insta_analysis/blob/main/imgs/Screenshot_19.png)

- `GET /check/{user}/posts`: Retrieve posts info made by the specified user.
![Image Description](https://github.com/kaydurgu/insta_analysis/blob/main/imgs/Screenshot_20.png)

## Getting Started

To run the application locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your/repository.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables for API keys and database configurations.
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## Contributors

- Bakytbek uulu Zhanbolot

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
