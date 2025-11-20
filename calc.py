class Ingredient:
    def __init__(self, name, qty_per_craft, price_per_ingredient):
        self.name = name
        self.qty_per_craft = qty_per_craft
        self.price_per_ingredient = price_per_ingredient

    def total_cost_for_quantity(self, total_qty):
        return self.price_per_ingredient * total_qty

    def cost_per_craft(self):
        return int(round(self.qty_per_craft * self.price_per_ingredient))

class Craft:
    def __init__(self, name, ingredients, craft_price, num_crafts, total_units):
        self.name = name
        self.ingredients = ingredients
        self.craft_price = craft_price
        self.num_crafts = num_crafts
        self.total_units = total_units

    def calculate(self):
        # Расчет стоимости одного крафта
        total_ingredients_cost = sum(ing.cost_per_craft() for ing in self.ingredients)
        self.cost_per_craft = total_ingredients_cost + self.craft_price
        self.total_cost = self.cost_per_craft * self.num_crafts

        # Итоговое количество всех ингредиентов
        for ing in self.ingredients:
            ing.total_qty = ing.qty_per_craft * self.num_crafts
            ing.total_price = ing.total_cost_for_quantity(ing.total_qty)

        # Расчет стоимости за единицу
        self.cost_per_unit = int(self.total_cost / self.total_units)

    def generate_statistics(self):
        lines = []
        lines.append(f'=======================================\nСтатистика по крафту "{self.name}":\n')
        lines.append(f'Всего крафтов: {self.num_crafts}, получится предметов {self.total_units}\n')
        for ing in self.ingredients:
            cost_per_craft_str = f'{ing.cost_per_craft():,}'.replace(',', ' ')
            total_price_str = f'{ing.total_price:,}'.replace(',', ' ')
            total_qty_str = f'{ing.total_qty:,}'.replace(',', ' ')
            lines.append(
                f"{ing.name}: необходимо на 1 крафт - {ing.qty_per_craft}; цена за 1 шт.- {ing.price_per_ingredient:,}".replace(
                    ',', ' ') +
                f"; цена за 1 крафт- {cost_per_craft_str}; итог по общему количеству ({total_qty_str}): {total_price_str}\n"
            )
        total_cost_str = f'{self.total_cost:,}'.replace(',', ' ')
        lines.append(f'\nОбщая цена за {self.num_crafts} крафтов: {total_cost_str}\n')
        lines.append(f'Стоимость за одну единицу: {int(self.cost_per_unit)}\n')
        return ''.join(lines)

    def save_statistics(self, filename='statistika.txt'):
        stats = self.generate_statistics()
        print(stats)
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(stats)


def main():
    # Ввод данных
    name = input("Введите название крафта (или exit для выхода): ")
    if name == 'exit':
        return
    total_units = int(input("Введите количество единиц получаемого предмета: "))
    num_ingredients = int(input("Введите количество ингредиентов: "))

    ingredients = []
    for i in range(num_ingredients):
        print(f"\nИнгредиент {i+1}:")
        ing_name = input("Название ингредиента: ")
        qty_per_craft = int(input(f"Количество {ing_name} для одного крафта: "))
        price_per_ingredient = int(input(f"Цена за 1 {ing_name}: ").replace(' ', ''))
        ingredients.append(Ingredient(ing_name, qty_per_craft, price_per_ingredient))

    craft_price = int(input("Введите цену самого крафта: ").replace(' ', ''))
    num_crafts = int(input("Введите количество крафтов: "))
    total_units = total_units * num_crafts

    craft = Craft(name, ingredients, craft_price, num_crafts, total_units)
    craft.calculate()
    craft.save_statistics()

    print("Статистика сохранена в файл 'statistika.txt'.")

if __name__ == "__main__":
    main()