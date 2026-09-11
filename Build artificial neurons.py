x1 = 2 
x2 = 3 
w1 = 0.5
w2 = 0.8

bias = 1
# formula 
# z= w1 x1 + w2 x2 +...+wn xn + b

z = (x1 * w1) + (x2 * w2) + bias

# x = input
# w = weight
# z = pre-activation value 

output  = max(0, z)
print("Weighted Sum:", z)
print("Output:", output)
