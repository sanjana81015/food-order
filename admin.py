
class admin:

     def __init__ (self):
      self.fooditem={101:['dosa',1,200,0,25],102:['pizza',1,300,0,15]}
      
     def addfood(self):
        self.foodrow={}
        self.FoodID= len(self.fooditem) + 101
    
        
        name=input('enter food name : ')
        quantity=input('enter plate : ')
        price=int(input('enter per plate price : '))
        discount=int(input('enter discount : '))
        stock=input('enter stock  : ')
        self.foodrow[self.FoodID]=[name,quantity,price,discount,stock]
        self.fooditem.update(self.foodrow)
        print('food added successfully....')
        print(self.fooditem)

     def editfood(self):
        food_id=int(input('enter food id  which u want to update'))
        for i,k in self.fooditem.items():
            if i==food_id:
                food_name = input("Enter updated food name : ")
                f_qty = (input("Enter updated food quantity : "))
                f_price = input("Enter updated food price : ")
                f_dis = input("Enter updated food discount : ")
                f_stock = (input("Enter updated food stock : "))
                 
                k[0]=food_name
                k[1]=f_qty
                k[2]=f_price
                k[3]=f_dis
                k[4]=f_stock
                print(self.fooditem)
                print('updated successfully')
                return
        print('pls check foodid and try again')

     def viewfood(self):
         for i,j in self.fooditem.items():
            print(f'food id : {i}\nName : {j[0]}\nQuantity : {j[1]} pieces\nPrice : {j[2]}rs\nDiscount : {j[3]}%\nStock : {j[4]} pieces available')

     def removefood(self):
        food_id=int(input('enter food id  which u want to delete'))
        for i,k in self.fooditem.items():
            if i==food_id:
               del self.fooditem[i]
               print('food item remove successfully')
               return
        print('check your ID and try again')
   
     def get(self):
      for i,j in self.fooditem.items():        
           print(f'Food ID: {i},{j[0]},{j[1]},{j[2]}per plate')
      return

     def getfood(self,fid):
         for i,j in self.fooditem.items():
           if fid==i:
              return j