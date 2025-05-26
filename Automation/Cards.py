from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

card_numbers = ['1234123413241234', '2234123413241234', '3234123413241234']
card_csvs = ['123', '325', '454']
card_dates = ['31.04.2036', '22.04.2023', '11.04.2022']

def test_cards_validation(card_number, card_csv, card_date):
    # Тут буде тест з пошуком елементів та їх взаємодією
    print(f'Добавлена карта: {card_number}, CSV: {card_csv}, card_date: {card_date}')

for i in range(len(card_numbers)):
    test_cards_validation(card_numbers[i], card_csvs[i], card_dates[i])