def largest():
    with open("numbers.txt") as new_file:
        best = 0
        for line in new_file:
            linings = int(line)
            if linings > best:
                best = linings
        return best
            
if __name__=="__main__":
    largest()