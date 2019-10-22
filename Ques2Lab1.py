List = [{"V" : "S001"} , {"V" : "S002"} , {"VI" : "S001"} , {"VI" : "S005"} , {"VII" : "S005"} , {"V" : "S009"} , {"VIII" : "S007"}]
unique_value = set( val for dic in List for val in dic.values())
print("Unique Values: " , unique_value)
