# Program converts miles driven to kilometers

def main():
  # Display intro message
    intro()
  
    try:
  # Get number of miles driven
        miles = float(input('Please enter number of miles driven: '))
      
  # Converts miles to kilometers
        miles_to_kilometers(miles)
      
    except ValueError:
        print("Please enter a valid number.")
        print()
        main()
      
  # Intro function displays intro when called
def intro():
    print("This program converts miles to kilometers")
    print("1 mile = 1.60934 kilometers")
    print()

  # The miles_to_kilometers function calculates number of kilometers from miless entered
  # and displays the miles and kilometers rounding to two decimal points and adding commas
def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    formatted_kilometers = f"{kilometers:,.2f}"
    formatted_miles = f"{miles:,.2f}"
    mile_plural = 'mile' if miles == 1 else 'miles'
    kilometer_plural = 'kilometer' if kilometers == 1 else 'kilometers'

    print(f'You have driven {formatted_miles} {mile_plural} which is equal to {formatted_kilometers} {kilometer_plural}')

  # Call the main function
main()

