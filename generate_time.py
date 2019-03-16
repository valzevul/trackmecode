with open("results") as file:
    res = file.readlines()
final_results = dict() 
for line in res:
    params = line.split(",")
    (build_type, build_time) = (params[-2], params[-1])
    try:
        final_results[build_type] += int(build_time)
    except KeyError:
        final_results[build_type] = int(build_time)
print(final_results)
