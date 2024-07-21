import numpy as np

def find_roots(a, b, c):
    coefficients = [a] + [0]*18 + [b, c]
    roots = np.roots(coefficients)
    return roots

def calculate_spectral_radius(roots):
    spectral_radius = max(abs(root) for root in roots)
    return spectral_radius

if __name__ == "__main__":
    a = float(input("Enter the value for a: "))
    b = float(input("Enter the value for b: "))
    c = float(input("Enter the value for c: "))
    
    roots = find_roots(a, b, c)
    
    print("The roots of the polynomial are:")
    for root in roots:
        print(root)
    
    spectral_radius = calculate_spectral_radius(roots)
    print(f"The spectral radius is: {spectral_radius}")