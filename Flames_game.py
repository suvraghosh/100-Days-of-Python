print("       Let's predict the relationship between two names..!!")
def common_char(name1,name2):
    for i in range(len(name1)):
        for j in range(len(name2)):
            if name1[i]==name2[j]:
                a=name1[i]
                name1.remove(a)
                name2.remove(a)
                name3=name1+["*"]+name2
                return[name3,True]
    name3=name1+["*"]+name2
    return[name3,False]
if __name__=="__main__":
    n1=input("Enter the first name: ")
    n1.lower()
    n1.replace(" ","")
    n1_list=list(n1)
    n2 = input("Enter the second name: ")
    n2.lower()
    n2.replace(" ","")
    n2_list = list(n2)
    proceed=True

    while proceed:
       r1_list=common_char(n1_list,n2_list)
       c1_list=r1_list[0]
       proceed=r1_list[1]
       s1_index=c1_list.index("*")
       n1_list=c1_list[:s1_index]
       n2_list=c1_list[s1_index+1:]

    count = len(n1_list) + len(n2_list)

    # list of FLAMES
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(result) > 1:
        split_index = (count % len(result) - 1)

        if split_index >= 0:

            # list slicing
            right = result[split_index + 1:]
            left = result[: split_index]

            # list concatenation
            result = right + left

        else:
            result = result[: len(result) - 1]

    print("Relationship status :", result[0])