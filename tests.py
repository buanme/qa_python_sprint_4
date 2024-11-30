import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детективы')
        return collector


    def test_add_new_book_add_two_books(self,collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_with_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби: Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_in_list(self, collector):
        assert collector.get_books_genre()['Гордость и предубеждение и зомби'] == 'Детективы'

    def test_set_book_genre_not_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Праздник в замке Дракулы')
        collector.set_book_genre('Праздник в замке Дракулы', 'Мистика')
        assert collector.get_books_genre()['Праздник в замке Дракулы'] == ''

    def test_get_book_genre(self, collector):
        assert collector.get_books_genre().get('Гордость и предубеждение и зомби') == 'Детективы'

    def test_get_books_with_specific_genre(self, collector):
        assert collector.get_books_with_specific_genre('Детективы') == ['Гордость и предубеждение и зомби']

    @pytest.mark.parametrize('expected_result', [{'Гордость и предубеждение и зомби': 'Детективы'}])
    def test_get_books_genre(self, collector,expected_result):
        assert collector.get_books_genre() == expected_result

    def test_get_books_for_children_two_books(self, collector):
        collector.add_new_book('Король лев')
        collector.set_book_genre('Король лев', 'Мультфильмы')
        collector.add_new_book('Бетховен')
        collector.set_book_genre('Бетховен', 'Комедии')
        assert collector.get_books_for_children() == ['Король лев', 'Бетховен']

    def test_get_books_for_children_empty(self, collector):
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_double(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_no_book(self, collector):
        collector.add_book_in_favorites('Красавица и чудовище')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Король лев')
        collector.add_book_in_favorites('Король лев')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Король лев', 'Гордость и предубеждение и зомби']
