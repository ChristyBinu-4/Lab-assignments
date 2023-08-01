andGateInput = [
    [0, 0],
    [0, 1],
    [1, 0], 
    [1, 1]
]
andGateOutput = [0, 0, 0, 1]
weight = [0, 0]
new_weight = [0, 0]

flag = 0
i = 0
learningRate = 0.1
iteration = 0

while flag != 1:
    a, b = andGateInput[i]
    weight_a, weight_b = weight
    
    result = a * weight_a + b * weight_b #model
    
    #activation function
    if result < 0.5 :
        result = 0
    else : 
        result = 1
    
    if result != andGateOutput[i]:
        error = andGateOutput[i] - result
        weight_a_new = weight_a + (learningRate * error * a)
        weight_b_new = weight_b + (learningRate * error * b)
        new_weight = [weight_a_new, weight_b_new]
        print("new_weight : ", weight_a_new, weight_b_new)

    i = i + 1    
    if new_weight == [weight_a, weight_b] and i == len(andGateInput):
        flag = 1
    
    weight = new_weight
    if i > 3:
        i = 0

