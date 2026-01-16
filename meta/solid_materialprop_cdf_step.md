The material type for a step c.d.f. is `CDF step`.

For this material the c.d.f. is given by

\[
F\left(\Xi\right)=H\left(\Xi\right)\quad,
\]

where $H\left(\cdot\right)$ is the Heaviside unit step function. The step c.d.f. may be used to model fracture.

![FigDamageCDFStep.png](figs/FigDamageCDFStep.png)

_Example:_
```
<damage type="CDF step">
  <mu>1.0</mu>
  <Dmax>1</Dmax>
</damage>
```