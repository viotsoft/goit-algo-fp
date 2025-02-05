# Завдання 7

## Імітація кидків двох гральних кубиків (Метод Монте-Карло)

У цьому проєкті ми моделюємо велику кількість кидків двох гральних кубиків для оцінки ймовірностей сум на кубиках.

## Результати симуляції

Для **1 000 000** кидків ми отримали такі приблизні ймовірності (приклад):

![image](https://github.com/user-attachments/assets/88f81609-26e7-4e47-aac0-6c48237f778c)

## Висновки до завдання 7

1. Експериментальні (емпіричні) ймовірності **близькі** до теоретичних при великій кількості повторень.
2. Найбільш ймовірна сума – **7** (близько \(1/6\)), що підтверджується як теоретично, так і емпірично.
3. Збільшення кількості кидків зменшує різницю між теоретичними та емпіричними значеннями (згідно із Законом Великих Чисел).
4. Розбіжність між Монте-Карло симуляцією і теорією **менше 1%** майже для всіх сум при 1 мільйоні кидків.

Проєкт демонструє, що метод Монте-Карло є дієвим підходом для наближених оцінок імовірностей у випадкових процесах.

---
