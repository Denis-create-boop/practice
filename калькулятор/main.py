

def calc(funk):
    
    if "()" not in funk:
        if "*" not in funk and "/" not in funk:
            result = 0
            sym = ''
            for el in funk:
                try:
                    el = int(el)
                    if sym:
                        if sym == '+':
                            result += el
                        elif sym == '-':
                            result -= el
                    else:
                        result = el
                except:
                    sym = el
        else:
            num = ''
            ls = []
            ls_i = []
            for el in funk:
                try:
                    el = int(el)
                    num += str(el)
                except:
                    ls.append(int(num))
                    ls.append(el)
                    num = ''
            ls.append(int(num))
            
                    
    else:
        pass
    
    return result
                        
        
        


def main():
    while True:
        funk = input("==>> ")
        result = calc(''.join(funk.split()))
        print(result)
        print()



if __name__ == "__main__":
    main()