import unittest
from unittest.mock import patch, Mock
import main

class TestMovieLibrary(unittest.TestCase):
    @patch('main.requests.get') 
    def test_get_single_movie_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"id": 1, "title": "Mock Movie"}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        
        
        movie = main.get_single_movie(1)
        
        # Verify
        self.assertEqual(movie['title'], "Mock Movie")
        mock_get.assert_called_once_with(
            "https://api.themoviedb.org/3/movie/1",
            headers={"Authorization": f"Bearer {main.API_TOKEN}"}
        )
    
    @patch('main.requests.get')
    def test_get_movie_cast_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"cast": [{"name": "Mock Actor"}]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        
        cast = main.get_movie_cast(1)
        
        self.assertIn("Mock Actor", [member['name'] for member in cast])
    

if __name__ == '__main__':
    unittest.main()
