# Control Flow

## if
```cpp
if (x == 100) {
	cout << "x" << endl;
} else if (x = 90) {
	cout << x << endl;
} else {
	cout << "default" << endl;
}
```

## switch
```cpp
int a;
switch(a) {
  case 1:
    cout << '1'; // prints "1",
    break;
  case 2:
    cout << '2'; // then prints "2"
    break;
  default:
    break;
}
```

## while
- while
```cpp
while (n > 0) {
	cout << n << endl;
	--n;
}
```
- do while
```cpp
do {
	cout << "Enter text: " << endl;
	cout << x;
} while (x);
```

## for
```cpp
for (int i = 0; i < 10; ++i) {
	cout << i << endl;
}
```