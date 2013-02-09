def checkio(offers):
    '''
       the amount of money that Petr will pay for the ride
    '''
    initial_sofi, raise_sofi, initial_oldman, reduction_oldman = offers

    while True:
        if initial_sofi >= initial_oldman:
            return initial_sofi
        else:
            if initial_sofi + raise_sofi > initial_oldman:
                return initial_oldman

        initial_sofi += raise_sofi
        initial_oldman -= reduction_oldman

if __name__ == '__main__':
    first = checkio([150, 50, 1000, 100])
    print "first=", first
    assert first == 450, 'First'

    assert checkio([150, 50, 900, 100]) == 400, 'Second'
    assert checkio([500, 300, 700, 100]) == 700, 'Third'
    print 'All is ok'

