#***************coffee machine**********************

#global varibales
milk=900
water=1000
coffee=200
profit=0

coffee_type={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24},
        "cost":150

    },
    "espresso": {
        "ingredients": {
            "water": 500,
            "milk": 0,
            "coffee": 18 },
        "cost": 100

    },
    "cappuccino": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 24, },
        "cost": 200

    }
}

def check_resource(coffe_t):
    if coffe_t=="latte":
        if coffee_type["latte"]["ingredients"]["water"]<=water and coffee_type["latte"]["ingredients"]["milk"]<=milk and coffee_type["latte"]["ingredients"]["coffee"]<=coffee:
            return True
    elif coffe_t == "espresso":
        if coffee_type["espresso"]["ingredients"]["water"]<=water and coffee_type["espresso"]["ingredients"]["milk"]<=milk and coffee_type["espresso"]["ingredients"]["coffee"]<=coffee:
            return True
    elif coffe_t == "cappuccino":
        if coffee_type["cappuccino"]["ingredients"]["water"]<=water and coffee_type["cappuccino"]["ingredients"]["milk"]<=milk and coffee_type["cappuccino"]["ingredients"]["coffee"]<=coffee:
            return True
    else:
        return False


while True:
    coffe_t=input("do you want to get the  latte,espresso,cappuccino,report or off>")
    if coffe_t=="off":
        break
    elif coffe_t=="report":
        print(f'''
            milk:{milk},
            water:{water},
            coffee:{coffee},
            money:{profit}
        ''')

    else:
        if check_resource(coffe_t):
            five=int(input("how many 5 rupess coins:"))
            ten=int(input("how many 10 rupess coins:"))
            twen=int(input("how many 20 rupess coins:"))
            cost=five*5+ten*10+twen*20

            if coffee_type[coffe_t]["cost"]<cost:
                print(f'ur change {cost-coffee_type[coffe_t]["cost"]}')
                profit+=cost
                print("take ur order")
                water -= coffee_type[coffe_t]["ingredients"]["water"]
                milk -= coffee_type[coffe_t]["ingredients"]["milk"]
                coffee -= coffee_type[coffe_t]["ingredients"]["coffee"]
            elif coffee_type[coffe_t]["cost"]>cost:
                print("not sufficient money")
            else:
                #reducing the resources
                print("take ur order")
                water-=coffee_type[coffe_t]["ingredients"]["water"]
                milk-=coffee_type[coffe_t]["ingredients"]["milk"]
                coffee-=coffee_type[coffe_t]["ingredients"]["coffee"]

        else:
            print("not sufficeint resources to make the beverage")
            print("come after refilling ! bye for now")
            break