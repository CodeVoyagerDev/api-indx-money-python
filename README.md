## Программные интерфейсы INDX

**[Balance](https://ru.webmoney.wiki/projects/webmoney/wiki/INDX_API_Balance)** - Текущий баланс Трейдера.

**[Tools](https://ru.webmoney.wiki/projects/webmoney/wiki/INDX_API_Tools)** - Список инструментов биржи.

**[NP](https://ru.webmoney.wiki/projects/webmoney/wiki/INDX_API_NP)** - Список активов за которые торгуют.

**[ExTools](https://ru.webmoney.wiki/projects/webmoney/wiki/INDX_API_ExTools)** - Расширенный список инструментов.

**[ExToolsByNP](https://ru.webmoney.wiki/projects/webmoney/wiki/INDX_API_ExToolsByNP)** - Cписок инструментов относительно актива за который торгуют.

**[HistoryTrading](https://ru.webmoney.wiki/projects/webmoney/wiki/INDX_API_HistoryTrading)** - История торгов Трейдера.

**[HistoryTransaction](https://ru.webmoney.wiki/projects/webmoney/wiki/INDX_API_HistoryTransaction)** - История трансакций Трейдера.

**[OfferMy](https://ru.webmoney.wiki/projects/webmoney/wiki/INDX_API_OfferMy)** - Список текущих заявок Трейдера на покупку/продажу.

**[OfferList](https://ru.webmoney.wiki/projects/webmoney/wiki/INDX_API_OfferList)** - Список текущих заявок по инструменту на покупку/продажу на бирже.

**[OfferAdd](https://ru.webmoney.wiki/projects/webmoney/wiki/INDX_API_OfferAdd)** - Постановка новой заявки Трейдера на покупку/продажу по инструменту на бирже.

**[OfferDelete](https://ru.webmoney.wiki/projects/webmoney/wiki/INDX_API_OfferDelete)** - Удаление заявки Трейдера на покупку/продажу инструмента на бирже.

**[Tick](https://ru.webmoney.wiki/projects/webmoney/wiki/INDX_API_Tick)** - Статистика сделок за период времени.


### API: Документация
Этот проект представляет собой реализацию взаимодействия с API биржи IndxMoney, предоставляющей возможность управлять аккаунтом трейдера, получать данные о текущих торгах, совершать сделки и анализировать результаты. Данный код реализован на языке Python и предоставляет функционал для работы с API биржи.

### Установка
Для использования данного кода необходимо предварительно установить следующие библиотеки:

```angular2html
pip install requests
```

или

```angular2html
pip freeze > requirements.txt
```

### Конфигурация
Чтобы начать использовать класс IndxMoney, вам необходимо создать экземпляр класса и передать параметры авторизации:

>* Login: Логин трейдера.
>* password: Пароль трейдера.
>* wmid: WMID (идентификатор трейдера в системе).
>* reqn: Уникальный запрос (номер запроса).
>* culture: Язык интерфейса (по умолчанию: "ru-RU").

```angular2html
from indx import IndxMoney
indx = IndxMoney(login="ваш_логин", password="ваш_пароль", culture='ru-RU', wmid="ваш_wmid", reqn="номер_запроса")
```
### Методы

1. balance()
Возвращает текущий баланс трейдера.

**Пример вызова:**

```angular2html
balance = indx.balance()
print(balance)
```
2. tools()
Возвращает список доступных инструментов биржи.

**Пример вызова:**

```angular2html
tools = indx.tools()
print(tools)
```

3. np()
Возвращает список активов, доступных для торговли.

**Пример вызова:**

```angular2html
np_list = indx.np()
print(np_list)
```

4. ex_tools()
Возвращает расширенный список инструментов.

**Пример вызова:**
```
ex_tools = indx.ex_tools()
print(ex_tools)
```

5. ex_tools_by_np(np)
Возвращает расширенный список инструментов для конкретного актива.

_Параметры:_

np: Название актива (например, WMZ, USDT и т.д.)
**Пример вызова:**

```angular2html
ex_tools_np = indx.ex_tools_by_np("WMZ")
print(ex_tools_np)
```

6. history_trading(id, date_start, date_end)
Возвращает историю торгов трейдера за указанный период.

_Параметры:_

* id: Идентификатор инструмента.
* date_start: Начальная дата в формате YYYYMMDD.
* date_end: Конечная дата в формате YYYYMMDD.
 
**Пример вызова:**

```
history = indx.history_trading(id="123", date_start="20230101", date_end="20231231")
print(history)
```

7. history_transaction(id, date_start, date_end)
Возвращает историю транзакций трейдера за указанный период.

_Параметры:_

* id: Идентификатор инструмента.
* date_start: Начальная дата в формате YYYYMMDD.
* date_end: Конечная дата в формате YYYYMMDD.

**Пример вызова:**

```angular2html
transactions = indx.history_transaction(id="123", date_start="20230101", date_end="20231231")
print(transactions)
```

8. offer_my()
Возвращает список текущих заявок трейдера на покупку/продажу.

**Пример вызова:**

```angular2html
offers = indx.offer_my()
print(offers)
```

9. offer_list(id)
Возвращает список текущих заявок по инструменту на бирже.

_Параметры:_

* id: Идентификатор инструмента.

**Пример вызова:**

```angular2html
offer_list = indx.offer_list(id="123")
print(offer_list)
```

10. offer_add(id, count, is_bid, price, is_anonymous=True)
Создает новую заявку на покупку/продажу инструмента.

_Параметры:_

* id: Идентификатор инструмента.
* count: Количество инструментов.
* is_bid: Тип заявки: True — покупка, False — продажа.
* price: Цена за единицу.
* is_anonymous: Заявка будет анонимной (по умолчанию: True).

**Пример вызова:**

```angular2html
new_offer = indx.offer_add(id="123", count=10, is_bid=True, price=100.5)
print(new_offer)
```

11. offer_delete(offers_id)
Удаляет заявку на покупку/продажу инструмента.

_Параметры:_

* offers_id: Идентификатор заявки.

**Пример вызова:**

```angular2html
delete_offer = indx.offer_delete(offers_id="12345")
print(delete_offer)
```

12. tick(id, kind)
Возвращает статистику сделок по инструменту за определенный период.

_Параметры:_

* id: Идентификатор инструмента.
* kind: Период отбора (1 — день, 2 — неделя, 3 — месяц, 4 — год).

**Пример вызова:**

```angular2html
tick_stats = indx.tick(id="123", kind=1)
print(tick_stats)
```






















