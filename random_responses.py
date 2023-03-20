import random


def random_string():
    random_list = [
    "Ndiyo, na unafikiri vipi kuhusu hilo?",
    "Haya, endelea kuongea.",
    "Sijaelewa kabisa. Je, unaweza kufafanua zaidi?",
    "Ninapata picha unayosema. Lakini, kwa nini unahisi hivyo?",
    "Ninafikiria ni vizuri zaidi tukajikita kwenye mada yetu.",
    "Ningependa kujua zaidi kuhusu hilo.",
    "Ndiyo, na unataka kufanya nini baadaye?",
    "Nasikia unavyosema. Unaweza kufafanua kwa undani zaidi?",
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
