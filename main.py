def main():
    print('Welcome to the Tip Calculator')
    pretotal = float(input('Total Bill: $'))
    party_size = int(input('Number of people to split bill: '))
    tip = float(input('Tip (10, 12, or 15): ')) / 100
    total_per_person = ((pretotal * tip) + pretotal) / party_size
    print(f'Each person should pay: ${total_per_person:.2f}')


if __name__ == '__main__':
    main()
