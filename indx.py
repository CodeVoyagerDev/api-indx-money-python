# К методам API WM идентификатор трейдера может обращаться не чаще 1 раза в секунду
import base64
import hashlib
import json
import requests


class IndxMoney:
    def __init__(self, login: str, password: str, wmid: str, reqn: str, culture="ru-RU"):
        self.login = login
        self.password = password
        self.wmid = wmid
        self.culture = culture
        self.reqn = reqn

    @staticmethod
    def api_indx(api_name, api_params):
        header = {
            "Content-type": "application/json; charset=UTF-8",
        }
        url = "https://api.indx.ru/api/v2/trade/" + api_name
        return requests.post(url, data=json.dumps(api_params), headers=header).json()

    def make_params(self, auth):
        signature = base64.b64encode(hashlib.sha256(auth.encode('utf-8')).digest()).decode('ascii')
        params = {
            "ApiContext": {
                "Login": self.login,
                "Password": self.password,
                "Wmid": self.wmid,
                "Culture": self.culture,
                "Signature": signature,
                "Reqn": self.reqn

            }
        }
        return params

    def balance(self):
        """
        Текущий баланс трейдера \n
        формируется из параметров: \n
        Login, Password, Culture, Wmid, Reqn \n

        wmid:: Wmid трейдера: "строка 12 символов, кодировка win-1251" \n
        nickname:: ник трейдера: строка от 0 до 255 символов, кодировка win-1251\n
        balance:: баланс трейдера: текущий баланс трейдера на Интернет-бирже, состоящий с цены портфеля (price)
        и суммы на счету (wmz) \n
        portfolio:: портфель трейдера: список принадлежащих инструментов трейдера с указанием названия,
        количества и средней цены покупки \n
        profit:: сделки трейдера: общая сумма затрат при покупке и продажах нот трейдером
        """
        parameters_balance = (
            self.login + ';'
            + self.password + ';'
            + self.culture + ';'
            + self.wmid + ';'
            + self.reqn
        )
        return self.api_indx('Balance', self.make_params(parameters_balance))

    def tools(self):
        """
        Список инструментов биржи \n
        формируется из параметров: \n
        Login, Password, Culture, Reqn
        """
        parameters_tools = (
            self.login + ';'
            + self.password + ';'
            + self.culture + ';'
            + self.reqn
        )
        return self.api_indx('Tools', self.make_params(parameters_tools))

    def np(self):
        """
        Список активов за которые торгуют.
        Формируется из параметров: \n
        Login, Password, Culture, Reqn\n

        id	номер инструмента	используется для обращения к инструментам в методах: \n
        HistoryTrading, HistoryTransaction, OfferMy и т.д.
        """
        parameters_np = (
                self.login + ';'
                + self.password + ';'
                + self.culture + ';'
                + self.reqn
        )
        return self.api_indx('NP', self.make_params(parameters_np))

    def ex_tools(self):
        """
        Расширенный список инструментов.
        Формируется из параметров: \n
        Login, Password, Culture, Reqn\n

        """
        parameters_ex_tools = (
                self.login + ';'
                + self.password + ';'
                + self.culture + ';'
                + self.reqn
        )
        return self.api_indx('ExTools', self.make_params(parameters_ex_tools))

    def ex_tools_by_np(self, np):
        """
        Расширенный список инструментов.
        Формируется из параметров: \n
        Login, Password, Culture, Reqn\n

        np	название актива за который торгуют	строка содержит одно из значений WMZ|USDT|USDC|TUSD|BTC|ETH|LTH\n
        (указывать заглавными буквами)
        """
        parameters_ex_tools_by_np = (
                self.login + ';'
                + self.password + ';'
                + self.culture + ';'
                + self.wmid + ';'
                + np + ';'
                + self.reqn
        )
        return self.api_indx('ExToolsByNP', self.make_params(parameters_ex_tools_by_np))

    def history_trading(self, id, date_start, date_end):
        """
        История торгов трейдера \n
        формируется из параметров: \n
        Login, Password, Culture, Wmid, ID, DateStart, DateEnd, Reqn\n

        Trading:: критерии отбора: применяется для поиска торгов по номеру инструмента
        с указанием временного интервала\n
        id:: номер инструмента: применяется для поиска инструмента\n
        date_start:: начальная дата:	временной интервал, формат YYYYMMDD,
        где YYYY – число года, MM – число месяца, DD – число дня\n
        date_end:: конечная дата: временной интервал, формат YYYYMMDD, где YYYY – число года,
        MM – число месяца, DD – число дня\n

        """
        parameters_history_trading = (
            self.login + ';'
            + self.password + ';'
            + self.culture + ';'
            + self.wmid + ';'
            + id + ';'
            + date_start + ';'
            + date_end + ';'
            + self.reqn
        )

        params = self.make_params(parameters_history_trading)

        params['Trading'] = {
            "ID": id,
            "DateStart": date_start,
            "DateEnd": date_end,
        }

        return self.api_indx("HistoryTrading", params)

    def history_transaction(self, id, date_start, date_end):
        """
        История трансакций трейдера \n
        формируется из параметров: \n
        Login, Password, Culture, Wmid, ID, DateStart, DateEnd, Reqn\n

        Trading:: критерии отбора: применяется для поиска торгов по номеру инструмента
        с указанием временного интервала\n
        id:: номер инструмента: применяется для поиска инструмента\n
        date_start::	начальная дата:	временной интервал, формат YYYYMMDD, где YYYY – число года,
        MM – число месяца, DD – число дня\n
        date_end:: конечная дата: временной интервал, формат YYYYMMDD, где YYYY – число года,
        MM – число месяца, DD – число дня\n
        """
        parameters_history_transaction = (
            self.login + ';'
            + self.password + ';'
            + self.culture + ';'
            + self.wmid + ';'
            + id + ';'
            + date_start + ';'
            + date_end + ';'
            + self.reqn
        )

        params = self.make_params(parameters_history_transaction)

        params['Trading'] = {
            "ID": id,
            "DateStart": date_start,
            "DateEnd": date_end
        }

        return self.api_indx("HistoryTransaction", params)

    def offer_my(self):
        """
        Список текущих заявок Трейдера на покупку / продажу \n
        формируется из параметров: \n
        Login, Password, Culture, Wmid, Reqn\n
        kind:: тип операции	задается целым десятичным числом, 1 -покупка, 0 - продажа
        """
        parameters_offer_my = (
            self.login + ';'
            + self.password + ';'
            + self.culture + ';'
            + self.wmid + ';'
            + self.reqn
        )
        return self.api_indx("OfferMy", self.make_params(parameters_offer_my))

    def offer_list(self, id):
        """
        Список текущих заявок по инструменту на покупку/продажу на бирже \n
        формируется из параметров: \n
        Login, Password, Culture, Wmid, ID, Reqn\n

        Trading::критерии отбора: применяется для поиска торгов по номеру инструмента с указанием временного интервала\n
        id:: номер инструмента:	применяется для поиска инструмента\n
        """
        parameters_offer_list = (
            self.login + ';'
            + self.password + ';'
            + self.culture + ';'
            + self.wmid + ';'
            + id + ';'
            + self.reqn
        )
        params = self.make_params(parameters_offer_list)

        params['Trading'] = {
            "ID": id,
        }

        return self.api_indx("OfferList", params)

    def offer_add(self, id, count, is_bid, price, is_anonymous=True):
        """
        Постановка новой заявки Трейдера на покупку/продажу по инструменту на бирже. \n
        формируется из параметров: \n
        Login, Password, Culture, Wmid, OfferID, Reqn \n

        id:: номер инструмента	создание заявки для данного инструмента \n
        count:: количество количество покупаемых или продаваемых инструментов \n
        is_bid:: тип подачи заявки:	true - заявка будет создана для покупки, false - для продажи \n
        price:: цена: стоимость за одну единицу инструмента \n
        is_anonymous:: статус подачи заявки: True - заявка будет создана анонимно, Nickname в списке заявок
        не отображается, False - отображается (по умолчанию стоит True "Анонимно"). \n

        """
        parameters_offer_add = (
            self.login + ';'
            + self.password + ';'
            + self.culture + ';'
            + self.wmid + ';'
            + id + ';'
            + self.reqn
        )
        params = self.make_params(parameters_offer_add)

        params['Offer'] = {
            "ID": id, "Count": count,
            "IsAnonymous": is_anonymous,
            "IsBid": is_bid,
            "Price": price
        }

        return self.api_indx("OfferAdd", params)

    def offer_delete(self, offers_id):
        """
        Удаление заявки Трейдера на покупку/продажу инструмента на бирже \n
        формируется из параметров: \n
        Login, Password, Culture, Wmid, OfferID, Reqn \n

        offers_id:: номер заявки: задается целым десятичным числом \n
        """
        parameters_offer_delete = (
            self.login + ';'
            + self.password + ';'
            + self.culture + ';'
            + self.wmid + ';'
            + offers_id + ';'
            + self.reqn
        )

        params = self.make_params(parameters_offer_delete)

        params['OfferID'] = offers_id

        return self.api_indx("OfferDelete", params)

    def tick(self, id, kind):
        """
        Статистика сделок за период времени \n
        формируется из параметров: \n
        Login, Password, Culture, Wmid, Tick/ID, Tick/Kind, Reqn \n

        Tick:: критерии отбора: применяется для поиска сделок по номеру инструмента с указанием временного интервала \n
        id:: номер инструмента: применяется для поиска инструмента \n
        kind:: период отбора: временной интервал, значения: 1 – день, 2 – неделя, 3 – Месяц, 4 - год
        """
        parameters_tick = (
            self.login + ';'
            + self.password + ';'
            + self.culture + ';'
            + self.wmid + ';'
            + id + ';'
            + kind + ';'
            + self.reqn
        )

        params = self.make_params(parameters_tick)

        params['Tick'] = {
            "ID": id,
            "Kind": kind,
        }

        return self.api_indx("Tick", params)
