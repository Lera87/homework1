customer_code = str(input("Please enter your customer code: "))
beginning_meter = int(input("Please enter your beginning meter reading: "))
ending_meter = int(input("Please enter your ending meter reading: "))

water_used = ending_meter - beginning_meter

if beginning_meter > ending_meter:
    water_used_total = (((999999999 - beginning_meter) + 1) + ending_meter) * 0.1
else:
    water_used_total = water_used * 0.1


if customer_code.lower() == 'r':
    total_bill = (5.00 + (water_used_total * 0.0005))

elif customer_code.lower() == 'c':
    if water_used <= 4000000:
        total_bill = 1000.00
    elif water_used > 4000000:
        total_bill = (1000.00 + (water_used_total * 0.00025))

elif customer_code.lower() == 'i':
    if water_used_total <= 4000000:
        total_bill = 1000.00
    elif water_used > 4000000 and water_used <= 10000000:
        total_bill = 2000.00
    elif water_used > 10000000:
        total_bill = 2000.00 + (water_used_total * 0.00025)


print("**************************************")
print("Customer code: ", customer_code)
print("Beginning meter reading: ", beginning_meter)
print("Ending meter reading: ", ending_meter)
print("Gallons of water used: {:.1f}".format(water_used_total))
print("Amount billed: ${:.2f}".format(total_bill))
