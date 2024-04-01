import pytest
from main import app
from unittest.mock import Mock

list_types = ['popular', 'now_playing', 'top_rated', 'upcoming']

@pytest.mark.parametrize("list_type", list_types)
def test_homepage_various_lists(monkeypatch, list_type):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("main.get_movies_list", api_mock)

    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
        assert response.status_code == 200
        api_mock.assert_called_once_with(list_type)
