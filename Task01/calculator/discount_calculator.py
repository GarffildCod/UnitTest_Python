class Calculator:
    def calculate_discount(self, purchase_amount, discount_percent):
        if purchase_amount < 0 or discount_percent < 0 or discount_percent > 100:
            raise ArithmeticException("Невалидные аргументы")
        discount_amount = purchase_amount * (discount_percent / 100)
        return purchase_amount - discount_amount


class ArithmeticException(Exception):
    pass


if __name__ == '__main__':
    c = Calculator()
    total_price: float = 12_543.00
    print(f"_________________________\n"
          f"Итоговая цена   : {total_price}"
          f"\nс учетом скидки : {c.calculate_discount(total_price, 20):.2f}",
          "\n_________________________")

    print(f"_________________________\n"
          f"Итоговая цена   : {total_price}"
          f"\nс учетом скидки : {c.calculate_discount(total_price, 120):.2f}",
          "\n_________________________")
