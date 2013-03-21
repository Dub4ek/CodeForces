inputData = raw_input('Input: ');
inputData = inputData.split(' ');

if inputData.len() == 2:
    n = inputData[0];
    k = inputData[1];

    if n >= 0 and n <= 10**5 and k <= n:
        print 'correct'
