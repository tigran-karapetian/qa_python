# qa_python
# Добавлены проверки:
Нельзя добавить одну и ту же книгу дважды:
test_add_new_book_add_the_same_book_fail(self)

#Нельзя выставить рейтинг книге, которой нет в списке
test_set_book_rating_not_in_the_list_fail(self, collector)

#Нельзя выставить рейтинг меньше 1
test_set_book_rating_set_less_than_one_fail(self,collector)

#Нельзя выставить рейтинг больше 10
test_set_book_rating_set_more_than_ten_fail(self,collector)


#У не добавленной книги нет рейтинга
test_none_added_book_is_not_rating(self, collector)

#Добавление книги в избранное
test_add_book_in_favorites_success(self, collector)

#Нельзя добавить книгу в избранное,
#если её нет в словаре books_rating
test_add_book_in_favorites_if_book_not_in_books_rating_faile(self, collector)

#Проверка удаления книги из избранного
test_delete_book_from_favorites_success(self, collector)