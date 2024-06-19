# kpoints_epsilon
Generation of kpoints for epsion.x calculations in quantum espresso

The calculation of epsilon.x needs a high number of kpoints and it must be defined by "hand". This small program create the kpoitns depending on crystal, and it is posible to select the k1xk2xk3 grid. The weight is just calculated as the 1 divided by the total kpoints.

input parameters: kx, ky, kz points.
