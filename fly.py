import insect as i

def main():
    housefly = i.Insectclass(2,4)
    mosquito = i.Insectclass(3,6)

    housefly.flight_len()
    mosquito.flight_len()

    print('This insect is this distance:', housefly.get_flight())
    print('This insect is this distance:', mosquito.get_flight())

main()