def calculate(min, max, step):
   num=0
   for i in range(min,max+1,step):
      num+=i 
   print(num)
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

def avg(data):
   total=0
   ppl=0
   for i in data["employees"]:
      if i["manager"]==False:
         total+=i["salary"]
         ppl+=1
   print(int(total/ppl)) 
avg({
        "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
        ]
    })

def func(a):
   def func_2(b,c):
      x=a+(b*c)
      print(x)
   return func_2
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

def maxProduct(nums):
   n=0
   max=0
   max1=0
   x=int(len(nums))
   for i in range(x):
      for j in range(i+1,x):
        if x<=2:
          max1=nums[i]*nums[j]
        else:
          n=nums[i]*nums[j]
          max=n 
          if max>max1:
            max1=max 
       
          
   print(max1)                           
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

def twoSum(nums, target):
   for i in range(int(len(nums))):
      for j in range(int(len(nums))):
         if i!=j:
            s=nums[i]+nums[j]
            if s==target:
               return [i,j]                
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

def maxZeros(nums):
   num=0   
   num1=0  
   x=int(len(nums))
   for i in range(x):
      if nums[i]==0:
         num+=1    
         if num>num1:
               num1=num                 
      else:
         num=0    
   print(num1)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3





