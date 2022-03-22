import Avatar
import json


class ViewPrev:
    def __init__(self):
        self.waiter = Avatar

    def loadOrders(self, name):

        try:
            with open("Json\People.json") as p:
                data = p.read()
                people = json.loads(data)

                self.ordernum = people[name]
                self.ordernumlist = list(people[name].keys())

                for order in self.ordernumlist:
                    ordercontent = self.ordernum[order]
                    ordercontentlist = list(self.ordernum[order].keys())
                    print(f'Order {order}:')
                    waiter.say('Order {order}')
                    for contentorder in ordercontentlist:
                        orderprice = ordercontent[contentorder]
                        print(f'- {contentorder}: {orderprice}')
                        waiter.say(f'{contentorder}, {orderprice}')
                return
        except:
            print("error")


if __name__ == "__main__":
    a = ViewPrev()
    b = a.loadOrders('Michael')
