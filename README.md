# Общее описание 
Этот модуль создан для облегчения разговора с клиентами, а также для более быстрого обучения ИИ для ответов на самые простые вопросы (По типу "Привет", "Как дела?" и т. д.). В модуле есть как консольная версия модуля (использование print), так и версия для переменных (использование return).
# Установка
В данный момент установка других модулей для использования нашего не требуется.
# Приступая к работе
В данный момент в модуле существует 2 класса - Talk_with_consumer_eng_return и Talk_with_consumer_eng_print. Не трудно догадаться, что к чему и какой язык будет выводиться. В каждом из классов есть 4 функции (они одинаковые в обоих классах). Во всех функциях есть списки с различными словами и фразами, на выходе из функции модуль random выбирает случайное из заданных списков.
Список функций: 
1. **hello** - вывод случайного приветствия
2. **how_are_you_que** - вывод случайного вопроса "Как дела?"
3. **how_are_you_ans** - вывод случайного ответа на вопрос "Как дела?"
4. **bye** - вывод случайного прощания
