cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")
else:
    print("All cars built successfully. No faulty cars!")

# Este for com um else no mesmo nivel de indentação significa que caso o loop execute todo sem encontrar breaks ou continues irá executar o else.