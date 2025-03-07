import termcolor


def heart():
    heart = []
    st_heart = ""
    start_one = 21
    end_one = 24
    start_two = 49
    end_two = 52
    def draw():
        nonlocal st_heart, heart, start_one, end_one, start_two, end_two
        count = 0
        for _ in range(2):
            for _ in range(75):
                st_heart += termcolor.colored("$", "blue")
            heart.append(st_heart)
            st_heart = ""
            count += 1

        for i in range(25):
            for i in range(75):
                if start_one < start_two:
                    if i < start_one or i > end_two:
                        st_heart += termcolor.colored("$", "blue")
                    elif i > end_one and i < start_two:
                        st_heart += termcolor.colored("$", "blue")
                    elif (i > start_one and i < end_one) or (i > start_two and i < end_two):
                        st_heart += termcolor.colored("&", "red")
                    else:
                        st_heart += " "
                else:
                    if i < start_one or i > end_two:
                        st_heart += termcolor.colored("$", "blue")
                    elif i > start_one and i < end_two:
                        st_heart += termcolor.colored("&", "red")
                    else:
                        st_heart += " "
            heart.append(st_heart)
            
            count += 1
            if count > 7 and count < 9:
                start_one -= 1
                end_one += 1
                start_two -= 1
                end_two += 1
                
            elif count == 9:
                for i in range(2):
                    heart.append(st_heart)
            
            elif count > 9:
                start_one += 2
                end_two -= 2
            else:
                if i == 6:
                    start_one -= 2
                    end_one += 2
                    start_two -= 2
                    end_two += 2
                else:
                    start_one -= 3
                    end_one += 3
                    start_two -= 3
                    end_two += 3
                    
            st_heart = ""
      
    draw()
    
    for st in heart:
        print(st)