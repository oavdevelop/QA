from merge import Concatenation

ss = Concatenation()
print('concat(5, 5), 10) = ', ss.concat(5, 5))
print('concat(0, "5"), 5) = ', ss.concat(0, "5"))
print('concat("5", 0), 5) = ', ss.concat("5", 0))
print('concat("100", "100"), 200) = ', ss.concat("100", "100"))
print('concat("foo", "bar"), "foobar") = ', ss.concat("foo", "bar"))

print('concat(0, 0), 0) = ', ss.concat(0, 0))
print('concat(1, 242424240000000000000000000000000), 242424240000000000000000000000001) = ', ss.concat(1, 242424240000000000000000000000000))
print('concat(-2000, 2000), 0) = ', ss.concat(-2000, 2000))
print('concat(-10, -10), -20) = ', ss.concat(-10, -10))

print('concat(0.002, 0.001), 0.003) = ', ss.concat(0.002, 0.001))
print('concat(0.0, 0), 0) = ', ss.concat(0.0, 0))
print('concat(0.0, 1), 1) = ', ss.concat(0.0, 1))
print('concat(.0, 0), 0) = ', ss.concat(.0, 0))
print('concat(.0, 1), 1) = ', ss.concat(.0, 1))
print('concat("", 0), "0") = ', ss.concat("", 0))
print('concat("", "foo"), "foo") = ', ss.concat("", "foo"))
print('concat(1.2E+1, 1.1), 13.1) = ', ss.concat(1.2E+1, 1.1))
print('concat([1], 4), 5) = ', ss.concat([1], 4))
print('concat(["foo"], 4), "foo4") = ', ss.concat(["foo"], 4))
print('concat([1, 2, 3], 4), "??") = ', ss.concat([1, 2, 3], 4))



