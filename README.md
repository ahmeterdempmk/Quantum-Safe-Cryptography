# Quantum-Safe-Cryptography

A comprehensive implementation of cryptographic algorithms designed to be resistant to quantum computing attacks. This repository contains implementations of various cryptographic protocols across asymmetric, symmetric, and hash-based approaches.

## Overview

Quantum computers pose a significant threat to many widely-used cryptographic algorithms. This repository provides educational implementations of both traditional cryptographic methods and quantum-resistant alternatives to help understand the landscape of post-quantum cryptography.

## Directory Structure
```
Quantum-Safe-Cryptography/
├── Asymmetric Key Cryptography/
│   ├── app.py
│   ├── breaking_rsa.py
│   ├── diffie_hellman_protocol.py
│   └── dsa.py
├── Hash Functions/
│   └── app.py
├── Symmetric Key Cryptography/
│   └── app.py
└── LICENSE
```

## Features

### Asymmetric Key Cryptography
- **RSA Implementation**: Standard RSA algorithm implementation with demonstration of its vulnerability to quantum attacks.
- **Breaking RSA**: Demonstrates methods that could be used by quantum computers to break RSA encryption.
- **Diffie-Hellman Protocol**: Implementation of the classic key exchange protocol.
- **DSA (Digital Signature Algorithm)**: Implementation of DSA for digital signatures.

### Hash Functions
- Implementation of various cryptographic hash functions.
- Demonstrations of their applications in security.

### Symmetric Key Cryptography
- Implementation of symmetric encryption algorithms.
- Analysis of their resistance to quantum computing attacks.

### Installation
```bash
git clone https://github.com/yourusername/Quantum-Safe-Cryptography.git
cd Quantum-Safe-Cryptography
```

## Security Notice

The implementations in this repository are primarily for educational purposes. While they demonstrate the principles of quantum-safe cryptography, they have not undergone the rigorous security auditing required for production systems.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the terms of the LICENSE file in this repository. Unless otherwise stated, you can use and modify this code for personal or educational purposes.

## References

- [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [RFC 8017: RSA Cryptography Standard](https://tools.ietf.org/html/rfc8017)
- [RFC 7748: Elliptic Curves for Security](https://tools.ietf.org/html/rfc7748)
- [RFC 6234: US Secure Hash Algorithms (SHA and HMAC-SHA)](https://tools.ietf.org/html/rfc6234)
- [IBM Quantum: Practical Introduction to Quantum-Safe Cryptography](https://learning.quantum.ibm.com/course/practical-introduction-to-quantum-safe-cryptography)
