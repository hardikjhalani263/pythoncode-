
amount = 0 
def myntra():
        global amount
        try: 
            while True:
                print("\nWelcome to Myntra")
                print("Press to search the item:")
                print("1. shirt")
                print("2. Pant")
                print("3. Shoes")
                print("4. watch")
                print("5. Exit")

                choice = input("Enter a choice (1-5): ")

                if choice == '1':
                    amount = 0
                    while True:
                        b = int(input("press 1 for shirt \n press 2 for t-shirts \n press 3 for short t-shirts \n press 0 for previews page: "))
                        if(b == 1):
                            c = int(input("press 1 for shirt1 : 400 \n press 2 for shirt2 : 500 \n press 3 for shirt3 : 600 \n press 0 for exit: "))
                        if c == 1:
                            print("show all sirts1")
                            d = int(input("press 1 for add to card"))
                        if d == 1:
                            amount += 400
                        elif c == 2:
                            print("show all sirts2")
                            d = int(input("press 1 for add to card"))
                            if d == 1:
                                amount += 500
                            elif c == 3:
                                print("show all sirts3")
                                d = int(input("press 1 for add to card"))
                            if d == 1:
                                amount += 600
                        else:
                            break

                else:
                    print("thanks for visit our website........")
                    print("your total balance is : ",amount)

                if choice == '2':
                    amount = 0
                    while True:
                            b = int(input("press 1 for paint \n press 2 for short paint \n press 3 for jeans \n press 0 for previews page: "))
                            if(b == 1):
                                c = int(input("press 1 for paint1 : 400 \n press 2 for short paint2 : 500 \n press 3 for jeans3 : 600 \n press 0 for exit: "))
                            if c == 1:
                                print("show all paint1")
                                d = int(input("press 1 for add to card"))
                            if d == 1:
                                amount += 400
                            elif c == 2:
                                print("show all short paint2")
                                d = int(input("press 1 for add to card"))
                                if d == 1:
                                    amount += 500
                                elif c == 3:
                                    print("show all jeans3")
                                    d = int(input("press 1 for add to card"))
                                if d == 1:
                                    amount += 600
                            else:
                                break

                else:
                    print("thanks for visit our website........")
                    print("your total balance is : ",amount)

                if choice == '3':
                    amount = 0
                    while True:
                        b = int(input("press 1 for shoes \n press 2 for formal shoes \n press 3 for lofer \n press 0 for previews page: "))
                        if(b == 1):
                            c = int(input("press 1 for shoes1 : 400 \n press 2 for formal shoes2 : 500 \n press 3 for lofer3 : 600 \n press 0 for exit: "))
                        if c == 1:
                            print("show all sirts1")
                            d = int(input("press 1 for add to card"))
                        if d == 1:
                            amount += 400
                        elif c == 2:
                            print("show all sirts2")
                            d = int(input("press 1 for add to card"))
                            if d == 1:
                                amount += 500
                            elif c == 3:
                                print("show all sirts3")
                                d = int(input("press 1 for add to card"))
                            if d == 1:
                                amount += 600
                        else:
                            break

                else:
                    print("thanks for visit our website........")
                    print("your total balance is : ",amount)

                if choice == '4':
                    amount = 0
                    while True:
                        b = int(input("press 1 for watch \n press 2 for steel watch \n press 3 for leather watch \n press 0 for previews page: "))
                        if(b == 1):
                            c = int(input("press 1 for watch1 : 400 \n press 2 for steel watch2 : 500 \n press 3 for leather watch3 : 600 \n press 0 for exit: "))
                        if c == 1:
                            print("show all watch1")
                            d = int(input("press 1 for add to card"))
                        if d == 1:
                            amount += 400
                        elif c == 2:
                            print("show all steel watch2")
                            d = int(input("press 1 for add to card"))
                            if d == 1:
                                amount += 500
                            elif c == 3:
                                print("show all leather watch3")
                                d = int(input("press 1 for add to card"))
                            if d == 1:
                                amount += 600
                        else:
                            break

                else:
                    print("thanks for visit our website........")
                    print("your total balance is : ",amount)

                
            else:
                print
        except Exception as e:
            print("error is -->>>",e)         
def payment():
        
        if amount== amount:
            print("payment succeessfull")
        else:
            raise ValueError("you enter the wrong amount")

payment()
myntra()    