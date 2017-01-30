counter=0
while(counter<5):
    print counter
    counter +=1
else:
    print"counter value reached %d" %(counter)

#print out 1,2,3,4
for i in xrange(1,10):
    if(i%5==0):
        break
    print i
else:
    print"this is not printed because for loop is terminated because of break but not due to fail in condition"
