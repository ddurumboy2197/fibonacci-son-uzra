# test_fibonacci.py
import pytest
from fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_fibonacci_non_integer():
    with pytest.raises(TypeError):
        fibonacci(1.5)

def test_fibonacci_large():
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040
```

```javascript
// fibonacci.test.js
import fibonacci from './fibonacci';

describe('fibonacci', () => {
  it('should return 0 for n = 0', () => {
    expect(fibonacci(0)).toBe(0);
  });

  it('should return 1 for n = 1', () => {
    expect(fibonacci(1)).toBe(1);
  });

  it('should return 1 for n = 2', () => {
    expect(fibonacci(2)).toBe(1);
  });

  it('should return 2 for n = 3', () => {
    expect(fibonacci(3)).toBe(2);
  });

  it('should return 3 for n = 4', () => {
    expect(fibonacci(4)).toBe(3);
  });

  it('should return 5 for n = 5', () => {
    expect(fibonacci(5)).toBe(5);
  });

  it('should return 8 for n = 6', () => {
    expect(fibonacci(6)).toBe(8);
  });

  it('should return 13 for n = 7', () => {
    expect(fibonacci(7)).toBe(13);
  });

  it('should return 21 for n = 8', () => {
    expect(fibonacci(8)).toBe(21);
  });

  it('should return 34 for n = 9', () => {
    expect(fibonacci(9)).toBe(34);
  });

  it('should throw error for negative n', () => {
    expect(() => fibonacci(-1)).toThrowError();
  });

  it('should throw error for non-integer n', () => {
    expect(() => fibonacci(1.5)).toThrowError();
  });

  it('should return 55 for n = 10', () => {
    expect(fibonacci(10)).toBe(55);
  });

  it('should return 6765 for n = 20', () => {
    expect(fibonacci(20)).toBe(6765);
  });

  it('should return 832040 for n = 30', () => {
    expect(fibonacci(30)).toBe(832040);
  });
});
