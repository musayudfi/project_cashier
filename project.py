import pandas as pd
import numpy as np


class transaction:
    def __init__(self) -> None:
        self.items = pd.DataFrame({}, columns=['name_item', 'qty_item', 'price_item'])
        pass

    def add_item(self, name_item:str, qty_item:int, price_item: float) -> None:
        temp_df = pd.DataFrame([{"name_item":name_item, 
                                 "qty_item":qty_item, 
                                 "price_item": price_item }])
        
        if self.items.shape[0] >0:
            self.items = pd.concat([self.items, temp_df])
        else:
            self.items = temp_df
    
    def update_item_name(self, name_item, update_name_item) -> None:
        if self.items.shape[0] > 0:
            self.items.loc[self.items["name_item"]==name_item, "name_item"] = update_name_item
        else:
            print("Item is not created!, create item via add_item method")

    def update_item_qty(self, name_item, qty_item) -> None:
        if self.items.shape[0] > 0:
            self.items.loc[self.items["name_item"]==name_item, "qty_item"] = qty_item
        else:
            print("Item is not created!, create item via add_item method")
    
    def update_item_price(self, name_item, price_item ) -> None:
        if self.items.shape[0] > 0:
            self.items.loc[self.items["name_item"]==name_item, "price_item"] = price_item
        else:
            print("Item is not created!, create item via add_item method")
    
    def delete_item(self, name_item) -> None:
        if self.items.shape[0] > 0:
            self.items = self.items.loc[self.items["name_item"]!=name_item]
        else:
            print("Item is not created!, create item via add_item method")
    
    def reset_transaction(self) -> None:
        self.items = pd.DataFrame({})
    
    def check_order(self) -> None:
        if self.items.shape[0] > 0:
            print(self.items)
        else:
            print("Item is empty, create item via add_item method")
    
    def check_out(self) -> None:
        if self.items.shape[0] > 0:
            total_price = self.items["price_item"].sum()
            print(total_price)
            if total_price > 200000:
                print(f'Total {total_price} get discound 5%. final price {0.95*total_price}')
            elif total_price > 300000:
                print(f'Total {total_price} get discound 6%. final price {0.94*total_price}')
            elif total_price > 500000:
                print(f'Total {total_price} get discound 7%. final price {0.93*total_price}')
            else:
                print(f'Total {total_price}  final price {total_price}')
        else:
            print("Item is empty, create item via add_item method")
    
    def item_data(self):
        print(self.items)
        print(self.items.transpose())

if __name__ == "__main__":
    tr = transaction()
    tr.add_item("mobil", 2, 500000)
    tr.add_item("motor", 2, 1000000)
    tr.add_item("sepeda", 10, 10000000)
    tr.item_data()
    tr.check_out()
