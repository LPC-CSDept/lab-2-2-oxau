def main():
    ##################################################
    # Comlete your code here
    ##################################################
    workhours = int(input('Hours worked: '))
    reg_hours = 40
    reg_rate = 18.25
    o_rate = 27.78
    if (workhours > 40):
        reg_charge = reg_rate * 40
        overtime_charge =  (workhours - 40)*o_rate
        total_wages = ((workhours - 40)*o_rate) + reg_charge
    elif (workhours <= 40):
        reg_charge = (reg_rate * workhours)
        overtime_charge = 0
        total_wages = (workhours*reg_rate)

    print ('Regular Charge: ' + str(reg_charge))
    print ('Overtime Charge: ' + str(overtime_charge))
    print ('Total Wage: ' + str(total_wages))
    pass


if __name__ == '__main__':
    main()
