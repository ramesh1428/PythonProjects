import json
import random
with open('item.json','r') as f:
    d= json.load(f)
    # print(d)
    list_items=list(d.values())[0]
    # print(list_items[0])

class Bristo:
    list_selected_items=[]
    list_price =[]
    set_selected_items=[]
    individual_orders=[]
    def displayMenu(self):
        print("Items available")
        print("================")
        for i in range(0,len(list_items)):
            menu=f"{i+1}.{list_items[i].get('item_name')} --> price: {list_items[i].get('price')}"
            print(menu)
    def selectItem(self):
        flag = 'y'
        choose_item=int(input("Choose an item from the menu:"))
        while choose_item<=0 or choose_item>10:
            choose_item = int(input("Choose correct item from the menu:"))
        if choose_item >0 and choose_item<=10:
                self.list_selected_items.append({"item_name":list_items[choose_item-1].get('item_name'),"price":list_items[choose_item-1].get('price')})
        while flag == 'y':
            choose_item = int(input("Choose another item from the menu or press 11 to exit:"))
            while choose_item <= 0 or choose_item>11:
                choose_item = input("Choose correct item from the menu:")
            if choose_item > 0 and choose_item <= 10:
                self.list_selected_items.append({"item_name": list_items[choose_item - 1].get('item_name'),
                                                     "price": list_items[choose_item - 1].get('price')})
            elif choose_item == 11:
                break
        # print(self.list_selected_items)
        # for i in range(0, len(self.list_selected_items)):
        #     self.set_selected_items_rep.append(self.list_selected_items[i].get('item_name'))
        # print(self.set_selected_items_rep)
    def customerDetails(self):
        name = str(input("Enter your name : "))
        while not name.isalpha():
            name = str(input("Enter your name : "))
        mob = str(input("Enter your Mobile number : "))
        while len(mob) != 10 or mob.startswith("0"):
            mob = input("Enter your Mobile number again : ")
        with open(f"{self.order_num}.txt", "a") as f:
            f.write(f"Customer Name : {name} \n")
            f.write(f"Customer Phone number : {mob} \n")
            f.write("Orders \n")
            f.write("****************** \n")
        print("Customer name :"+name)
        print("Customer PhoneNo :"+mob)
    def individualPrice(self):
        for i in range(0,len(self.list_selected_items)):
            self.set_selected_items.append(f"{self.list_selected_items.count(self.list_selected_items[i])} X {self.list_selected_items[i].get('item_name')} ₹{self.list_selected_items[i].get('price')*self.list_selected_items.count(self.list_selected_items[i])}")
        s = set(self.set_selected_items)
        for i in range(0, len(s)):
            self.individual_orders.append(s.pop())
        with open(f"{self.order_num}.txt","a",encoding="utf-8")as f:
            f.write("Items Quantity Price \n")
        for i in range(0,len(self.individual_orders)):
            print(self.individual_orders[i])
            with open(f"{self.order_num}.txt", "a",encoding="utf-8") as f:
                f.write(f"{self.individual_orders[i]} \n")


    def totalPrice(self):
        check_student=int(input("Enter 1 if you are a student or 0 if not"))
        while check_student !=0 and check_student != 1:
            check_student = int(input("Enter 1 if you are a student or 0 if not"))
        if check_student ==1:
            for i in range(0,len(self.list_selected_items)):
                self.list_price.append(self.list_selected_items[i].get('price'))
            # print(self.list_price)
            sum=0
            gst_cost=0
            for i in range(0,len(self.list_price)):
                sum=sum+self.list_price[i]
                total_cost=sum-sum*5/100
                gst_cost=total_cost+total_cost*18/100
            print(f"{gst_cost}")
            with open(f"{self.order_num}.txt","a",encoding = "utf-8") as f:
                f.write("Student Discount 5% \n")
                f.write("Tax      18% \n")
                f.write("****************** \n")
                f.write(f"Grand Total ₹ {gst_cost} \n")
        elif check_student==0:
            for i in range(0,len(self.list_selected_items)):
                self.list_price.append(self.list_selected_items[i].get('price'))
            print(self.list_price)
            sum=0
            gst_cost=0
            for i in range(0,len(self.list_price)):
                sum=sum+self.list_price[i]
                gst_cost =sum+sum*18/100
            print(f"{gst_cost}")
            with open(f"{self.order_num}.txt","a",encoding = "utf-8") as f:
                f.write("****************** \n")
                f.write(f"Grand Total ₹ {gst_cost} \n")
    def generateOrderNo(self):
        self.order_num= f"ODN{random.randint(10000, 99999)}"
        with open(f"{self.order_num}.txt", "a",encoding="utf-8") as f:
            f.write(f"ORDER NUMBER : {self.order_num} \n")
        print(self.order_num)
obj1=Bristo()
obj1.generateOrderNo()
obj1.customerDetails()
obj1.displayMenu()
try:
    obj1.selectItem()
except ValueError:
    print("You've entered wrong options to select")
obj1.individualPrice()
try:
    obj1.totalPrice()
except ValueError:
    print("Wrong values")
