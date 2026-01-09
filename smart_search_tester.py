from selene.support.shared import browser
from selene import query
from selene import be, have
from selenium import webdriver
import time

# Задача
# Проверяет:
# Что на первой странице есть хотя бы 5 результатов



# Настройка
browser.config.driver = webdriver.Chrome()
browser.config.timeout = 10

try:
    # Тест из курса (точно как в примере)
    browser.open('https://duckduckgo.com')


    browser.element('[name="q"]').type('автоматизация тестирования Python').press_enter()
    
    browser.all('a').should(have.size_greater_than(0))
    all_links = browser.all('a')
    links_elements = list(all_links)
    result = []
    for i, element in enumerate(links_elements[:5], 1):
        href = element.get(query.attribute('href'))
        if href and 'qa.guru' in href:
            result.append(href)
            print(f'Найдена ссылка #{len(result)}: {href}')
    
    #Ручная проверка

    # element = browser.element('.search3__input')
    # print('✓ Элемент найден в DOM')

    # print(f'Видимый: {element.matching(be.visible)}')
    # print(f'Существует: {element.matching(be.present)}')
    # print(f'КликАбельный: {element.matching(be.clickable)}')

    # print(f'Размер: {element().size["width"]}x{element().size["height"]}')
    # print(f'Display: {element().value_of_css_property("display")}')
    # print(f'Opacity: {element().value_of_css_property("opacity")}')
    
except Exception as e:
    print(f"Ошибка: {e}")
    
finally:
    browser.quit()