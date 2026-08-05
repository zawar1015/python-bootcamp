class InsufficientBalanceError(Exception):
    """Custom exception for low balance"""
    pass

balance = 5000

try:
    amount= int(input("Enter withdrawl amount : "))
    if amount < 0:
        raise ValueError("Withdrawl amount must be greater than 0")

    server_status = "online"

    if server_status != "online":
        raise ConnectionError("Bank server is unavailable .")

    if amount>balance:
        raise InsufficientBalanceError(
            f"available balance is only {balance}"
        )
    balance -= amount

except ValueError as e:
    print("Input error : ", e)

except ConnectionError as e:
    print("Network error : " , e)
except InsufficientBalanceError as e:
    print("Transaction failed : ", e)

else:
    print("Transaction successful .")
    print("Withdrawn amount : ", amount)
    print("Remaining Balance : ", balance)