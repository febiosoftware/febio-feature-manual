The force in the Hill discrete element is the sum of the passive element and the active element. 

\[
F=F_{p}+F_{a}
\]

The passive force is given by,

\[
F_{p}=\begin{cases}
F_{max}\left(\exp\left(Ksh\left(l-1\right)/L_{max}-1\right)/\exp\left(Ksh-1\right)\right) & ,l>1\\
0 & ,l\leqslant1
\end{cases}
\]

where l is the relative stretch defined by, l=lm/l0 and lmis the discrete element length and l0is either the L0 parameter, or the initial discrete element length (if L0 is set to zero). 

The active force is given by, 

\[
Fa=ac\,F_{max}\,F_{tl}\left(l\right)\,F_{tv}\left(v\right)
\]

Here, $v$, a measure of the relative discrete element's growth speed, is defined by,

\[
v=v_m/\left(V_{max}\,S_v\left(ac\right)\right)
\]

where $v_m$ is the actual discrete element's growth speed. 

The properties Sv, Ftl, and Ftv, are optional and will evaluate to 1 if omitted. They can be defined as load curves. See the example below. 

_Example:_
```
<discrete_material id="1" name="test" type="Hill">
  <Vmax>1</Vmax>
  <ac>0.1</ac>
  <Fmax>50</Fmax>
  <Ksh>5</Ksh>
  <Lmax>1.5</Lmax>
  <L0>10</L0>
  <Ftl type="point">
    <interpolate>smooth</interpolate> 				
    <points>
      <pt>0.0, 0</pt>
      <pt>0.1, 0.000258139</pt>
      <pt>0.2, 0.00161616</pt>
      <pt>0.3, 0.00740118</pt>
      <pt>0.4, 0.0272783</pt>
      <pt>0.5, 0.0820396</pt>
      <pt>0.6, 0.201851</pt>
      <pt>0.7, 0.406524</pt>
      <pt>0.8, 0.670275</pt>
      <pt>0.9, 0.904792</pt>
      <pt>1.0, 0.999955</pt>
      <pt>1.1, 0.904792</pt>
      <pt>1.2, 0.670275</pt>
      <pt>1.3, 0.406524</pt>
      <pt>1.4, 0.201851</pt>
      <pt>1.5, 0.0820396</pt>
      <pt>1.6, 0.0272783</pt>
      <pt>1.7, 0.00740118</pt>
      <pt>1.8, 0.00161616</pt>
      <pt>1.9, 0.000258139</pt>
      <pt>2.0, 0</pt>
	</points>
  </Ftl> 
</discrete_material> 
```