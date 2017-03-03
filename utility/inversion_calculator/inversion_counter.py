def getInvCount(arr, n):

  inv_count = 0
  for i in range(n - 1):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            inv_count = inv_count + 1
  return inv_count

state = 0
batch_count = 0
batches = []
temp_array = []
with open('./mylogs_clean.log') as fp:
#with open('./test_log.txt') as fp:
    for line in fp:
        line = line.strip()
        if state == 0:
            if line == "batch_report_start":
                state = 1
                temp_array = []
                continue
        if state == 1:
            if line == "batch_report_end":
                batches.append(temp_array)
                state = 0
                continue   
        
        if line.isdigit():
            temp_array.append(int(line))

            #try:
            #    temp_array.append(int(line))
            #except:
            #    print(line)

j = 1
# for i in batches:
#     #print i
#     print(j, "Inversion" ,getInvCount(i, len(i)), len(i))
#     j = j + 1

for i in range(len(batches) - 1, len(batches) - 11, -1):
    print(j, "Inversion" ,getInvCount(batches[i], len(batches[i])), len(batches[i]))
    j = j + 1