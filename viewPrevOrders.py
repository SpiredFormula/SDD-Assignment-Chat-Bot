from Avatar import Avatar
import json


class ViewPrev:
    def __init__(self):
        self.waiter = Avatar()

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

                    self.waiter.say(f'Order {order}:')
                    tprice = []
                    for contentorder in ordercontentlist:
                        orderprice = ordercontent[contentorder]
                        self.waiter.say(f'- {contentorder}: ${orderprice}')
                        tprice.append(orderprice)
                    num = 0
                    for t in tprice:
                        num = num + t
                    self.waiter.say(f'Total Price: ${num}')

                return
        except:
            self.waiter.say("You have no previous orders")


if __name__ == "__main__":
    a = ViewPrev()
    b = a.loadOrders('Michael')
