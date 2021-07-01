Работаю с тестами

------------
- unittest -
------------
https://docs.python.org/3/library/unittest.html
методы assert*() - https://docs.python.org/3/library/unittest.html#unittest.TestCase
- Фикстуры -
Метод setUp() - вызывается автоматически для каждого отдельного теста
Метод tearDown() - тоже самое, но в конце

unittest.TestSuite() - Мы можем осуществлять выборочный запуск тестов через этот класс

декораторы @unittest.skip* - нужны для пропуска определенных тестов (как методов, так и классов целиком) (возможно, по условию)
https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures
https://docs.python.org/3/library/unittest.html#unittest.skip

декоратор @unittest.expectedFailure - ожидает ошибки. Если тест пройден, это будет считаться неудачным.

Когда есть несколько тестов с небольшимим различиями, можно делать ПОДтесты, используя subTest()
# https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests
- если производить тесты простыми итерациями, то при 1ом непройденном тесте программа прекратит какие-либо действия

Класс TestCase()
Включает в себя 3 группы методов:
    - для запуска тестов (Например, setUp, tearDown, setUpClass, tearDownClass)
    - реализация тестов для проверки условий и сообщения от ошибах (assert*())
    - дополнительные методы запроса, позволяющие собирать информацию о самом тесте(Например, fail, failureException, longMessage)

Класс unittest.IsolatedAsyncioTestCase(methodName='runTest') -
- Аналогично TestCase(), но для карутин

Класс unittest.TestSuite(tests=())
Этот класс представляет собой совокупность отдельных тестовых примеров и наборов тестов.
Объекты TestSuite ведут себя так же, как объекты TestCase, за исключением того, что на самом деле они не реализуют тест.
Вместо этого они используются для объединения тестов в группы тестов, которые должны выполняться вместе.

python -m unittest - запуск из консоли
python -m unittest test_calc.CalcTest - запуск отдельного класса
python -m unittest -v test_calc.py - запуск с выводом подробной информации


-----------------
- unittest.mock -
-----------------
https://docs.python.org/3/library/unittest.mock-examples.html
https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
Mock заменяет выбранные объекты экземплярами класса MagicMock(), проверяя,
правтльно ли вызывается замененный объект