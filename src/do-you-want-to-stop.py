# You should write a loop around this question, and keep asking until
# the answer is "yes" (lower case).
n = 10
i = 1
while i <= n:
  print("Hello, World!")
  stop = input("Do you want to stop?")
  if stop == "yes":
    print(f"Stopped after {i}/{n} iterations.")
    break
  i += 1
  print(f"All {n}/{n} iterations finished!")
