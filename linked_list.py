head = {
        "value":11,
        "next":{
                "value":95,
                "next":{
                    "value":110,
                    "next":{
                        "value":250,
                        "next":{
                            "value":1000,
                            "next":None
                        }
                    }
                }
            }
        }

print(head['next']['next']['value'])

# print(linked_list.head.next.next.value)
