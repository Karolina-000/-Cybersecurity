"""
One hot summer day Pete and his friend Billy decided to buy a watermelon. 
They chose the biggest and the ripest one, in their opinion. After that 
the watermelon was weighed, and the scales showed w kilos. They rushed home, 
dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide 
the watermelon in such a way that each of the two parts weighs even number of kilos, 
at the same time it is not obligatory that the parts are equal. The boys are 
extremely tired and want to start their meal as soon as possible, that's why 
you should help them and find out, if they can divide the watermelon in the way 
they want. For sure, each of them should get a part of positive weight.

Input:
The first (and the only) input line contains integer number w (1 <= w <= 100) — 
the weight of the watermelon bought by the boys.

Output:
Print YES, if the boys can divide the watermelon into two parts, each of them 
weighing even number of kilos; and NO in the opposite case.
"""


# 1. ვიღებთ საზამთროს წონას (w).
# int() ფუნქცია ტექსტს გადაიყვანს მთელ რიცხვში.
w = int(input("Enter the weight of the watermelon: "))

# 2. ვამოწმებთ ორ აუცილებელ პირობას:
# ა) w > 2  --> წონა უნდა იყოს 2-ზე მეტი (რადგან 2-ის გაყოფა მხოლოდ 1+1-ად შეიძლება, 1 კი კენტია).
# ბ) w % 2 == 0 --> წონა 2-ზე უნაშთოდ უნდა იყოფოდეს (ანუ იყოს ლუწი).
if 1 <= w <= 100:
    if w > 2 and w % 2 == 0:
        # თუ ორივე პირობა შესრულდა, ვბეჭდავთ YES-ს (ყველა დიდი ასოთი)
        print("YES")
    else:
        # სხვა შემთხვევაში ვბეჭდავთ NO-ს
        print("NO")