# Prompt Recipes

Use these as directing patterns, not copy-and-paste decoration. Replace every bracketed variable and remove any line that does not serve the shot.

## Contents

- Base prompt compiler
- Camera recipes
- Portrait and character recipes
- Product recipes
- Space and environment recipes
- Food, artwork, and graphic recipes
- Constraint language
- Anti-patterns

## Base Prompt Compiler

### Director plan

```text
Shot function: [reveal / intimacy / inspection / follow / scale / tension / hold]
Shot size and angle: [medium close-up, eye level]
Primary camera move: [slow push-in]
Magnitude and direction: [small, straight forward]
Timing: [stable start, gradual move, smooth settle]
Subject motion: [one simple action]
Environment motion: [one supporting action]
Focus behavior: [locked / rack focus / shallow focus tracking]
Preserve: [identity, geometry, text, light, composition]
End frame: [specific final composition]
```

### Model-ready prompt

```text
The camera [primary move with direction, magnitude, and timing] as [subject motion].
[Environmental motion and focus behavior]. [Preservation statements]. One
continuous [duration]-second shot that [end-frame intent].
```

## Camera Recipes

### Slow push-in

Use for intimacy, tension, importance, or premium detail.

```text
The camera begins locked, then makes a very slow, small push toward [focal target].
[Subject] performs [micro-action]. [Environment] moves subtly. The original angle,
identity, and scene geometry remain stable. One continuous five-second shot that
settles on [end frame].
```

### Pull-out reveal

Use only when the source has enough edge reserve or a prepared wider environment.

```text
The camera slowly pulls backward from [initial detail], revealing [plausible context]
while keeping [subject] centered. Perspective expands naturally and the horizon,
architecture, and subject identity remain coherent. The move decelerates into a
wide final composition.
```

### Pan left or right

Use to redirect attention across visible or plausible adjacent space.

```text
From a fixed camera position, the camera pans slowly [left/right] from [source focal
point] to [destination focal point]. The motion remains level and stabilized.
[Supporting environment motion]. One continuous shot with a clean stop on the
destination.
```

### Tilt up or down

Use for height, scale, or detail-to-whole reveal.

```text
From a fixed camera position, the camera tilts slowly [up/down], beginning on
[start detail] and ending on [destination]. Vertical lines remain straight and the
horizon behaves naturally. The move settles without lateral drift.
```

### Small truck

Use when foreground and background separation is clear.

```text
The camera makes a small, constant-speed truck [left/right], creating restrained
parallax between [foreground], [subject], and [background]. Subject scale and
orientation remain stable. The camera settles after revealing [detail or relation].
```

### Partial arc

Use for product or character dimensionality. State the angle.

```text
The camera makes a very slow [10-25]-degree arc from [start side] toward [end side],
maintaining [subject] at nearly constant scale. Only a limited three-quarter view is
revealed. [Identity/product geometry] remains consistent and the camera settles on
a deliberate hero frame.
```

### Tracking alongside

Use when the subject already has a clear path.

```text
At [camera height], the camera tracks parallel to [subject] moving [direction] at a
steady pace, maintaining a consistent [medium/full] framing. The walk cycle remains
natural, ground contact stays stable, and the background passes with coherent
parallax. One continuous stabilized shot.
```

### Follow from behind

```text
The camera follows [subject] from a [rear three-quarter/shoulder-level] position as
they move into [space]. The distance and framing remain consistent. Perspective lines
guide the motion forward while identity, wardrobe, gait, and environment geometry
remain stable.
```

### Handheld observation

```text
The camera remains mostly locked with subtle low-amplitude handheld drift, as if
operated by a calm documentary camera operator. [Subject action]. Natural micro-shake
only, with no abrupt reframing or focus hunting.
```

### Macro glide and rack focus

```text
The camera glides a very short distance across [material detail], then performs one
controlled rack focus from [near detail] to [hero feature]. Surface texture and
product geometry remain precise. The move ends in a sharp commercial close-up.
```

## Portrait and Character Recipes

### Living portrait

```text
Very slow push-in toward the subject's eyes. The subject takes one natural breath,
blinks once, and makes a barely perceptible head adjustment. Hair responds gently to
a soft breeze. Facial identity, age, skin texture, wardrobe, and background remain
consistent. One quiet five-second portrait shot.
```

Do not request smiling, turning, speaking, hand movement, wind, and camera orbit at the same time.

### Tense close-up

```text
The camera begins locked in a close-up, then creeps forward a small distance as the
subject's expression tightens subtly. Focus remains on the eyes and the background
stays still. Identity and lighting direction remain unchanged. The shot settles into
an oppressive close frame.
```

### Fashion side tracking

```text
The camera tracks smoothly beside the model at waist height as they take two measured
steps [direction]. Garment fabric moves with believable weight while face, body
proportions, accessories, and clothing design remain stable. The background moves with
coherent lateral parallax. One continuous commercial fashion shot.
```

### Character entry into depth

```text
The camera follows from a rear three-quarter position as the character walks slowly
through [doorway/corridor/path]. The distance remains constant and the architecture
guides the forward motion. Gait, ground contact, costume, and identity remain coherent.
```

## Product Recipes

### Luxury hero arc

```text
The camera performs a very slow 15-degree arc from front-left toward a centered
three-quarter view, maintaining the product at constant scale. Controlled highlights
travel gently across [metal/glass/material]. Product silhouette, proportions, logo,
label, seams, and surface finish remain fixed. One continuous six-second shot that
settles into a clean hero frame.
```

### Packaging push-in

```text
The camera makes a small straight push toward the front label while the package
remains perfectly still. Studio light shifts only enough to reveal material texture.
Typography, logo, color, corners, and packaging proportions remain sharp and unchanged.
The shot ends with the full label readable.
```

### Jewelry macro inspection

```text
A macro camera glides slowly across [stone/setting/engraving] with extremely shallow
travel. One controlled rack focus moves from the near facet to the central setting.
Prismatic highlights shift naturally while stone count, metal geometry, engraving,
and clasp structure remain consistent.
```

### Cosmetic bottle pedestal

```text
The camera rises slowly by a small amount while maintaining a frontal three-quarter
view of the bottle. The pedestal and background remain aligned. Reflections slide
gently across the glass, while the cap, label, liquid level, bottle shape, and logo
remain stable. The final frame presents the full silhouette cleanly.
```

### Electronics detail reveal

```text
The camera makes a short lateral glide from [material edge] to [feature], creating
subtle parallax across the product surface. The screen, buttons, ports, printed marks,
and edge geometry remain fixed and legible. The move ends on a sharp close-up of
[feature].
```

### 360 request fallback

When only one view exists, do not write a fake full orbit prompt. Use:

```text
Create a restrained 20-degree inspection arc around the visible front three-quarter
surface only. Do not reveal the unseen back. Maintain the product silhouette, label,
and proportions, and settle back into a frontal hero composition.
```

Then recommend additional views for a true 360 deliverable.

## Space and Environment Recipes

### Corridor dolly

```text
The camera dollies slowly forward along the corridor's central perspective axis.
[Subject] moves at a calm pace ahead of the camera. Window light and haze shift subtly.
Walls, floor lines, doors, and vanishing point remain stable. One continuous shot with
a smooth stop at [destination].
```

### Architecture tilt reveal

```text
From a fixed position, the camera tilts upward from [entrance/detail] to reveal the
full height of [building/interior]. Vertical lines remain straight, the horizon stays
level, and light direction remains consistent. The move ends in a balanced wide frame.
```

### Landscape pan

```text
The camera pans slowly [direction] across the layered landscape, moving from [start]
to [destination]. Foreground foliage moves slightly in the wind, distant clouds drift
more slowly, and water reflections remain coherent. The horizon stays stable and the
camera stops cleanly on [destination].
```

### Drone-like rising reveal

Use only with strong layered depth.

```text
The camera rises slowly and moves slightly forward, revealing more of [valley/coast/
city] while keeping the horizon level. Foreground separates naturally from the distant
landscape. Atmospheric haze and cloud motion remain subtle. One smooth continuous rise.
```

### Cinemagraph

```text
The camera remains completely locked. Only [steam/waterfall/flame/reflection] moves in
a subtle continuous cycle while every other element remains still. Preserve the exact
composition and create a seamless [3-4]-second loop.
```

## Food, Artwork, and Graphic Recipes

### Food close-up

```text
The camera makes a very small push toward [dish/detail] as [steam/sauce/bubbles]
moves naturally. Focus remains on [hero texture]. Plate shape, garnish placement,
food structure, and lighting remain consistent. The shot settles into an appetizing
commercial close-up.
```

### Pour shot

```text
The camera remains locked in a close-up while [liquid] pours in one smooth stream into
[container]. The liquid has believable weight, splash, and surface tension. Container
geometry, label, hands, and background remain stable. No camera move competes with the
fluid action.
```

### Artwork with 2.5D parallax

```text
Create a restrained 2.5D camera drift [direction] using separated foreground,
midground, and background layers. Preserve the original illustration style, linework,
palette, and character design. Avoid volumetric reinterpretation beyond the prepared
layers. One smooth five-second move.
```

### Poster or logo animation

```text
Keep the camera locked and preserve all typography and logo geometry. Animate only
[specified graphic element] with [bounded motion]. Maintain exact alignment, color,
spacing, and readability. End on the original approved layout.
```

For exact typography, prefer post-production motion graphics over generative deformation.

## Constraint Language

Useful positive constraints:

- "maintains constant subject scale"
- "preserves the original camera angle"
- "the horizon remains level"
- "vertical architecture remains straight"
- "facial identity remains consistent throughout"
- "product geometry and printed text remain fixed and legible"
- "one continuous shot with no change of location"
- "the motion settles into a stable final frame"
- "only the specified element moves"

Dedicated negative prompt examples, when supported:

```text
warped face, duplicate limbs, unstable hands, deformed product, changing logo,
garbled text, reflection discontinuity, flicker, frame jump, abrupt cut,
unmotivated camera shake, focus pumping
```

## Anti-Patterns

Avoid:

- "cinematic camera movement" without naming the move;
- "360 product rotation" when the camera or object behavior is ambiguous;
- "zoom around" or other physically contradictory wording;
- several camera verbs joined by commas in a short clip;
- restating every visual detail from the source image;
- adding complex character action to compensate for a static frame;
- asking for exact readable text from an already weak source;
- ending without a target composition;
- using quality adjectives as substitutes for direction.
