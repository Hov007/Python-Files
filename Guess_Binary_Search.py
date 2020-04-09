def guesser(start=0, end=1000, step=1):
    if step > 10:
        print("You cheated!!!")
        return

    guess = (start + end) // 2
    print('My guess number {}: {}'.format(step, guess))
    hint = int(input())
    if hint == 0:
        print('I guessed in {} steps!'.format(step))
        return
    if start == end:
        print("You cheated!!!")
        return
    if hint == -1:
        end = guess
    if hint == 1:
        start = guess + 1
    guess = (start + end) // 2
    return guesser(start, end, step + 1)

if __name__=='__main__':
    ready_or_not = None
    while ready_or_not!=0:
        try:
            ready_or_not = int(input('Please input 0 once you\'re ready: '))
        except:
            print("Please enter 0 if you're ready: ")
    guesser()