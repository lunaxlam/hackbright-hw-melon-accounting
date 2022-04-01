"""An accounting program that outputs whether a customer overpaid or underpaid for their melon delivery."""

# constant variable for cost of melon
MELON_COST = 1.00

def accounting_report(melon_cost, customer_orders_filepath):
    """
    Calculates cost of melons and prints if customer overpaid or underpaid. 
    Returns None. 

    :param melon cost: cost of melon as a float
    :param: customer_orders_filepath: text file for customer order log as a string
    """

    # creates a customer_log file object by passing in the reference file
    customer_log = open(customer_orders_filepath)

    # reads each line in the file object
    for line in customer_log:
        line = line.rstrip()                       # removes excess whitespace to the right of the line
        words = line.split("|")                    # tokenizes the string of each line by the | delimiter, creating a list of the string elements

        customer_ID = words[0]                     # stores customer ID number
        customer_name = words[1]                   # stores customer name
        customer_melons = words[2]                 # stores customer melon count
        customer_paid = float(words[3])            # stores customer payment total

        # stores result of calculated customer expected payment total
        customer_expected = float(customer_melons) * melon_cost

        # checks if expected customer payment status does not == expected payment status
        if customer_expected != customer_paid:

            # calculate customer payment status difference
            underpaid = customer_expected - customer_paid
            overpaid = customer_paid - customer_expected

            # prints message detailing customer actual payment and expected payment status
            print(f"{customer_name.upper()}, ID# {customer_ID}\n{customer_name} paid ${customer_paid} for {customer_melons} melons, expected payment total: ${customer_expected:.2f}.")

            # prints underpaid or overpaid amount total depending on customer payment status
            if customer_paid < customer_expected:
                print(f"Balance owed by customer: ${underpaid:.2f}.\n")
            else:
                print(f"Refund owed to customer: ${overpaid:.2f}.\n")
    
    # closes the file object
    customer_log.close()

# calls the function
accounting_report(MELON_COST, "customer-orders.txt")