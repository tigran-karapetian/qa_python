# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books_success(self, collector):


        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже


    # Нельзя добавить одну и ту же книгу дважды
    def test_add_new_book_add_the_same_book_fail(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1

    #Нельзя выставить рейтинг книге, которой нет в списке
    def test_set_book_rating_not_in_the_list_fail(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение', 2)
        assert collector.books_rating == {'Гордость и предубеждение и зомби':1}

    #Нельзя выставить рейтинг меньше 1
    def test_set_book_rating_set_less_than_one_fail(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', -1)
        assert collector.books_rating == {'Гордость и предубеждение и зомби':1}

    #Нельзя выставить рейтинг больше 10
    def test_set_book_rating_set_more_than_ten_fail(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)
        assert collector.books_rating == {'Гордость и предубеждение и зомби':1}

    #У не добавленной книги нет рейтинга
    def test_none_added_book_is_not_rating(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_rating('Гордость и предубеждение') is None

    #Добавление книги в избранное
    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert  len(collector.get_list_of_favorites_books()) == 1

    #Нельзя добавить книгу в избранное,
    #если её нет в словаре books_rating
    def test_add_book_in_favorites_if_book_not_in_books_rating_faile(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    #Проверка удаления книги из избранного
    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []