The `rigid_euler_angles` constraint allows the user to prescribe the rotation of a rigid body using three Euler angles. 

The `rb` parameter is the name attribute assigned to the corresponding rigid body material as defined in the Material section.

The following example prescribes a rotation around the z-axis using a load controller. 

```
<rigid_bc type="rigid_euler_vector">
  <rb>rigid</rb>
  <vx>0</vx>
  <vy>0</vy>
  <vz lc="1">180.0</vz>
</rigid_bc>
```