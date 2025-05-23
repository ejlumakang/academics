class ParkingGarage:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.garage = [['_' for each in range(columns)] for each in range(rows)]

    def display_garage(self):
        for row in self.garage:
            print(' '.join(row)) 

    def park_vehicle(self, row, column):
        if 1 <= row <= self.rows and 1 <= column <= self.columns:
            if self.garage[row - 1][column - 1] == '_':
                self.garage[row - 1][column - 1] = 'P'
                print('Vehicle parked successfully.')
            else:
                print('Spot is already taken.')
        else:
            print('Invalid row or column number.')

    def retrieve_vehicle(self, row, column):
        if 1 <= row <= self.rows and 1 <= column <= self.columns:
            if self.garage[row - 1][column - 1] == 'P':
                self.garage[row - 1][column - 1] = '_'
                print('Vehicle retrieved successfully.')
            else:
                print('No vehicle found in the spot.')
        else:
            print('Invalid row or column number.')


def main():
    rows = 3  # Number of rows in the parking garage
    columns = 3  # Number of columns in the parking garage

    parking_garage = ParkingGarage(rows, columns)

    while True:
        print('Menu:')
        print('1. Park')
        print('2. Retrieve vehicle')
        print('3. Display garage')
        print('4. Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            row = int(input('Enter the row number (1 to {}): '.format(rows)))
            column = int(input('Enter the column number (1 to {}): '.format(columns)))
            parking_garage.park_vehicle(row, column)

        elif choice == 2:
            row = int(input('Enter the row number (1 to {}): '.format(rows)))
            column = int(input('Enter the column number (1 to {}): '.format(columns)))
            parking_garage.retrieve_vehicle(row, column)

        elif choice == 3:
            parking_garage.display_garage()

        elif choice == 4:
            print('Exiting the program.')
            break

        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()