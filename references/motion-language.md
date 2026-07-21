# Professional Motion Language

Use this reference to choose and describe camera movement. Treat the terms as physical camera behaviors, not interchangeable style words.

## Contents

- Camera physics
- Movement families
- Narrative intent
- Magnitude, speed, and timing
- Motion hierarchy
- Combination rules
- Prompt language
- Fast decision table

## Camera Physics

### Rotation around a fixed camera position

Rotation changes where the lens points but does not move the camera through space.

- **Pan / 摇镜**: rotate left or right.
- **Tilt / 俯仰**: rotate up or down.
- **Roll**: rotate around the lens axis.

Image-to-video risk is usually lower because the model can reuse much of the visible scene. Risk rises when the move reaches beyond the image boundary or reveals large unseen areas.

### Translation through space

Translation changes camera position and therefore changes perspective, overlap, and parallax.

- **Dolly / 推拉**: move forward or backward.
- **Truck / 横移**: move left or right parallel to the scene.
- **Pedestal / 升降**: move vertically without tilting.
- **Crane or jib / 摇臂**: move vertically and often laterally on an arc.
- **Tracking / 跟拍**: move with a subject while preserving a relationship.
- **Orbit or arc / 环绕**: travel around a subject.

Image-to-video risk is higher because the model must infer surfaces and spatial relations not visible in the source image.

### Optical framing change

- **Zoom / 变焦**: change focal length and field of view while the camera remains in place.
- **Digital crop**: enlarge or crop the frame without optical perspective behavior.
- **Rack focus / 移焦**: change the plane of sharp focus without moving the camera.

A zoom changes framing but does not create the perspective shift of a dolly. A dolly changes the apparent size relationship between foreground and background. Do not use "zoom" and "dolly" as synonyms.

### Combined optical and physical moves

- **Dolly zoom**: dolly and zoom in opposite directions to keep the subject size similar while the background perspective changes.
- **Crash zoom**: very fast focal-length change used for impact.
- **Push with focus pull**: move toward a subject while transferring focus to a detail.

These moves need strong geometry, clear focal targets, and a model capable of following sequential instructions. They are not default I2V choices.

## Movement Families

| Movement | Physical behavior | Typical intent | Single-image risk | Safe first test |
| --- | --- | --- | --- | --- |
| Static / locked | No camera motion | observation, formality, tension | very low | subject or environment micro-motion only |
| Push-in | Slow forward move | intimacy, importance, tension | low-medium | small travel, 3-5s |
| Pull-out | Slow backward move | context, isolation, reveal | medium | reveal only existing or plausible surroundings |
| Pan | Fixed-position horizontal rotation | scan, follow, reveal adjacency | low-medium | short controlled pan within frame reserve |
| Tilt | Fixed-position vertical rotation | height, scale, reveal | low-medium | preserve vertical lines and horizon logic |
| Truck | Sideways translation | inspection, parallax, spatial discovery | medium-high | small move with layered depth |
| Pedestal | Vertical translation | product inspection, elevation | medium-high | small move with clean background |
| Crane/jib | Vertical plus lateral arc | scale, dramatic reveal | high | use only with strong depth and open environment |
| Arc | Partial travel around subject | dimensionality, relation | medium-high | 10-25 degrees |
| Orbit | Travel around subject | inspection, entrapment, hero reveal | high | avoid above 45 degrees from one view |
| Tracking | Move alongside a subject | continuity and action | medium-high | clear path and simple gait |
| Follow | Move behind or beside subject | immersion, pursuit | medium-high | subject already oriented into depth |
| Lead | Move backward ahead of subject | engagement, anticipation | high | face and gait references should be strong |
| Handheld | Controlled positional and rotational instability | realism, urgency | low geometry risk, high taste risk | low amplitude, low frequency |
| Steadicam | Smooth body-level following move | polished immersion | medium | one path, no abrupt direction changes |
| Whip pan | Extremely fast pan with blur | transition or shock | medium-high | short, one clear source and destination |
| Macro glide | Small translating move across detail | material, craft, luxury | medium | shallow travel, stable product geometry |
| Rack focus | Change focus target | redirect attention | low-medium | two clearly separated depth planes |

## Narrative Intent

### Increase intimacy or importance

Use a slow push-in, restrained zoom-in, or focus transfer toward the subject. Prefer a physical push when the environment has useful depth; prefer a zoom or crop when depth confidence is low.

### Reveal context

Use pull-out, tilt, pan, or a limited crane. The destination must contain plausible information. A pull-out from a tightly cropped image can invent an entire room and should be treated as high risk.

### Inspect a product

Use macro glide, small truck, pedestal, shallow arc, or a slow push into a material detail. Preserve silhouette, proportions, seams, ports, label, typography, and reflection logic. A real 360 showcase requires multiple views or a 3D-capable reconstruction workflow.

### Follow action

Use tracking, follow, lead, or steadicam language only when the subject has a readable direction of travel and enough space. State the camera-subject relationship: parallel, behind, three-quarter front, shoulder height, or low angle.

### Express scale

Use tilt-up, crane-up, wide push-in, aerial drift, or pull-back. Keep the horizon and vertical architecture coherent.

### Create tension

Use creeping push-in, locked oppressive frame, minimal handheld drift, or a slow arc that reveals a relationship. Fast orbit and decorative shake usually reduce tension by turning the scene into spectacle.

### Create isolation

Use pull-out, static wide shot, or a slow rise that makes the subject smaller. Protect negative space and do not let background invention become the focal point.

### Observe objectively

Use locked-off, slow pan, or restrained documentary handheld. Movement should feel motivated by attention, not by a desire to keep every frame moving.

## Magnitude, Speed, and Timing

### Travel magnitude

- **Minimal**: almost static; micro-drift, breathing camera, focus change.
- **Small**: enough motion to read, but composition remains substantially intact.
- **Medium**: clear parallax or angle evolution; requires reliable depth.
- **Large**: substantial new viewpoint or environment reveal; needs multiple references, explicit camera controls, or strong 3D reconstruction.

For one still, default to minimal or small.

### Angular guidance

- `5-15 degrees`: subtle dimensional arc; usually the safest product or portrait option.
- `15-30 degrees`: clear three-dimensional inspection; requires depth and edge reserve.
- `30-45 degrees`: high reconstruction load; inspect unseen surfaces and identity drift.
- `45-90 degrees`: use only with strong references or an explicitly capable workflow.
- `180-360 degrees`: do not promise from one front view. Require multi-view, generated turnaround, reference video, or a 3D asset.

### Speed language

- **Very slow**: contemplative, premium, forensic, emotionally heavy.
- **Slow**: default professional I2V pace; readable and stable.
- **Medium**: commercial energy with controlled detail.
- **Fast**: action, impact, whip pan, or crash zoom; use short duration and clear end state.

Use speed plus motion shape:

- "begins almost imperceptibly, accelerates gently, then settles"
- "constant slow lateral glide"
- "quick pan with controlled motion blur, stopping cleanly on the product"
- "smooth long-tail deceleration into the final hero frame"

Avoid relying on abstract easing names unless the provider exposes numeric controls.

### Time structure

For a 5-second shot:

1. Hold the source composition for roughly `0.25-0.5s`.
2. Develop one primary motion over roughly `3-3.5s`.
3. Decelerate into a readable final frame for roughly `0.75s`.

For a 3-second shot, remove secondary motion before increasing speed.

## Motion Hierarchy

Choose one dominant layer:

1. **Camera-led**: product inspection, reveal, scale, spatial discovery.
2. **Subject-led**: portrait micro-expression, walking, cloth, liquid, machinery.
3. **Environment-led**: clouds, fog, rain, reflections, foliage, practical light.
4. **Near-static**: tension, luxury still life, evidence insert, formal portrait.

Supporting layers should remain lower in amplitude and complexity than the dominant layer.

Example hierarchy:

```text
Primary: slow 15-degree arc around the watch.
Secondary: reflections slide subtly across the metal.
Hold: watch geometry, hands, logo, and dial markings remain fixed.
```

Bad hierarchy:

```text
Orbit rapidly while zooming, crane upward, rotate the watch, animate the background,
change the lighting, and rack focus repeatedly.
```

## Combination Rules

Good combinations:

- push-in + subtle subject breathing;
- small arc + controlled reflection movement;
- tracking + simple walking cycle;
- static frame + atmospheric motion;
- macro glide + one rack focus;
- pull-out + slight environment reveal.

Risky combinations:

- orbit + truck + zoom;
- fast camera + complex full-body action;
- crane + large subject rotation;
- dolly zoom + changing focal subject;
- whip pan + long exposure-like environment motion;
- multiple direction reversals in one short shot.

When a prompt needs "then", confirm that the duration can make both beats readable. Otherwise split the idea into two shots.

## Prompt Language

### Strong motion instruction

```text
The camera makes a very slow 15-degree arc from front-left toward a centered
three-quarter view, maintaining the product at constant scale. Reflections move
gently across the brushed metal while the logo, dial markings, proportions, and
background geometry remain stable. One continuous five-second shot that settles
into a clean hero frame.
```

### Weak motion instruction

```text
Make it cinematic with a cool 360 camera move, dynamic lighting, epic zooms,
smooth motion, 4K quality.
```

The weak version has no bounded path, no hierarchy, no preservation target, and no end frame.

### Positive preservation language

Prefer:

- "the face remains identity-consistent throughout"
- "the packaging shape and printed label remain fixed and legible"
- "the camera preserves the original horizon and architectural lines"
- "the composition remains centered with constant subject scale"

Use a provider's negative-prompt field, when supported, for concise failure modes such as duplicate limbs, warped text, flicker, or camera shake.

## Fast Decision Table

| Source condition | Prefer | Avoid |
| --- | --- | --- |
| Flat portrait, little depth | push-in, zoom, micro-drift | large orbit, truck, crane |
| Product centered with clean separation | small arc, macro glide, pedestal | 360 from one view |
| Corridor or road with strong leading lines | dolly-in, follow | lateral orbit |
| Wide landscape with layered depth | slow pan, small truck, drone-like push | fast multi-axis move |
| Architecture with strict verticals | locked, tilt, straight dolly | roll, unstable handheld |
| Food or liquid close-up | macro glide, rack focus, slow push | large camera travel |
| Illustration with flat layers | pan, zoom, 2.5D parallax | realistic full orbit |
| Weak or artifacted source | static or regenerate source | any move that magnifies defects |
