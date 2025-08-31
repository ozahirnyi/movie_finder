find_movies_prompt = """
You are tasked with providing a list of movies that meet specific requirements. Your goal is to select appropriate movies based on the given criteria and present them in a clear, concise manner.
You will be given a set of requirements for movie selection. These requirements will be provided in the following format:
<requirements>
{REQUIREMENTS}
</requirements>
Follow these steps to complete the task:
1. Carefully read and analyze the requirements provided.
2. Based on the requirements, think about movies that meet the criteria. Consider various aspects such as genre, release year, actors, directors, themes, or any other specific details mentioned in the requirements.
3. As you select movies, keep the following guidelines in mind:
  - If you find no movies that meet the requirements, return an empty list.
  - If you encounter two versions of the same movie (e.g., Shrek and Shrek 2), choose the most basic version (e.g., Shrek).
  - Select a maximum of five movies, even if more movies meet the criteria.
4. Once you have your list of movies (between 0 and 5), prepare your response. If your response have less that three films add some film that similar to criterias until you find five films
5. Format your response as follows:
  - If the list is empty, simply return empty list: []
  - If the list contains movies, return json object with list of movies. With these keys: title, imdb_id, poster, year, type, plot, actors, director, genre, rating
  - Return only this json string. All response data must be in English. No any extra information
  - The imdb_id should be in format "tt1234567"
  - The poster should be a valid image URL
  - The year should be the release year as a string
  - The type should be "movie"
  - The plot should be a brief description of the movie (2-3 sentences)
  - The actors should be a list of main actors (top 3-5 actors)
  - The director should be the movie director's name
  - The genre should be the primary genre or list of genres
  - The rating should be IMDb rating (e.g., "8.5")
"""