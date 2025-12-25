from main import BooksCollector
import pytest

class TestBooksCollector: 
    
    @pytest.mark.parametrize('name', ['A', 'A'*40])
    def test_add_new_book_add_two_books(self, collector, name):
        collector.add_new_book(name)

        assert name in collector.get_books_genre()
        
    def test_add_new_book_check_name_add(self, collector):
        collector.add_new_book('Гарри Поттер')

        assert 'Гарри Поттер' in collector.get_books_genre()    

    def test_add_new_book_without_name_negative(self, collector):
        collector.add_new_book("")
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_long_name_negative(self, collector):
        long_name = 'B' * 41 
        collector.add_new_book(long_name)

        assert len(collector.get_books_genre()) == 0
        
    

    def test_set_book_genre_sets_genre_for_existing_book(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'


    def test_new_book_has_no_genre_by_default(self, collector):
       collector.add_new_book('Гарри Поттер')

       assert collector.get_book_genre('Гарри Поттер') == '' 


    def test_book_genre_by_name_unknown_book(self, collector):

        assert collector.get_book_genre('Любовь и голуби') is None
  


    @pytest.mark.parametrize('name, genre', [['Гарри Потер','Фантастика'], ['Гринч', 'Мультфильмы']]) 
    def test_get_books_with_specific_genrere_turns_only_matching(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        result = collector.get_books_with_specific_genre(genre)

        assert name in result
        


    @pytest.mark.parametrize('name, genre', [['Гарри Потер','Фантастика'], ['Гринч', 'Мультфильмы']])
    def test_get_books_genre_matches_added_book(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_genre() == {name: genre}



    def test_get_books_for_children_with_childern_book(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert 'Гарри Поттер' in collector.get_books_for_children()

    def test_get_books_for_children_with_not_childern_book(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert 'Оно' not in collector.get_books_for_children()
 

    def test_add_book_in_favorites_add_one_book(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()


 

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')

        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()


    
    def test_get_list_of_favorites_books_returns_current_state(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Гринч')

        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гринч')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер', 'Гринч']

