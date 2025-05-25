import pandas as pd

def test_libraries():
    print('')
    # Создать DataFrame
    df = pd.DataFrame({
        'ім\'я': ['Іван', 'Марія', 'Петро'],
        'вік': [25, 30, 21],
    })

    print(df)

    filtration = df[df['вік'] > 25]
    # print(filtration)

    # Группировка:
    group = df.groupby('вік').count()
    # print(group)

    # Агрегация:
    aggregation = df['вік'].mean()
    # print(aggregation)
