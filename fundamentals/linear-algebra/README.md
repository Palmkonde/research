# Linear algebra
The linear algebra that qubit states need, and no more. A complex number $z$ has a modulus $\lvert z\rvert$ and a phase, and $\lvert z\rvert^2 = z^* z$ turns an amplitude into a probability. A state is a column vector of complex numbers, a linear combination of basis vectors such as $\lvert 0\rangle$ and $\lvert 1\rangle$. The inner product $\langle\phi\vert\psi\rangle = \sum_i \phi_i^* \psi_i$ gives lengths and overlaps, and a unit vector has length 1. Matrices are linear maps acting on vectors; a unitary matrix ($U^\dagger U = I$) keeps lengths and inner products, and the tensor (Kronecker) product joins vector spaces, multiplying their dimensions. For density matrices it also needs the trace, eigenvalues, and Hermitian ($A = A^\dagger$) and positive semidefinite matrices.

## Questions
- [ ] What is a complex vector space, and why does its inner product conjugate the first argument?
- [ ] What makes a matrix unitary, and why does a unitary preserve lengths and inner products?
- [ ] How does the tensor (Kronecker) product combine vectors and matrices, and why do the dimensions multiply?
- [ ] What are eigenvalues and eigenvectors, and why does a self-adjoint (Hermitian) matrix have real eigenvalues and an orthonormal eigenbasis?
