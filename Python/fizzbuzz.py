_fb     = {3:'Fizz', 5:'Buzz'}
_fbi    = [3,5]
_fbmap  = {
  0x1:     _fb[3],
  0x2:     _fb[5],
  0x1|0x2: _fb[3]+_fb[5]
}
_fblist = []

ITERATIONS = 100

DEFAULT = 0x0
FLAGS   = {
  3: 0x1,
  5: 0x2
}
ALL     = 0xffff


def main():

  for i in range(ITERATIONS):
    _fb_flagint = fizzbuzz(i)
    if _fb_flagint == 0:
      _fblist.append(i)
    else:
      _fblist.append(_fbmap[_fb_flagint])

  print(_fblist)

def fizzbuzz(i):
  _fbstr = 0

  for x in _fbi:
    _fbstr |= FLAGS[x] * (not (i%x))
  
  return _fbstr

main()