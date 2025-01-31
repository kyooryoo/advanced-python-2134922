# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(f"bytes: {b}")
    
    s = "This is a string"
    print(f"string: {s}")
    
    # Try combining them. This will cause an error:
    # print(s+b)
    
    # Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    s2 = b.decode('utf-8')
    print(f"string: {s+s2}")
    
    b2 = s.encode('utf-8')
    print(f"bytes: {b2+b}")
    
    # encode the string as UTF-32
    b3 = s.encode('utf-32')
    print(f"bytes in UTF32: {b3}")
    
if __name__ == "__main__":
    main()
