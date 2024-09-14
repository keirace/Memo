# THREE.JS
## GLSL
- vite i glsl

in vite.config...
```
import 

```

hsl color (360deg, Sat, Lightness)
hsl(Math.random(), 100%, 70%)

## Shadows
* Person Closer Soft Shadow (PCSS)


## Event
```
console.log('---')
console.log('distance', event.distance) // Distance between camera and hit point
console.log('point', event.point) // Hit point coordinates (in 3D)
console.log('uv', event.uv) // UV coordinates on the geometry (in 2D)
console.log('object', event.object) // The object that triggered the event
console.log('eventObject', event.eventObject) // The object that was listening to the event (useful where there is objects in objects)

console.log('---')
console.log('x', event.x) // 2D screen coordinates of the pointer
console.log('y', event.y) // 2D screen coordinates of the pointer

console.log('---')
console.log('shiftKey', event.shiftKey) // If the SHIFT key was pressed
console.log('ctrlKey', event.ctrlKey) // If the CTRL key was pressed
console.log('metaKey', event.metaKey) // If the COMMAND key was pressed
```

In R3F there's no difference between onPointerOver and onPointerEnter

Occlusion
```
onClick={(e) => e.stopPropagation()}
```

Performance Boost for raycasting
* meshBounds - creates bounding sphere around the mesh - less precise
* Bvh - for more complex geometries
